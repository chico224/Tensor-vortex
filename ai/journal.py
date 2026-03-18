import json
import os
from datetime import datetime
import logging

logger = logging.getLogger("AI_Journal")

class AIJournal:
    """
    Système d'Auto-Apprentissage et de "UX Cognitive".
    Enregistre les détails mathématiques de chaque prise de décision
    pour permettre à un modèle de Machine Learning de s'auto-optimiser.
    """
    
    def __init__(self, log_dir="data"):
        self.log_dir = log_dir
        os.makedirs(self.log_dir, exist_ok=True)
        self.journal_file = os.path.join(self.log_dir, "ai_trading_memory.jsonl")

    def log_trade_context(self, symbol, timeframe, capital, strategies_votes, is_high_leverage):
        """
        Harde les conditions du marché AVANT le trade.
        """
        context = {
            "timestamp": datetime.now().isoformat(),
            "symbol": symbol,
            "timeframe": timeframe,
            "capital": capital,
            "high_leverage_mode": is_high_leverage,
            "strategies_votes": strategies_votes, # ex: {"RSI": 1, "MACD": 1, "Bollinger": 1, ...}
            "trade_id": None,
            "result": None,
            "profit": None
        }
        return context

    def update_trade_result(self, context, trade_id, profit):
        """
        Met à jour le contexte avec le résultat pour créer le set d'entraînement IA.
        """
        context["trade_id"] = trade_id
        context["profit"] = profit
        context["result"] = "WIN" if profit > 0 else "LOSS"
        
        with open(self.journal_file, "a") as f:
            f.write(json.dumps(context) + "\n")
            
        logger.info(f"Expérience IA enregistrée dans le journal cognitif. (Trade {trade_id} - Résultat: {context['result']})")
