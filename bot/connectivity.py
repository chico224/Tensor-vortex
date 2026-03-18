import MetaTrader5 as mt5
import os
import time
import logging
from dotenv import load_dotenv

# Configuration du logging de niveau entreprise
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler("bot_activity.log"),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger("MT5_Connectivity")

class MT5Connector:
    """
    Expertise 50 ans : Gestionnaire de connexion robuste avec Hardening Natif.
    Assure une liaison stable entre le bot quantitatif et le terminal MT5.
    """
    
    def __init__(self):
        load_dotenv()
        account_raw = os.getenv("MT5_ACCOUNT", "0")
        try:
            self.account = int(account_raw)
        except ValueError:
            logger.warning(f"⚠️ 'MT5_ACCOUNT' ({account_raw}) n'est pas un nombre. Tentative de connexion sans login explicite.")
            self.account = 0
            
        self.password = os.getenv("MT5_PASSWORD", "")
        self.server = os.getenv("MT5_SERVER", "")
        self.is_connected = False

    def connect(self):
        """Initialisation durcie de la connexion."""
        # Tentative 1 : Terminal déjà ouvert
        if mt5.initialize():
            logger.info("Terminal MT5 detecte et initialise.")
            return self._login()
            
        # Tentative 2 : Utilisation du chemin spécifié dans .env
        path = os.getenv("MT5_PATH")
        if path and mt5.initialize(path=path):
            logger.info(f"Terminal MT5 demarre via le chemin: {path}")
            return self._login()
            
        logger.error(f"Echec critique de l'initialisation MT5. Assurez-vous que le terminal est OUVERT. Erreur: {mt5.last_error()}")
        return False

    def _login(self):
        """Tentative de connexion au compte de trading."""
        if self.account == 0:
            logger.warning("Aucun compte specifie ou login non-numerique. Utilisation du compte terminal actuel.")
            self.is_connected = True
            return True
        return self.login_with_credentials()

    def login_with_credentials(self):
        """Tentative de connexion au compte de trading."""
        authorized = mt5.login(self.account, password=self.password, server=self.server)
        
        if authorized:
            logger.info(f"Connecte au compte {self.account} ({self.server})")
            self.is_connected = True
            return True
        else:
            logger.error(f"Echec de la connexion au compte {self.account}. Erreur: {mt5.last_error()}")
            return False

    def check_connection(self):
        """Heartbeat : vérifie si la connexion est toujours active."""
        terminal_info = mt5.terminal_info()
        if terminal_info is None:
            logger.warning("Connexion perdue avec le terminal MT5.")
            self.is_connected = False
            return False
        
        if not terminal_info.connected:
            logger.warning("Terminal MT5 déconnecté du serveur de trading.")
            self.is_connected = False
            return False
            
        return True

    def shutdown(self):
        """Fermeture propre des ressources pour éviter les fuites mémoire sur VPS."""
        mt5.shutdown()
        logger.info("Connexion MT5 fermée proprement.")

if __name__ == "__main__":
    # Test unitaire rapide
    connector = MT5Connector()
    if connector.initialize():
        print("Structure de base opérationnelle.")
        connector.shutdown()
