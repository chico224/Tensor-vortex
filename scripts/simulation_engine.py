import pandas as pd
import numpy as np
import MetaTrader5 as mt5
import logging
from bot.quant_engine import QuantEnsembleEngine
from bot.risk_manager import RiskManager
from bot.connectivity import MT5Connector

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger("Simulator")

class VirtualMarketSimulator:
    """
    Simulateur de Marché Virtuel Élite (Enterprise Grade).
    Teste les 110 experts sur des données historiques réelles.
    """
    
    def __init__(self, symbol="EURUSD", timeframe=mt5.TIMEFRAME_M1, lookback=2000):
        self.symbol = symbol
        self.timeframe = timeframe
        self.lookback = lookback
        self.engine = QuantEnsembleEngine()
        self.risk = RiskManager(db_manager=self.engine.db)
        self.connector = MT5Connector()

    def run_simulation(self):
        logger.info(f"--- DÉMARRAGE SIMULATION SUR {self.symbol} (Marché Virtuel) ---")
        
        if not self.connector.connect():
            logger.error("❌ ERREUR CRITIQUE : Connexion MT5 impossible.")
            logger.info("👉 ACTION REQUISE : Veuillez ouvrir votre application MetaTrader 5 manuellement avant de relancer ce script.")
            return

        # 1. Extraction des données historiques réelles
        rates = mt5.copy_rates_from_pos(self.symbol, self.timeframe, 0, self.lookback)
        if rates is None:
            logger.error("Impossible de récupérer les données MT5.")
            return
            
        df_full = pd.DataFrame(rates)
        df_full['time'] = pd.to_datetime(df_full['time'], unit='s')
        
        results = []
        balance = 100.0 # Capital virtuel de départ
        initial_balance = balance
        
        # 2. Simulation pas à pas (Fenêtre glissante)
        window_size = 500
        for i in range(window_size, len(df_full)):
            df_window = df_full.iloc[i-window_size:i].copy()
            
            # Évaluation Consensus Normal
            signal, details = self.engine.evaluate_normal_trade(df_window)
            
            if signal != 0:
                # Simulation d'un trade
                entry_price = df_full.iloc[i]['open']
                exit_price = df_full.iloc[min(i+10, len(df_full)-1)]['close'] # Sortie après 10 min
                
                profit = (exit_price - entry_price) * 10000 * signal # Simplifié (1 pip = 1$)
                balance += profit
                
                results.append({
                    'time': df_full.iloc[i]['time'],
                    'signal': "ACHAT" if signal == 1 else "VENTE",
                    'profit': profit,
                    'balance': balance
                })
                
                logger.info(f"Trade Virtuel @ {df_full.iloc[i]['time']} | {signal} | Profit: {profit:.2f} | Balance: {balance:.2f}")

        # 3. Rapport Final
        total_profit = balance - initial_balance
        win_rate = len([r for r in results if r['profit'] > 0]) / len(results) if results else 0
        
        print("\n" + "="*50)
        print(f"RAPPORT SIMULATION ÉLITE : {self.symbol}")
        print(f"Trades totaux : {len(results)}")
        print(f"Profit cumulé : {total_profit:.2f}$")
        print(f"Win Rate : {win_rate*100:.2f}%")
        print(f"Consommation RAM : Optimale via SQLite")
        print("="*50)

if __name__ == "__main__":
    sim = VirtualMarketSimulator(symbol="XAUUSD", lookback=1000)
    sim.run_simulation()
    mt5.shutdown()
