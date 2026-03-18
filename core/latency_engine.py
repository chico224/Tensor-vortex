import MetaTrader5 as mt5
import time
import numpy as np
import logging

logger = logging.getLogger("PreEmptiveLatency")

class LatencyEngine:
    """
    PRE-EMPTIVE LATENCY ENGINE (HFT Silicon Valley Standard).
    Calcule la dérivée mathématique du Ping vers le serveur Broker.
    Permet au QuantEngine de tirer l'ordre AVANT l'instant limite 
    en prédisant le lag réseau.
    """
    
    def __init__(self, history_size=20):
        self.history_size = history_size
        self.ping_history = []
        self.last_deriv = 0.0
        
    def measure_ping(self):
        """Mesure instantanée du ping (ms)."""
        info = mt5.terminal_info()
        if info:
            ping_ms = info.ping_last / 1000.0  # en ms
            self._update_history(ping_ms)
            return ping_ms
        return 50.0 # defaut
        
    def _update_history(self, ping):
        self.ping_history.append(ping)
        if len(self.ping_history) > self.history_size:
            self.ping_history.pop(0)
            
    def calculate_preemptive_offset(self):
        """
        Calcule de combien de millisecondes le bot doit anticiper le trade.
        Utilise la dérivée première de l'historique de ping pour deviner
        si la latence est en train de s'empirer ou s'améliorer.
        """
        if len(self.ping_history) < 3:
            return 0.0 # pas assez de data
            
        # Dérivée première via numpy gradient
        arr = np.array(self.ping_history)
        gradient = np.gradient(arr)
        
        # La dérivée moyenne récente
        recent_accel = np.mean(gradient[-3:]) 
        
        # Ping actuel + l'accélération prévue (pour le prochain instant t+1)
        predicted_ping = arr[-1] + recent_accel
        
        # On ne permet pas des valeurs négatives ou folles
        predicted_ping = max(5.0, min(predicted_ping, 500.0))
        
        logger.debug(f"[HFT] Ping prédictif calculé: {predicted_ping:.2f}ms. (Offset pour Front-Running)")
        return predicted_ping
        
    def wait_for_strike(self, target_timestamp, offset_ms=None):
        """
        Bloque jusqu'au moment PARFAIT de l'exécution, en soustrayant
        la latence réseau prédite pour atterrir EXACTEMENT à target_timestamp.
        """
        if offset_ms is None:
            offset_ms = self.calculate_preemptive_offset()
            
        # Convert ms to seconds
        offset_sec = offset_ms / 1000.0
        
        # Le *vrai* target interne de tir
        strike_time = target_timestamp - offset_sec
        
        now = time.time()
        if strike_time > now:
            sleep_duration = strike_time - now
            if sleep_duration > 0:
                time.sleep(sleep_duration)
        
        return offset_ms # retourne l'avantage gagné
