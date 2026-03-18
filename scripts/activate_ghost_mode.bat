@echo off
TITLE MT5 Bot Sniper - Ghost Mode Activator
SET BOT_DIR=%~dp0..
SET PYTHON_EXE=python

echo ========================================================
echo MT5 BOT SNIPER - ACTIVATION MODE FANTOME (Elite)
echo ========================================================
echo.
echo Ce script va configurer le bot pour tourner en ARRIERE-PLAN
echo de maniere permanente sur votre ordinateur local.
echo.

:: 1. Création de la tâche planifiée pour lancement au démarrage
echo [*] Configuration de la relance automatique au demarrage...
schtasks /create /tn "MT5_Bot_Sniper" /tr "cmd.exe /c cd /d %BOT_DIR% && set PYTHONPATH=. && start /b python main.py" /sc onlogon /f /rl highest

:: 2. Lancement immédiat en arrière-plan
echo [*] Lancement du bot en mode furtif...
cd /d %BOT_DIR%
set PYTHONPATH=.
start /b python main.py > logs\ghost_output.log 2>&1

echo.
echo ✅ SUCCES : Le bot est maintenant un "Trader de l'Ombre".
echo.
echo [!] Info : Le bot tourne sans fenêtre visible. 
echo [!] Pour voir ce qu'il fait, consultez : logs\bot_execution.log
echo [!] Pour l'arreter : Utilisez le Gestionnaire des taches (processus Python).
echo.
echo ========================================================
pause
