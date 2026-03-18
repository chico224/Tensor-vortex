import os
import subprocess
import time
import logging
import MetaTrader5 as mt5
from bot.connectivity import MT5Connector

logger = logging.getLogger("UltraLight")

class UltraLightManager:
    """
    Expertise 50 ans : Gestionnaire de ressources pour environnements contraints (2GB RAM).
    Optimise le terminal MT5 pour une consommation proche de zero.
    """
    
    def __init__(self, mt5_path):
        self.mt5_path = mt5_path
        # Stockage local de la config pour eviter les erreurs de permission
        self.config_path = os.path.abspath(os.path.join(os.getcwd(), "data", "min_config.ini"))
        os.makedirs(os.path.dirname(self.config_path), exist_ok=True)
        self._create_minimal_config()

    def _create_minimal_config(self):
        """Crée un fichier de configuration MT5 qui désactive TOUT le visuel."""
        config_content = """[Common]
Login=0
ProxyEnable=0
CertConfirm=0
NewsEnable=0
SoundEnable=0
[Charts]
MaxBars=1000
PrintColor=0
[Experts]
AllowLiveTrading=1
AllowDllImport=1
"""
        with open(self.config_path, "w") as f:
            f.write(config_content)
        logger.info(f"Configuration minimale creee : {self.config_path}")

    def launch_headless(self):
        """Lance MT5 en mode totalement invisible (SW_HIDE)."""
        try:
            # Expertise 50 ans : Utilisation des flags Windows pour une invisibilité totale
            startupinfo = subprocess.STARTUPINFO()
            startupinfo.dwFlags |= subprocess.STARTF_USESHOWWINDOW
            startupinfo.wShowWindow = 0 # SW_HIDE

            cmd = [self.mt5_path, f"/config:{self.config_path}", "/inc"]
            subprocess.Popen(
                cmd, 
                startupinfo=startupinfo,
                creationflags=subprocess.DETACHED_PROCESS | subprocess.CREATE_NEW_PROCESS_GROUP
            )
            logger.info("Terminal MT5 lance en mode 100% INVISIBLE.")
            return True
        except Exception as e:
            logger.error(f"Erreur lors du lancement headless : {e}")
            return False

def optimize_system_for_2gb():
    """Script de hardening pour liberer la RAM Windows."""
    # Cette partie necessite des droits admin, on va juste logger les conseils 
    # ou tenter des optimisations de process priority.
    logger.info("Optimisation du processus Python pour priorité HAUTE.")
    try:
        import psutil
        p = psutil.Process(os.getpid())
        p.nice(psutil.HIGH_PRIORITY_CLASS)
    except Exception:
        pass

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    print("Pre-requis pour 2GB RAM pret.")
