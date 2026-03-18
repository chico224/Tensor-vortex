import numpy as np
import logging

logger = logging.getLogger("StatArb3D")

class StatisticalArbitrageTriangular:
    """
    ARBITRAGE STATISTIQUE 3D (Triangular Covariance)
    100% Mathématique. Traque les déséquilibres nanosecondes dans l'équation :
    EURUSD * USDJPY = EURJPY
    Si (EURUSD * USDJPY) - EURJPY != 0 au-delà des frais, lance un tir croisé.
    """
    def __init__(self, target_spread_pips=1.5):
        self.target_spread = target_spread_pips * 0.0001
        
    def check_triangle_anomaly(self, eurusd_ask, eurusd_bid, usdjpy_ask, usdjpy_bid, eurjpy_ask, eurjpy_bid):
        """
        Vérifie les deux boucles d'arbitrage possibles.
        Exige des prix bid/ask instantanés (Level 1).
        Retourne un tuple: (Action, Profit_Prévu, Ordres)
        """
        # Boucle 1 : Acheter EURUSD, Acheter USDJPY, Vendre EURJPY
        # Synthétique Ask EURJPY = Ask EURUSD * Ask USDJPY
        synthetic_ask = eurusd_ask * usdjpy_ask
        real_bid = eurjpy_bid
        
        profit_loop_1 = real_bid - synthetic_ask
        
        if profit_loop_1 > self.target_spread:
            logger.critical(f"🌌 [STAT-ARB 3D] Anomalie Boucle 1 détectée ! Profit pur garanti : {profit_loop_1:.5f}")
            orders = [
                {"symbol": "EURUSD", "type": "BUY"},
                {"symbol": "USDJPY", "type": "BUY"},
                {"symbol": "EURJPY", "type": "SELL"}
            ]
            return (1, profit_loop_1, orders)
            
        # Boucle 2 : Vendre EURUSD, Vendre USDJPY, Acheter EURJPY
        # Synthétique Bid EURJPY = Bid EURUSD * Bid USDJPY
        synthetic_bid = eurusd_bid * usdjpy_bid
        real_ask = eurjpy_ask
        
        profit_loop_2 = synthetic_bid - real_ask
        
        if profit_loop_2 > self.target_spread:
            logger.critical(f"🌌 [STAT-ARB 3D] Anomalie Boucle 2 détectée ! Profit pur garanti : {profit_loop_2:.5f}")
            orders = [
                {"symbol": "EURUSD", "type": "SELL"},
                {"symbol": "USDJPY", "type": "SELL"},
                {"symbol": "EURJPY", "type": "BUY"}
            ]
            return (-1, profit_loop_2, orders)
            
        return (0, 0.0, [])
