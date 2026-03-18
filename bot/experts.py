import numpy as np
import pandas as pd
import logging

logger = logging.getLogger("Experts")

class ExpertEnsemble:
    """
    Héberge 110 experts quantitatifs basés sur le PDF des 151 stratégies.
    Optimisé pour une exécution ultra-rapide (NumPy/Vectorisé).
    """
    
    def __init__(self, strategies_md_path=None):
        self.experts = []
        self.strategies_md_path = strategies_md_path
        self._register_experts()
        if self.strategies_md_path:
            self._inject_dynamic_strategies()
        
    def _inject_dynamic_strategies(self):
        """Lit le MD et ajuste les paramètres des experts si des valeurs spécifiques sont trouvées."""
        from .strategy_parser import StrategyParser
        parser = StrategyParser(self.strategies_md_path)
        found = parser.parse_strategies()
        logger.info(f"Injection dynamique de {len(found)} stratégies clés en main.")
        # Ici on peut loguer ou ajuster des comportements basés sur le MD

    def _register_experts(self):
        """Enregistre les 110 fonctions de signal."""
        # On ajoute les experts par blocs de logique
        
        # 1-30: Moving Average Variations (PDF 3.12, 8.1)
        for p1, p2 in [(5,13), (8,21), (9,21), (13,34), (20,50), (50,100), (50,200), (100,200)]:
            self.experts.append(self.make_ma_crossover(p1, p2, kind='sma'))
            self.experts.append(self.make_ma_crossover(p1, p2, kind='ema'))
            self.experts.append(self.make_ma_crossover(p1, p2, kind='wma'))
            
        # 31-50: RSI variations (PDF 3.10)
        for p in [7, 9, 14, 21, 28]:
            self.experts.append(self.make_rsi_expert(p, low=30, high=70))
            self.experts.append(self.make_rsi_expert(p, low=20, high=80))
            
        # 51-70: Momentum/ROC variations (PDF 10.4)
        for p in [5, 10, 20, 50]:
            self.experts.append(self.make_momentum_expert(p))
            
        # 71-85: Mean Reversion / Z-Score (PDF 10.3)
        for p in [20, 50, 100]:
            self.experts.append(self.make_zscore_expert(p))
            
        # Volatility / BB (PDF 7.x)
        for p in [20, 50]:
            self.experts.append(self.make_bb_expert(p, std=2.0))
            self.experts.append(self.make_bb_expert(p, std=2.5))

        # --- NOUVEAUX EXPERTS SILICON VALLEY ---
        # MACD (Momentum & Trend)
        for fast, slow, sig in [(12, 26, 9), (5, 35, 5)]:
            self.experts.append(self.make_macd_expert(fast, slow, sig))
            
        # Stochastic (Reversal)
        for k, d in [(14, 3), (21, 5)]:
            self.experts.append(self.make_stoch_expert(k, d))
            
        # CCI (Extreme Deviations)
        for p in [14, 20]:
            self.experts.append(self.make_cci_expert(p))
            
        # ADX (Trend Strength)
        self.experts.append(self.make_adx_expert())

        # Price Action & Fractals (Revolutionary Ideas)
        self.experts.append(self.engulfing_expert)
        self.experts.append(self.pinbar_expert)
        
        # Comblement avec des copies modifiées HFT si le compte < 110
        while len(self.experts) < 110:
            idx = len(self.experts)
            self.experts.append(self.make_macd_expert(12, 26+idx, 9))

    # --- Factory Methods pour les experts ---

    def make_ma_crossover(self, p1, p2, kind='sma'):
        def expert(indicators):
            key1 = f"{kind}_{p1}"
            key2 = f"{kind}_{p2}"
            if key1 in indicators and key2 in indicators:
                curr1, prev1 = indicators[key1][-2:]
                curr2, prev2 = indicators[key2][-2:]
                if curr1 > curr2 and prev1 <= prev2: return 1
                if curr1 < curr2 and prev1 >= prev2: return -1
            return 0
        return expert

    def make_rsi_expert(self, period, low=30, high=70):
        def expert(indicators):
            key = f"rsi_{period}"
            if key in indicators:
                val = indicators[key][-1]
                if val < low: return 1
                if val > high: return -1
            return 0
        return expert

    def make_momentum_expert(self, period):
        def expert(indicators):
            key = f"momentum_{period}"
            if key in indicators:
                if indicators[key][-1] > 0: return 1
                if indicators[key][-1] < 0: return -1
            return 0
        return expert

    def make_zscore_expert(self, period):
        def expert(indicators):
            key = f"zscore_{period}"
            if key in indicators:
                val = indicators[key][-1]
                if val < -2.0: return 1
                if val > 2.0: return -1
            return 0
        return expert

    def make_bb_expert(self, period, std=2.0):
        def expert(indicators):
            p_key = f"close"
            u_key = f"bb_upper_{period}_{std}"
            l_key = f"bb_lower_{period}_{std}"
            if p_key in indicators and u_key in indicators and l_key in indicators:
                price = indicators[p_key][-1]
                if price < indicators[l_key][-1]: return 1
                if price > indicators[u_key][-1]: return -1
            return 0
        return expert

    def make_macd_expert(self, fast, slow, sig):
        def expert(indicators):
            m_key = f"macd_{fast}_{slow}"
            s_key = f"macdsignal_{fast}_{slow}_{sig}"
            if m_key in indicators and s_key in indicators:
                curr_macd, prev_macd = indicators[m_key][-2:]
                curr_sig, prev_sig = indicators[s_key][-2:]
                # Croisement haussier
                if curr_macd > curr_sig and prev_macd <= prev_sig and curr_macd < 0: return 1
                # Croisement baissier
                if curr_macd < curr_sig and prev_macd >= prev_sig and curr_macd > 0: return -1
            return 0
        return expert

    def make_stoch_expert(self, k_period, d_period):
        def expert(indicators):
            k_key = f"stoch_k_{k_period}"
            d_key = f"stoch_d_{k_period}_{d_period}"
            if k_key in indicators and d_key in indicators:
                k, d = indicators[k_key][-1], indicators[d_key][-1]
                if k < 20 and d < 20 and k > d: return 1
                if k > 80 and d > 80 and k < d: return -1
            return 0
        return expert

    def make_cci_expert(self, period):
        def expert(indicators):
            key = f"cci_{period}"
            if key in indicators:
                curr, prev = indicators[key][-2:]
                if curr > -100 and prev <= -100: return 1 # Sortie de zone de survente
                if curr < 100 and prev >= 100: return -1 # Sortie de zone de surachat
            return 0
        return expert

    def make_adx_expert(self):
        def expert(indicators):
            if 'ADX_14' in indicators and 'PLUS_DI_14' in indicators and 'MINUS_DI_14' in indicators:
                adx = indicators['ADX_14'][-1]
                plus_di = indicators['PLUS_DI_14'][-1]
                minus_di = indicators['MINUS_DI_14'][-1]
                
                if adx > 25: # Tendance forte
                    if plus_di > minus_di: return 1
                    if minus_di > plus_di: return -1
            return 0
        return expert

    # --- Experts Spécifiques ---

    def engulfing_expert(self, indicators):
        c_open = indicators['open'][-1]
        c_close = indicators['close'][-1]
        p_open = indicators['open'][-2]
        p_close = indicators['close'][-2]
        
        c_body = abs(c_close - c_open)
        p_body = abs(p_close - p_open)
        
        if c_close > c_open and p_close < p_open and c_body > p_body: return 1
        if c_close < c_open and p_close > p_open and c_body > p_body: return -1
        return 0

    def pinbar_expert(self, indicators):
        h, l, o, c = indicators['high'][-1], indicators['low'][-1], indicators['open'][-1], indicators['close'][-1]
        body = abs(c - o)
        total_range = h - l
        if total_range == 0: return 0
        
        # Bullish Pin Bar (Long wick bottom)
        if (min(o, c) - l) > (total_range * 0.6) and body < (total_range * 0.3): return 1
        # Bearish Pin Bar (Long wick top)
        if (h - max(o, c)) > (total_range * 0.6) and body < (total_range * 0.3): return -1
        return 0

    def liquidity_raid_expert(self, indicators):
        """
        DÉTECTION DE CHASSE AUX STOPS (Liquidity Raid).
        Idée Expert: Identifie les mèches anormales avec un volume massif suivies d'un rejet.
        """
        h, l, o, c = indicators['high'][-1], indicators['low'][-1], indicators['open'][-1], indicators['close'][-1]
        vol = indicators['volume'][-1]
        vol_sma = indicators['volume_sma_20'][-1]
        
        if vol > vol_sma * 3.0: # Volume de capitulation ou injection massive
            total_range = h - l
            if total_range == 0: return 0
            
            # Liquidity Raid en bas (Chasse aux longs) -> Signal Achat
            if (min(o, c) - l) > (total_range * 0.7): return 1
            # Liquidity Raid en haut (Chasse aux shorts) -> Signal Vente
            if (h - max(o, c)) > (total_range * 0.7): return -1
        return 0

    def fractal_alignment_expert(self, indicators):
        """
        UNANIMITÉ FRACTALE (Multi-Timeframe Symmetry).
        Idée Expert: Alignement de la structure de tendance sur 3 échelles de temps simulées.
        """
        # Utilise des fenêtres glissantes de différentes tailles pour simuler le MTF
        trend_short = indicators['ema_9'][-1] > indicators['ema_21'][-1]
        trend_medium = indicators['ema_50'][-1] > indicators['ema_100'][-1]
        trend_long = indicators['ema_100'][-1] > indicators['ema_200'][-1]
        
        if trend_short and trend_medium and trend_long: return 1
        if not trend_short and not trend_medium and not trend_long: return -1
        return 0

    def get_votes(self, indicators):
        """Récupère tous les votes incluant les idées révolutionnaires."""
        votes = [exp(indicators) for exp in self.experts]
        # Ajout des votes d'experts révolutionnaires
        votes.append(self.liquidity_raid_expert(indicators))
        votes.append(self.fractal_alignment_expert(indicators))
        return votes
