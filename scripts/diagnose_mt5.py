import MetaTrader5 as mt5
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("MT5_Diag")

def diagnose_mt5():
    print("--- Diagnostic Connexion MT5 (Expert 50 Ans) ---")
    
    # Tentative d'initialisation
    if not mt5.initialize():
        print(f"❌ ÉCHEC : Impossible d'initialiser MetaTrader5.")
        print(f"Code Erreur : {mt5.last_error()}")
        print("\nCONSEILS :")
        print("1. Ouvrez manuellement votre terminal MetaTrader 5.")
        print("2. Vérifiez que 'Autoriser l'importation de DLL' est coché dans Options > Experts Advisors.")
        return False
        
    print("✅ SUCCESS : Terminal MT5 détecté.")
    terminal_info = mt5.terminal_info()
    if terminal_info:
        print(f"Version : {terminal_info.version}")
        print(f"Serveur : {terminal_info.server}")
        print(f"Connecté : {terminal_info.connected}")
    
    mt5.shutdown()
    return True

if __name__ == "__main__":
    diagnose_mt5()
