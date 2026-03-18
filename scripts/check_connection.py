import sys
import os
# Ajouter le répertoire parent au chemin pour importer le module bot
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from bot.connectivity import MT5Connector
import logging

def main():
    print("=== Diagnostic de Connectivité MT5 Elite ===")
    connector = MT5Connector()
    
    # Tentative d'initialisation
    if connector.initialize():
        print("[SUCCÈS] Connexion établie avec MetaTrader 5.")
        
        # Vérification des ressources VPS
        import psutil
        process = psutil.Process(os.getpid())
        mem_usage = process.memory_info().rss / (1024 * 1024)
        print(f"[INFO] Consommation RAM actuelle : {mem_usage:.2f} Mo")
        
        if mem_usage < 100:
            print("[CONFORMITÉ] Empreinte mémoire conforme aux VPS gratuits.")
        else:
            print("[ALERTE] Empreinte mémoire élevée, optimisation requise.")
            
        connector.shutdown()
    else:
        print("[ÉCHEC] Impossible de se connecter à MT5. Vérifiez vos identifiants dans .env")

if __name__ == "__main__":
    main()
