import MetaTrader5 as mt5
import os
from dotenv import load_dotenv

load_dotenv()
path = os.getenv("MT5_PATH")

print(f"Tentative d'initialisation avec le chemin : {path}")

# On remplace les / par des \ pour Windows si nécessaire
if path:
    path = path.replace("/", "\\")

if not mt5.initialize(path=path):
    print(f"❌ Échec de l'initialisation. Code erreur : {mt5.last_error()}")
else:
    print("✅ Succès de l'initialisation !")
    print(f"Info Terminal : {mt5.terminal_info()}")
    mt5.shutdown()
