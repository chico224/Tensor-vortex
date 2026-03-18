import zmq
import json
import logging
import threading
import time

logger = logging.getLogger("OmegaBroadcaster")

class SignalBroadcaster:
    """
    Architecture "One-to-Million" (Silicon Valley Scale).
    Ce module agit comme le Cerveau Central (Master).
    Il publie les signaux de trading instantanément via ZeroMQ (PUB/SUB)
    vers des millions d'instances "Worker" (les comptes clients).
    """
    def __init__(self, port="5555"):
        self.context = zmq.Context()
        self.socket = self.context.socket(zmq.PUB)
        
        # Binding sur toutes les interfaces pour accepter les connexions externes (VPS)
        self.bind_address = f"tcp://*:{port}"
        try:
            self.socket.bind(self.bind_address)
            logger.info(f"🚀 OMEGA BROADCASTER ACTIF sur {self.bind_address}")
            logger.info("En attente de connexion des millions de Workers...")
        except Exception as e:
            logger.error(f"Erreur d'initialisation du Broadcaster : {e}")

    def broadcast_signal(self, symbol, action, confidence, metadata=None):
        """
        Diffuse un signal pur à la vitesse de la lumière.
        action: 1 (Achat) ou -1 (Vente)
        """
        if metadata is None:
            metadata = {}
            
        payload = {
            "timestamp": time.time(),
            "symbol": symbol,
            "action": action,
            "confidence": confidence,
            "metadata": metadata
        }
        
        # Topic par défaut = 'TRADES'
        topic = "TRADES"
        message = f"{topic} {json.dumps(payload)}"
        
        try:
            self.socket.send_string(message)
            logger.info(f"📡 SIGNAL DIFFUSÉ [{symbol} -> {action}] à l'échelle globale.")
        except Exception as e:
            logger.error(f"Échec de diffusion du signal : {e}")

class SignalWorker:
    """
    Client ultra-léger (1MB RAM) qui écoute le Broadcaster.
    Idéal pour les petits VPS ou les comptes clients distribués.
    """
    def __init__(self, master_ip="tcp://localhost:5555", callback=None):
        self.context = zmq.Context()
        self.socket = self.context.socket(zmq.SUB)
        self.socket.connect(master_ip)
        
        # S'abonne uniquement aux messages de type 'TRADES'
        self.socket.setsockopt_string(zmq.SUBSCRIBE, "TRADES")
        self.callback = callback
        self.is_running = False
        logger.info(f"🔌 WORKER CONNECTÉ au Cerveau Central ({master_ip})")

    def start_listening(self):
        self.is_running = True
        threading.Thread(target=self._listen_loop, daemon=True).start()

    def _listen_loop(self):
        while self.is_running:
            try:
                # Réception Non-Bloquante ou avec Timeout
                message = self.socket.recv_string()
                topic, json_data = message.split(" ", 1)
                payload = json.loads(json_data)
                
                logger.debug(f"Signal reçu : {payload}")
                if self.callback:
                    self.callback(payload)
                    
            except zmq.ZMQError:
                pass # Timeout ou erreur de connexion
            except Exception as e:
                logger.error(f"Erreur dans la boucle Worker : {e}")
                
    def stop(self):
        self.is_running = False
        self.socket.close()
        self.context.term()
