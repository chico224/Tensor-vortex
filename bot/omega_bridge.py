from flask import Flask, jsonify, request
import threading
import logging
import os
from bot.connectivity import MT5Connector

logger = logging.getLogger("OmegaOrchestrator")

class OmegaBridge:
    """
    Pont d'interopérabilité pour GnTech-Rise & Sovereign Omega AI.
    Permet le pilotage à distance et le monitoring centralisé.
    """
    def __init__(self, bot_instance):
        self.app = Flask("SovereignOmegaBridge")
        self.bot = bot_instance
        self._setup_routes()

    def _setup_routes(self):
        @self.app.route('/status', methods=['GET'])
        def get_status():
            return jsonify({
                "module": "Survivor-Sniper-MT5",
                "orchestrator_linked": "Sovereign Omega AI",
                "status": "active" if self.bot.is_running else "paused",
                "account": os.getenv("MT5_ACCOUNT"),
                "ram_optimization": "Ultra-Low-2GB-Mode"
            })

        @self.app.route('/control', methods=['POST'])
        def control_bot():
            data = request.json
            command = data.get("command")
            if command == "stop":
                self.bot.stop()
                return jsonify({"status": "stopping"})
            elif command == "start":
                self.bot.start()
                return jsonify({"status": "starting"})
            return jsonify({"error": "unknown command"}), 400

    def start_bridge(self):
        # Lancer dans un thread séparé pour ne pas bloquer le bot
        threading.Thread(target=lambda: self.app.run(host='0.0.0.0', port=5000, debug=False, use_reloader=False)).start()
        logger.info("🔗 Sovereign Omega Bridge activé sur le port 5000.")
