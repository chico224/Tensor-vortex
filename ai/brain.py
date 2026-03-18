import logging
import json
import os
import pandas as pd
from datetime import datetime

logger = logging.getLogger("SurvivorBrain")

class SurvivorBrain:
    """
    Module d'Auto-Correction IA (Enterprise Grade).
    Analyse les échecs récents pour ajuster le comportement du bot.
    Implémente le Kill-Switch "3-Strikes".
    """
    
    def __init__(self, db_manager):
        self.db = db_manager
        self.consecutive_losses = 0
        self.is_halted = False
        self.last_analysis_time = None
        
    def check_survival_status(self):
        """Vérifie si le bot doit s'arrêter selon la règle des 3-Strikes."""
        if self.consecutive_losses >= 3:
            if not self.is_halted:
                logger.critical("🚨 RÈGLE DES 3-STRIKES ACTIVÉE : Arrêt d'urgence du trading réel.")
                self.is_halted = True
                self._run_cognitive_analysis()
        return not self.is_halted

    def update_results(self, profit):
        """Met à jour le compteur de survie après chaque trade."""
        if profit < 0:
            self.consecutive_losses += 1
            logger.warning(f"⚠️ Perte détectée. Compteur 3-Strikes: {self.consecutive_losses}/3")
        else:
            if self.consecutive_losses > 0:
                logger.info("✅ Profit détecté. Réinitialisation du compteur 3-Strikes.")
            self.consecutive_losses = 0
            self.is_halted = False

    def _run_cognitive_analysis(self):
        """
        Analyse les 10 derniers trades pour identifier la cause de l'échec.
        Idée Expert: Recherche de corrélations entre les pertes et la volatilité/session.
        """
        logger.info("🧠 Lancement de l'Analyse Cognitive IA...")
        
        # Récupération des données depuis SQLite via db_manager
        # (Simulé ici, sera étendu avec l'historique réel)
        self.last_analysis_time = datetime.now()
        
        # Logique d'auto-optimisation : 
        # Si les pertes surviennent par haute volatilité, on peut suggérer d'augmenter le seuil d'unanimité.
        logger.info("💡 Suggestion IA : Réduction temporaire de l'exposition sur XAUUSD possible.")

    def reset_survivor(self):
        """Réinitialise manuellement le bot après correction."""
        self.consecutive_losses = 0
        self.is_halted = False
        logger.info("♻️ Système Survivor réinitialisé.")
