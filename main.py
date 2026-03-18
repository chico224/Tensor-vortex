import os
import sys
import time
import logging
import MetaTrader5 as mt5
from bot.connectivity import MT5Connector
from bot.quant_engine import QuantEnsembleEngine
from bot.risk_manager import RiskManager
from bot.executor import OrderExecutor
from bot.omega_bridge import OmegaBridge

# S'assurer que les dossiers existent
os.makedirs("logs", exist_ok=True)
os.makedirs("data", exist_ok=True)

# Configuration du Logging de Niveau Entreprise
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler("logs/bot_execution.log"),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger("MainControl")

class SurvivorBot:
    def __init__(self):
        self.is_running = False
        self.connector = MT5Connector()
        self.engine = QuantEnsembleEngine()
        self.risk = RiskManager()
        self.executor = OrderExecutor()
        self.bridge = OmegaBridge(self)

    def start(self):
        if not self.connector.connect():
            logger.error("Échec de connexion MT5.")
            return False
        
        self.is_running = True
        logger.info("Survivor Bot Démarré.")
        
        # Lancement de la boucle de trading dans un thread pour laisser le bridge répondre
        threading.Thread(target=self._trading_loop).start()
        return True

    def stop(self):
        self.is_running = False
        logger.info("Survivor Bot mis en pause.")

    def _trading_loop(self):
        symbols = ["EURUSD", "XAUUSD", "USDJPY"]
        while self.is_running:
            try:
                for symbol in symbols:
                    if not self.is_running: break
                    
                    # Analyse via le consensus d'experts
                    signal, details = self.engine.analyze(symbol)
                    
                    if signal:
                        # Vérification du Risque via SurvivorBrain
                        if self.risk.validate_trade(symbol, signal):
                            self.executor.execute(symbol, signal, details)
                
                time.sleep(10) # Scan toutes les 10 secondes
            except Exception as e:
                logger.error(f"Erreur boucle: {e}")
                time.sleep(5)

if __name__ == "__main__":
    import threading
    bot = SurvivorBot()
    bot.bridge.start_bridge()
    bot.start()
