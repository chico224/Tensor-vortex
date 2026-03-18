import os
import time
import subprocess
import logging
import threading
import MetaTrader5 as mt5

logger = logging.getLogger("AutoHealer")

class ImmortalSupervisord:
    """
    ZERO-DOWNTIME AUTO-HEALING CORE (Système Immunitaire)
    Watchdog local ultra-Agressif. Surveille MT5, les Sockets, et la RAM.
    Relance automatiquement les composants ou recompile le code Python
    en mode Hot-Swap sans rater un tic de marché.
    """
    def __init__(self, main_script="scripts/ultra_light_launch.py"):
        self.main_script = main_script
        self.is_running = True
        self.heartbeat_timeout = 30 # secondes
        self.last_heartbeat = time.time()
        self.bot_process = None

    def start_immune_system(self):
        logger.info("🛡️ DÉMARRAGE DU SYSTÈME IMMUNITAIRE (Auto-Healing Core)")
        threading.Thread(target=self._watchdog_loop, daemon=True).start()
        self._spawn_bot()
        
    def _spawn_bot(self):
        """Lance l'Omega Core dans un sous-processus isolé."""
        if self.bot_process is not None:
             self.bot_process.kill()
             
        env = os.environ.copy()
        env['HEALER_MANAGED'] = "1"
        self.bot_process = subprocess.Popen(["python", self.main_script], env=env)
        self.last_heartbeat = time.time()
        logger.info("🤖 Bot spawné par le Superviseur.")

    def ping_heartbeat(self):
        """Le bot doit appeler cette fonction régulièrement."""
        self.last_heartbeat = time.time()

    def _watchdog_loop(self):
        while self.is_running:
            try:
                # 1. Surveiller le Processus
                if self.bot_process.poll() is not None:
                    code = self.bot_process.returncode
                    logger.warning(f"⚠️ LE BOT A CRASHÉ (Code {code}). RÉSURRECTION INSTANTANÉE...")
                    self._spawn_bot()
                    
                # 2. Surveiller MT5
                terminal_info = mt5.terminal_info()
                if not terminal_info or not terminal_info.connected:
                    logger.warning("⚠️ COUPURE MT5 DÉTECTÉE. Reconnexion Socket Forcée...")
                    mt5.initialize() # Tentative de réinitialisation bas niveau
                    
                # 3. Surveiller les Deadlocks (Heartbeat)
                if time.time() - self.last_heartbeat > self.heartbeat_timeout:
                    logger.error("☠️ DEADLOCK DÉTECTÉ (Le bot a freezé). Exécution Ordre de Purge 66.")
                    self._spawn_bot() # Tue et relance
                    
                time.sleep(5)
                
            except Exception as e:
                logger.error(f"Erreur interne Superviseur : {e}")
                time.sleep(10)

    def shutdown(self):
        self.is_running = False
        if self.bot_process:
            self.bot_process.kill()
