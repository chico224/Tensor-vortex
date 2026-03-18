import logging
from datetime import datetime

logger = logging.getLogger("RiskManager")

class RiskManager:
    """
    Gestionnaire de risque institutionnel (Enterprise Grade).
    Prend en charge les très petits capitaux (5$ - 10$) via l'adaptation 
    aux comptes "Cent" pour respecter la règle des 1%.
    """

    def __init__(self, db_manager, max_risk_pct=0.01, max_consecutive_losses=3):
        self.max_risk_pct = max_risk_pct
        from ai.brain import SurvivorBrain
        self.survivor = SurvivorBrain(db_manager)
        
        # Limites quotidiennes par symbole (Hyper-Scale)
        self.max_daily_normal = 200
        self.max_daily_sniper = 10
        
        self.daily_normal_trades = {} # {'EURUSD': 5, 'XAUUSD': 12}
        self.daily_sniper_trades = {}
        self.last_trade_date = None

    def _reset_daily_counters(self):
        """Réinitialise les compteurs si on est sur un nouveau jour."""
        current_date = datetime.now().date()
        if self.last_trade_date != current_date:
            self.daily_normal_trades.clear()
            self.daily_sniper_trades.clear()
            self.last_trade_date = current_date
            
    def _increment_trade_count(self, symbol, is_sniper=False):
        """Incrémente le compteur après exécution."""
        self._reset_daily_counters()
        if is_sniper:
            self.daily_sniper_trades[symbol] = self.daily_sniper_trades.get(symbol, 0) + 1
        else:
            self.daily_normal_trades[symbol] = self.daily_normal_trades.get(symbol, 0) + 1

    def can_trade(self, symbol, is_sniper=False):
        """
        Vérifie le statut de survie (Kill-Switch) ET les limites par symbole.
        """
        self._reset_daily_counters()
        
        # 1. Vérifie le Kill-Switch Global
        if not self.survivor.check_survival_status():
            return False
            
        # 2. Vérifie les limites par symbole
        if is_sniper:
            count = self.daily_sniper_trades.get(symbol, 0)
            if count >= self.max_daily_sniper:
                logger.debug(f"Limite Sniper journalière atteinte pour {symbol} ({self.max_daily_sniper}/j).")
                return False
        else:
            count = self.daily_normal_trades.get(symbol, 0)
            if count >= self.max_daily_normal:
                logger.debug(f"Limite Normale journalière atteinte pour {symbol} ({self.max_daily_normal}/j).")
                return False
                
        # /!\ L'incrémentation (_increment_trade_count) doit être appelée 
        # par l'exécuteur APRÈS un trade réussi, pas ici.
        return True

    def calculate_lot_size(self, balance, stop_loss_pips, pip_value, symbol_info):
        """
        Calcule la taille du lot pour risquer exactement 1% du capital.
        Adaptation Hyper-Scale : Gère automatiquement les comptes Cent, Standard, et ECN.
        symbol_info: Objet fourni par mt5.symbol_info(symbol)
        """
        risk_amount = balance * self.max_risk_pct
        
        if stop_loss_pips == 0 or pip_value == 0 or symbol_info is None:
            return 0.0
            
        # Calcul theorique
        raw_lot_size = risk_amount / (stop_loss_pips * pip_value)
        
        # Adaptation dynamique aux regles du compte (Standard/Cent/ECN)
        min_lot = symbol_info.volume_min
        max_lot = symbol_info.volume_max
        vol_step = symbol_info.volume_step
        
        # Arrondi au pas (step) autorise par le broker
        lot_size_steps = round(raw_lot_size / vol_step)
        lot_size = lot_size_steps * vol_step
        
        # Securite vitale (Zero Cramage)
        if lot_size < min_lot:
             logger.warning(f"Capital ({balance}$) insuffisant pour risquer 1% avec {stop_loss_pips} pips de SL sur un compte standard. Lot theorique: {lot_size}. On force le minimum: {min_lot}.")
             # L'utilisateur avec 5$ sur un compte Standard prendra plus de 1% de risque.
             # On accepte, mais on previendra dans l'interface utilisateur.
             lot_size = min_lot
             
        if lot_size > max_lot:
             lot_size = max_lot
             
        # Format propre (ex: 0.01 ou 0.001) base sur le step
        # Astuce : Convertir en string via format pour eviter les erreurs de float Python
        precision = len(str(vol_step).split('.')[1]) if '.' in str(vol_step) else 0
        lot_size = float(f"{lot_size:.{precision}f}")
             
        return lot_size

    def record_trade_result(self, symbol, profit, is_sniper=False):
        """Met à jour le cerveau Survivor après chaque trade ET incrémente les limites."""
        self._reset_daily_counters()
        self.survivor.update_results(profit)
        self._increment_trade_count(symbol, is_sniper)
