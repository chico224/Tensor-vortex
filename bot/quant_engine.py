import logging
from core.gpu_accelerator import math_engine as np
import pandas as pd
from ai.hft_eye import HFTTickEngine
from ai.stat_arb import StatisticalArbitrageTriangular

logger = logging.getLogger("QuantEngine")

class QuantEnsembleEngine:
    """
    Moteur de stratégie quantitatif ultra-rapide (Enterprise Grade).
    Implémente la logique d'Ensemble d'Experts (5 stratégies de base pour normal, 
    100 estimateurs Machine Learning pour haut levier).
    Utilise NumPy et Pandas pour un traitement vectorisé haute fréquence.
    """

    def __init__(self, strategies_md_path=None, db_path="data/trading_bot.db"):
        # Les 5 stratégies fondamentales
        self.core_strategies = ["Momentum_EMA", "MeanReversion_RSI", "Volatility_ATR", "VolumeTrend", "PriceAction"]
        from .experts import ExpertEnsemble
        from .db_manager import DBManager
        self.expert_ensemble = ExpertEnsemble(strategies_md_path)
        self.db = DBManager(db_path)
        
        # OMEGA CORE DEEP TECH
        self.hft_eye = HFTTickEngine()
        self.stat_arb = StatisticalArbitrageTriangular()
        
    def _calculate_indicators(self, df):
        """Calcule vectoriellement tous les indicateurs nécessaires pour les 110 experts."""
        if len(df) < 200: 
            return df
            
        # --- MOVING AVERAGES (SMA, EMA, WMA) ---
        for p in [5, 8, 9, 13, 20, 21, 34, 50, 100, 200]:
            df[f'sma_{p}'] = df['close'].rolling(window=p).mean()
            df[f'ema_{p}'] = df['close'].ewm(span=p, adjust=False).mean()
            # WMA simple via rolling weight
            df[f'wma_{p}'] = df['close'].rolling(window=p).apply(lambda x: np.dot(x, np.arange(1, p+1)) / np.arange(1, p+1).sum(), raw=True)

        # --- RSI (Relative Strength Index) ---
        delta = df['close'].diff()
        for p in [7, 9, 14, 21, 28]:
            gain = (delta.where(delta > 0, 0)).rolling(window=p).mean()
            loss = (-delta.where(delta < 0, 0)).rolling(window=p).mean()
            rs = gain / loss
            df[f'rsi_{p}'] = 100 - (100 / (1 + rs))
            
        # --- BOLLINGER BANDS & Z-SCORE ---
        for p in [20, 50, 100]:
            sma = df[f'sma_{p}']
            std = df['close'].rolling(window=p).std()
            df[f'zscore_{p}'] = (df['close'] - sma) / std
            for s in [2.0, 2.5]:
                df[f'bb_upper_{p}_{s}'] = sma + (std * s)
                df[f'bb_lower_{p}_{s}'] = sma - (std * s)

        # --- MOMENTUM / ROC ---
        for p in [5, 10, 20, 50]:
            df[f'momentum_{p}'] = df['close'] - df['close'].shift(p)
            
        # --- ATR & VOLUME ---
        high_low = df['high'] - df['low']
        high_close = np.abs(df['high'] - df['close'].shift())
        low_close = np.abs(df['low'] - df['close'].shift())
        true_range = pd.concat([high_low, high_close, low_close], axis=1).max(axis=1)
        df['ATR_14'] = true_range.rolling(14).mean()
        
        if 'tick_volume' in df.columns:
            df['volume_sma_20'] = df['tick_volume'].rolling(20).mean()
            df['volume'] = df['tick_volume'] # Shortcut pour les experts
            
        # --- MACD ---
        for fast, slow, sig in [(12, 26, 9), (5, 35, 5)]:
            ema_fast = df['close'].ewm(span=fast, adjust=False).mean()
            ema_slow = df['close'].ewm(span=slow, adjust=False).mean()
            df[f'macd_{fast}_{slow}'] = ema_fast - ema_slow
            df[f'macdsignal_{fast}_{slow}_{sig}'] = df[f'macd_{fast}_{slow}'].ewm(span=sig, adjust=False).mean()
            df[f'macdhist_{fast}_{slow}_{sig}'] = df[f'macd_{fast}_{slow}'] - df[f'macdsignal_{fast}_{slow}_{sig}']

        # --- STOCHASTIC ---
        for k_period, d_period in [(14, 3), (21, 5)]:
            low_min = df['low'].rolling(window=k_period).min()
            high_max = df['high'].rolling(window=k_period).max()
            df[f'stoch_k_{k_period}'] = 100 * ((df['close'] - low_min) / (high_max - low_min + 1e-10))
            df[f'stoch_d_{k_period}_{d_period}'] = df[f'stoch_k_{k_period}'].rolling(window=d_period).mean()

        # --- CCI (Commodity Channel Index) ---
        for p in [14, 20]:
            tp = (df['high'] + df['low'] + df['close']) / 3
            ma = tp.rolling(window=p).mean()
            md = tp.rolling(window=p).apply(lambda x: np.abs(x - x.mean()).mean(), raw=True)
            df[f'cci_{p}'] = (tp - ma) / (0.015 * md + 1e-10)

        # --- ADX / DMI ---
        # Calcul simplifié
        up_move = df['high'] - df['high'].shift(1)
        down_move = df['low'].shift(1) - df['low']
        plus_dm = np.where((up_move > down_move) & (up_move > 0), up_move, 0.0)
        minus_dm = np.where((down_move > up_move) & (down_move > 0), down_move, 0.0)
        
        atr14 = df['ATR_14'] + 1e-10
        plus_di14 = 100 * (pd.Series(plus_dm, index=df.index).rolling(14).mean() / atr14)
        minus_di14 = 100 * (pd.Series(minus_dm, index=df.index).rolling(14).mean() / atr14)
        
        dx = 100 * np.abs(plus_di14 - minus_di14) / (plus_di14 + minus_di14 + 1e-10)
        df['ADX_14'] = dx.rolling(14).mean()
        df['PLUS_DI_14'] = plus_di14
        df['MINUS_DI_14'] = minus_di14

        return df

    def generate_core_signals(self, market_data):
        """
        Génère les signaux pour les 5 stratégies de base.
        market_data: pandas DataFrame issu de MT5 (colonnes: time, open, high, low, close, tick_volume)
        Retourne 1 (Achat), -1 (Vente), ou 0 (Neutre) pour chaque stratégie.
        """
        votes = {strat: 0 for strat in self.core_strategies}
        
        if not isinstance(market_data, pd.DataFrame) or len(market_data) < 25:
            logger.warning("Données de marché insuffisantes pour l'analyse vectorielle.")
            return votes

        # Calcul vectoriel des indicateurs
        df = self._calculate_indicators(market_data.copy())
        
        # Utiliser la dernière bougie fermée (-2, car -1 = en cours)
        current = df.iloc[-2]
        prev = df.iloc[-3]
        
        # Logique Numérique 1 : Momentum (Croisement EMA)
        if current['EMA_9'] > current['EMA_21'] and prev['EMA_9'] <= prev['EMA_21']:
            votes["Momentum_EMA"] = 1
        elif current['EMA_9'] < current['EMA_21'] and prev['EMA_9'] >= prev['EMA_21']:
            votes["Momentum_EMA"] = -1
            
        # Logique Numérique 2 : Mean Reversion (RSI Extreme)
        if current['RSI_14'] < 30:
            votes["MeanReversion_RSI"] = 1
        elif current['RSI_14'] > 70:
            votes["MeanReversion_RSI"] = -1
            
        # Logique Numérique 3 : Volatility Breakout (Price vs ATR)
        if current['close'] > prev['close'] + current['ATR_14'] * 0.5:
            votes["Volatility_ATR"] = 1
        elif current['close'] < prev['close'] - current['ATR_14'] * 0.5:
            votes["Volatility_ATR"] = -1
            
        # Logique Numérique 4 : Volume Trend
        if 'Volume_SMA' in current:
            if current['tick_volume'] > current['Volume_SMA'] and current['close'] > current['open']:
                votes["VolumeTrend"] = 1
            elif current['tick_volume'] > current['Volume_SMA'] and current['close'] < current['open']:
                votes["VolumeTrend"] = -1
                
        # Logique Numérique 5 : Price Action (Engulfing simple)
        body = abs(current['close'] - current['open'])
        prev_body = abs(prev['close'] - prev['open'])
        if current['close'] > current['open'] and prev['close'] < prev['open'] and body > prev_body:
            votes["PriceAction"] = 1
        elif current['close'] < current['open'] and prev['close'] > prev['open'] and body > prev_body:
            votes["PriceAction"] = -1

    def generate_sniper_signals_110(self, market_data):
        """
        Utilise les 110 experts issus du PDF 151 Stratégies.
        """
        indicators = self._prepare_indicators_for_experts(market_data)
        votes = self.expert_ensemble.get_votes(indicators)
        return np.array(votes)

    def _prepare_indicators_for_experts(self, df):
        """Prépare un dictionnaire d'indicateurs complet pour le moteur d'experts."""
        # On s'assure que les indicateurs sont calculés
        df = self._calculate_indicators(df.copy())
        return df.to_dict(orient='list')

    def evaluate_normal_trade(self, market_data):
        """Évalue le niveau d'unanimité des 5 stratégies fondamentales."""
        votes_dict = self.generate_core_signals(market_data)
        votes = list(votes_dict.values())
        
        sum_votes = sum(votes)
        
        # Consensus robuste requis (Au moins 3/5 alignés, aucun avis contraire ne doit annuler l'élan)
        if sum_votes >= 3 and -1 not in votes:
            return 1, votes_dict
        elif sum_votes <= -3 and 1 not in votes:
            return -1, votes_dict
            
        return 0, votes_dict

    def evaluate_high_leverage_trade(self, market_data):
        """Consensus IA pour fort levier (Sniper Mode)."""
        votes_array = self.generate_sniper_signals_110(market_data)
        sum_votes = np.sum(votes_array)
        
        # L'utilisateur veut une unanimité sur 100 stratégies (ici on en a 110)
        threshold = 100 
        consensus_dict = {"sum_votes": int(sum_votes), "confidence": f"{(abs(sum_votes)/110)*100:.1f}%"}
        
        if sum_votes >= threshold:
            return 1, consensus_dict
        elif sum_votes <= -threshold:
            return -1, consensus_dict
            
        return 0, consensus_dict

    def analyze_consensus(self, symbol):
        """
        Analyse finale (Omega Core v3.0). Intègre l'expertise Standard, Sniper (110 experts),
        L'Oeil de Dieu (HFT Tick-by-Tick) et l'Arbitrage Statistique 3D.
        """
        actions = []
        confidences = []
        
        import MetaTrader5 as mt5
        rates = mt5.copy_rates_from_pos(symbol, mt5.TIMEFRAME_M5, 0, 300)
        if rates is None or len(rates) < 200:
             return "HOLD", {"confidence": 0}
             
        df = pd.DataFrame(rates)
        df['time'] = pd.to_datetime(df['time'], unit='s')
        
        # 1. Analyse Technique Pure (Sniper 110 Experts)
        sniper_signal, sniper_details = self.evaluate_high_leverage_trade(df)
        
        # 2. Oeil de Dieu (HFT)
        hft_signal = self.hft_eye.scan_tick_acceleration(symbol)
        
        # Synthèse stricte
        if sniper_signal == 1 and hft_signal >= 0:
            return "BUY", sniper_details
        elif sniper_signal == -1 and hft_signal <= 0:
            return "SELL", sniper_details
            
        return "HOLD", {"confidence": 0}
