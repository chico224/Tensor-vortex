import os
import sys

# OPTIMISATION RAM EXTREME (2GB) : Brider NumPy et les bibliothèques mathématiques
os.environ["OPENBLAS_NUM_THREADS"] = "1"
os.environ["MKL_NUM_THREADS"] = "1"
os.environ["NUMEXPR_NUM_THREADS"] = "1"
os.environ["OMP_NUM_THREADS"] = "1"

import logging
import time
from bot.headless_manager import UltraLightManager, optimize_system_for_2gb
from bot.connectivity import MT5Connector
from bot.quant_engine import QuantEnsembleEngine
from bot.risk_manager import RiskManager
from bot.executor import OrderExecutor
from bot.orchestrator import GnTechOrchestrator
from dotenv import load_dotenv

# Initialisation du Logging "Silence"
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler("logs/ultra_light.log"),
        logging.StreamHandler()
    ]
logger = logging.getLogger("TensorVortexLauncher")

def main():
    load_dotenv()
    
    # 0. Lecture de la Configuration Utilisateur (SaaS)
    import yaml
    try:
        with open("user_config.yaml", "r") as f:
            config = yaml.safe_load(f)
    except Exception as e:
        logger.error(f"Erreur lecture 'user_config.yaml'. Utilisez le fichier par défaut: {e}")
        return

    # ======== SYSTEME D'AUTO-GUERISON (Immortalité) ========
    # Si on n'est pas déjà géré par le Healer, on lance le superviseur
    if os.getenv("HEALER_MANAGED") != "1":
        from core.auto_healer import ImmortalSupervisord
        healer = ImmortalSupervisord()
        healer.start_immune_system()
        # Le processus parent s'arrête ici et laisse le healer gérer le bot
        try:
            while True: time.sleep(100)
        except KeyboardInterrupt:
            healer.shutdown()
            sys.exit(0)
        return

    node_role = config.get("cluster", {}).get("node_role", "master")

    # 1. Optimisation Système (RAM 2GB)
    optimize_system_for_2gb()
    
    # 2. Lancement de MT5 en mode Invisible (Headless)
    mt5_path = os.getenv("MT5_PATH", config.get("account", {}).get("path", "O/"))
    if not os.path.exists(mt5_path):
        logger.error(f"Erreur : Le chemin MT5 (MT5_PATH dans .env) est introuvable : {mt5_path}")
        return

    manager = UltraLightManager(mt5_path)
    if not manager.launch_headless():
        logger.error("Impossible de lancer le terminal MT5 en mode invisible.")
        return

    # Attente pour l'initialisation du terminal
    logger.info("⚡ TENSOR-VORTEX CORE INITIALISATION...")
    time.sleep(10)

    # 3. Connexion au Compte (Config YAML prioritaire, sinon .env)
    account = config.get("account", {}).get("login")
    password = config.get("account", {}).get("password")
    server = config.get("account", {}).get("server")
    
    if account and password and server:
         os.environ["MT5_ACCOUNT"] = str(account)
         os.environ["MT5_PASSWORD"] = str(password)
         os.environ["MT5_SERVER"] = str(server)
         
    connector = MT5Connector()
    if not connector.connect():
        logger.error("Echec de connexion aux serveurs de trading.")
        return

    # 4. Initialisation Execution & Risque
    risk_manager = RiskManager()
    executor = OrderExecutor(risk_manager)
    
    # ======== MODE WORKER (Execution Seule, 1MB RAM) ========
    if node_role == "worker":
        from core.broadcaster import SignalWorker
        logger.info("🤖 DÉMARRAGE MODE WORKER - TENSOR-VORTEX CLIENT")
        master_ip = config.get("cluster", {}).get("master_ip_address", "tcp://localhost:5555")
        
        def execute_signal(payload):
            symbol = payload["symbol"]
            action = "BUY" if payload["action"] == 1 else "SELL"
            if risk_manager.can_trade(symbol):
                logger.info(f"Signal reçu du Master pour {symbol} -> {action}")
                executor.execute_trade(symbol, payload["action"], payload["price"], 30, 60)

        worker = SignalWorker(master_ip=master_ip, callback=execute_signal)
        worker.start_listening()
        try:
            while True: time.sleep(1)
        except KeyboardInterrupt:
            worker.stop()
            connector.shutdown()
        return

    # ======== MODE MASTER (Cerveau + Diffusion) ========
    logger.info("🧠 DÉMARRAGE TENSOR-VORTEX MASTER (Hyper-Scale Broadcaster)")
    engine = QuantEnsembleEngine()
    from core.broadcaster import SignalBroadcaster
    broadcaster = SignalBroadcaster()
    
    # Interface d'Orchestration (GnTech-Rise Ready)
    from bot.orchestrator import GnTechOrchestrator
    orchestrator = GnTechOrchestrator(engine, risk_manager)
    from bot.omega_bridge import OmegaBridge
    bridge = OmegaBridge(connector) 
    bridge.start_bridge()
    logger.info("Interface d'orchestration Sovereign Tensor-Vortex ACTIVE.")

    # Boucle de Trading Haute Frequence (HFT)
    symbols = config.get("trading_rules", {}).get("trade_markets", ["EURUSD", "XAUUSD", "USDJPY"])
    
    try:
        while True:
            for symbol in symbols:
                # Analyse 100+ Experts + HFT + GPU
                consensus, details = engine.analyze_consensus(symbol)
                
                if consensus != "HOLD":
                    # On vérifie SI l'utilisateur n'est pas bloqué pour Facture Non Payée
                    from bot.billing_manager import SmartBillingSystem
                    billing = SmartBillingSystem()
                    account_active = os.getenv("MT5_ACCOUNT", "UNKNOWN")
                    # Pour la prod, il faudrait lire `last_payment_date` depuis la DB
                    is_suspended, msg = billing.check_suspension_status(account_active, None)
                    
                    if is_suspended:
                        logger.warning(f"⚠️ TRADING SUSPENDU ({account_active}) : {msg}")
                        continue
                        
                    if risk_manager.can_trade(symbol):
                        action_val = 1 if consensus == "BUY" else -1
                        price = mt5.symbol_info_tick(symbol).ask if action_val == 1 else mt5.symbol_info_tick(symbol).bid
                        
                        logger.info(f"🔥 VORTEX SIGNAL ({symbol}): {consensus} | Confiance: {details['confidence']}")
                        broadcaster.broadcast_signal(symbol, action_val, details['confidence'])
                        executor.execute_trade(symbol, action_val, price, 20, 40)
                        
            # ====== GESTION DES RAPPORTS QUOTIDIENS ======
            # (Normalement exécuté par un Scheduler type `cron` ou `schedule`)
            # Pour l'instant on force l'affichage toutes les heures
            current_minute = datetime.now().minute
            if current_minute == 0: 
               from bot.reporting_engine import ReportingEngine
               reporter = ReportingEngine(engine.db)
               # 1. Imprimer dans le Terminal pour l'Admin
               print(reporter.generate_terminal_report("daily", account_active))
               # 2. Sauvegarder le JSON pour le Site Web
               with open("dashboard/public/api_report.json", "w") as jf:
                   jf.write(reporter.generate_web_payload("monthly"))
                   
            time.sleep(10)
            
    except KeyboardInterrupt:
        logger.info("Arret demande par l'utilisateur.")
    finally:
        connector.shutdown()

if __name__ == "__main__":
    main()
