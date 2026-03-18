import re
import logging
from .experts import ExpertEnsemble

logger = logging.getLogger("StrategyParser")

class StrategyParser:
    """
    Analyse le fichier 151_strategies_extracted.md pour injecter les paramètres
    dans les experts du bot.
    """
    
    def __init__(self, file_path):
        self.file_path = file_path
        self.strategies_found = []

    def parse_strategies(self):
        """Extrait les noms et sections des stratégies."""
        try:
            with open(self.file_path, 'r', encoding='utf-8') as f:
                content = f.read()
                
            # Regex pour capturer les titres de stratégie (ex: 3.12 Strategy: Moving averages)
            pattern = r"(\d+\.\d+)\s+Strategy:\s+([^\n\r]+)"
            matches = re.finditer(pattern, content)
            
            for match in matches:
                self.strategies_found.append({
                    "id": match.group(1),
                    "name": match.group(2).strip(),
                    "position": match.start()
                })
                
            logger.info(f"Analyse terminée : {len(self.strategies_found)} stratégies détectées.")
            return self.strategies_found
            
        except Exception as e:
            logger.error(f"Erreur lors du parsing du fichier MD : {e}")
            return []

    def get_strategy_logic(self, strategy_id):
        """Récupère le texte complet d'une stratégie spécifique pour analyse par l'IA."""
        # Utile pour l'auto-optimisation IA future
        pass
