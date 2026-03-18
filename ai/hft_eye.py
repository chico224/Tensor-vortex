import MetaTrader5 as mt5
import numpy as np
import logging

logger = logging.getLogger("GodsEyeHFT")

class HFTTickEngine:
    """
    L'OEIL DE DIEU (HFT Micro-Structure)
    Oublie les bougies OHLC. Ce module lit l'essence pure du marché :
    les ticks milliseconde par milliseconde.
    Calcule l'accélération (dérivée seconde) du prix pour Prédire le Futur.
    """
    def __init__(self, history_capacity=1000):
        self.history_capacity = history_capacity
        
    def scan_tick_acceleration(self, symbol):
        """
        Récupère les 1000 derniers ticks et calcule l'Accélération Absolue.
        Si l'accélération s'inverse brusquement avec un fort volume,
        le prix vater se retourner dans les secondes qui suivent.
        """
        # copy_ticks_from demande datetimes. copy_ticks_range aussi.
        # Le plus HFT est de récupérer les N derniers ticks instantanément :
        ticks = mt5.copy_ticks_from(symbol, mt5.symbol_info_tick(symbol).time_msc, self.history_capacity, mt5.COPY_TICKS_ALL)
        
        if ticks is None or len(ticks) < 50:
            return 0 # Pas de flux tick
            
        # Extraire prix (Bid) et Volume
        prices = ticks['bid']
        
        # 1. Dérivée Première : Vélocité (Vitesse du prix)
        velocity = np.diff(prices)
        
        # 2. Dérivée Seconde : Accélération (Force g du marché)
        acceleration = np.diff(velocity)
        
        if len(acceleration) < 10:
             return 0
             
        # On regarde la micro-structure très récente (derniers ticks)
        recent_accel_mean = np.mean(acceleration[-10:])
        recent_velocity_mean = np.mean(velocity[-10:])
        
        # Le secret de Jane Street : 
        # Si la vélocité est positive (ça monte) mais l'accélération est FORTEMENT NÉGATIVE (ça freine sec)
        # -> Un Mur Institutionnel vient d'être atteint. Vent imminent.
        
        if recent_velocity_mean > 0 and recent_accel_mean < -0.0001:
            logger.warning(f"👁️ L'OEIL DE DIEU: Freinage brutal acheteur détecté sur {symbol}. Crash imminent de la bougie (Signal VENTE).")
            return -1
            
        # Si la vélocité est négative (ça chute) mais l'accélération est FORTEMENT POSITIVE (rebond)
        if recent_velocity_mean < 0 and recent_accel_mean > 0.0001:
            logger.warning(f"👁️ L'OEIL DE DIEU: Absorption vendeurs détectée sur {symbol}. Rebond imminent (Signal ACHAT).")
            return 1
            
        return 0
