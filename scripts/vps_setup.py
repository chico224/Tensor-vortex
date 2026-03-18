import os
import subprocess
import sys

def setup():
    print("🛠️ Configuration du VPS MT5 Bot...")
    
    # 1. Création des dossiers nécessaires
    folders = ["logs", "data", "strategies_input"]
    for folder in folders:
        if not os.path.exists(folder):
            os.makedirs(folder)
            print(f"✅ Dossier créé : {folder}")
            
    # 2. Vérification du fichier .env
    if not os.path.exists(".env"):
        print("⚠️ Attention : Fichier .env manquant. Veuillez le créer à partir du README.")
    
    # 3. Vérification des dépendances
    print("📦 Vérification des dépendances...")
    try:
        subprocess.check_call([sys.executable, "-m", "pip", "install", "-r", "requirements.txt"])
        print("✅ Dépendances installées.")
    except Exception as e:
        print(f"❌ Erreur lors de l'installation des dépendances : {e}")

    print("\n🚀 Configuration terminée. Vous pouvez lancer le bot avec 'python main.py'")

if __name__ == "__main__":
    setup()
