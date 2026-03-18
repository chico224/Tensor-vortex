import logging
import numpy as np

logger = logging.getLogger("SentimentEngine")

class MarketSentiment:
    """
    MOTEUR DE SENTIMENT v1.0 : Analyse de la psychologie des marchés (Cognitive UX).
    Détecte les phases d'accumulation et de distribution avant les explosions de prix.
    """
    
    def __init__(self, symbol):
        self.symbol = symbol
        self.sentiment_score = 0.5 # Neutre au départ

    def analyze(self, df):
        """
        Analyse la psychologie à travers le Price Action et le Volume.
        Retourne un score entre 0 (Peur extrême) et 1 (Cupidité extrême).
        """
        if len(df) < 5: return 0.5
        
        # 1. Analyse de la force des bougies (Marubozu/Doji)
        last_candle = df.iloc[-1]
        body_size = abs(last_candle['close'] - last_candle['open'])
        wick_size = (last_candle['high'] - last_candle['low']) - body_size
        
        # Ratio mèche/corps : Indique l'indécision ou le rejet
        rejection_ratio = wick_size / body_size if body_size > 0 else 1.0
        
        # 2. Convergence Volume/Prix
        vol_change = last_candle['tick_volume'] / df['tick_volume'].tail(5).mean()
        
        if last_candle['close'] > last_candle['open'] and vol_change > 1.5:
            # Pression acheteuse forte
            self.sentiment_score = min(1.0, self.sentiment_score + 0.1)
        elif last_candle['close'] < last_candle['open'] and vol_change > 1.5:
            # Pression vendeuse forte
            self.sentiment_score = max(0.0, self.sentiment_score - 0.1)
        else:
            # Retour progressif au neutre
            self.sentiment_score = 0.5 + (self.sentiment_score - 0.5) * 0.9
            
        return self.sentiment_score

# Innovation : Ce moteur alimente directement le NeuroFilter pour une précision cognitive.
