import MetaTrader5 as mt5
import logging

logger = logging.getLogger("OrderExecutor")

class OrderExecutor:
    """
    Exécuteur d'ordres de niveau Enterprise.
    Gère l'envoi, la modification et la fermeture des positions MT5.
    Intègre une sécurité native contre les erreurs de broker.
    """
    
    def __init__(self, risk_manager):
        self.risk = risk_manager

    def execute_trade(self, symbol, signal, price, sl_pips, tp_pips, comment="", is_sniper=False):
        """Envoie un ordre au marché avec SL et TP calculés."""
        
        # 1. Obtenir les infos du compte et du symbole (Hyper-Scale)
        account_info = mt5.account_info()
        symbol_info = mt5.symbol_info(symbol)
        
        if account_info is None or symbol_info is None:
            logger.error(f"Impossible d'obtenir les infos pour le compte ou le symbole {symbol}.")
            return None
            
        balance = account_info.balance
        
        # Calcul du pip_value basé sur la valeur du tick
        # Note: Un tick n'est pas toujours un pip (ex: 5 decimales = 1 tick = 0.1 pip)
        # On simplifie pour l'architecture 100% Mathématique
        tick_value = symbol_info.trade_tick_value
        tick_size = symbol_info.trade_tick_size
        point = symbol_info.point
        
        # Si EURUSD (point=0.00001, pip=0.0001)
        pip_multiplier = 10 if point < 0.001 else 1 
        pip_value = tick_value * (point * pip_multiplier) / tick_size

        # 2. Vérification du volume (lot size) en passant l'objet symbol_info
        lot = self.risk.calculate_lot_size(balance, sl_pips, pip_value, symbol_info)
        
        if lot < symbol_info.volume_min:
            logger.error(f"Lot calculé ({lot}) inférieur au minimum du broker ({symbol_info.volume_min}) pour {symbol}.")
            return None

        # 3. Préparation du type d'ordre
        order_type = mt5.ORDER_TYPE_BUY if signal == 1 else mt5.ORDER_TYPE_SELL
        
        # 4. Calcul SL / TP
        deviation = 20
        
        sl = price - (sl_pips * point * pip_multiplier * signal)
        tp = price + (tp_pips * point * pip_multiplier * signal)
        
        request = {
            "action": mt5.TRADE_ACTION_DEAL,
            "symbol": symbol,
            "volume": lot,
            "type": order_type,
            "price": price,
            "sl": sl,
            "tp": tp,
            "deviation": deviation,
            "magic": 123456,
            "comment": comment if comment else f"Quant Signal {signal}",
            "type_time": mt5.ORDER_TIME_GTC,
            "type_filling": mt5.ORDER_FILLING_IOC,
        }

        # 5. Envoi de l'ordre
        result = mt5.order_send(request)
        
        if result.retcode != mt5.TRADE_RETCODE_DONE:
            logger.error(f"Échec de l'ordre sur {symbol}: {result.comment} (Code: {result.retcode})")
            return None
            
        logger.info(f"✅ Trade {mode_str(signal)} ouvert sur {symbol} | Lot: {lot}")
        
        # 6. INCEREMENTATION DU COMPTEUR (Limites Hyper-Scale)
        # On suppose un profit theorique moyen pour l'exemple
        self.risk.record_trade_result(symbol, profit=0.0, is_sniper=is_sniper)
        
        return result

def mode_str(signal):
    return "ACHAT" if signal == 1 else "VENTE"
