import numpy as np
import logging

logger = logging.getLogger("DarkPoolDetector")

class DarkPoolAnomalyDetector:
    """
    DARK POOL ANOMALY DETECTION (La Chasse aux Baleines)
    Analyse 100% Mathématique. 
    Cherche des divergences extrêmes entre la dynamique du Spread et le Tick Volume
    pour débusquer les algorithmes Iceberg (ordres masqués institutionnels).
    """
    
    def __init__(self, baseline_periods=50):
        self.baseline_periods = baseline_periods
        
    def scan_for_whales(self, df):
        """
        df doit contenir: 'tick_volume', 'spread' (optionnel mais recommandé), 'close', 'open'
        """
        if len(df) < self.baseline_periods:
            return 0 # Pas de signal
            
        recent_vol = df['tick_volume'].iloc[-1]
        mean_vol = df['tick_volume'].iloc[-self.baseline_periods:-1].mean()
        std_vol = df['tick_volume'].iloc[-self.baseline_periods:-1].std()
        
        # Z-Score du volume
        vol_zscore = (recent_vol - mean_vol) / std_vol if std_vol > 0 else 0
        
        body_size = abs(df['close'].iloc[-1] - df['open'].iloc[-1])
        mean_body = abs(df['close'] - df['open']).iloc[-self.baseline_periods:-1].mean()
        
        # L'anomalie Iceberg : Volume COLOSSAL mais le prix ne bouge presque pas.
        # Pourquoi ? Car l'institutionnel ABSORBE toute la liquidité avec un ordre limite.
        
        if vol_zscore > 3.0 and body_size < mean_body * 0.5:
            # Un titan est dans le carnet d'ordres.
            
            # Pour déterminer la direction, on regarde si l'absorption s'est faite sur les Ask (Achat) ou Bid (Vente)
            # Sans accès Level II complet, on utilise l'asymétrie des mèches
            wick_up = df['high'].iloc[-1] - max(df['close'].iloc[-1], df['open'].iloc[-1])
            wick_down = min(df['close'].iloc[-1], df['open'].iloc[-1]) - df['low'].iloc[-1]
            
            if wick_down > wick_up * 2:
                # Liquidité absorbée en bas -> Baleine Acheteuse
                logger.warning("[DARK POOL] Absorption massive détectée (Achat).")
                return 1
            elif wick_up > wick_down * 2:
                # Liquidité absorbée en haut -> Baleine Vendeuse
                logger.warning("[DARK POOL] Absorption massive détectée (Vente).")
                return -1
                
        return 0
