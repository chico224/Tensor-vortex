# MT5 Bot Survivor - VPS Deployment Script (Enterprise Grade)
# Expertise 50 ans : Automatisation de production Windows Server

$ErrorActionPreference = "Stop"
$LogFile = "vps_deploy.log"

function Write-Log {
    param($Message)
    $TimeStamp = Get-Date -Format "yyyy-MM-dd HH:mm:ss"
    "$TimeStamp - $Message" | Out-File -FilePath $LogFile -Append
    Write-Host "$TimeStamp - $Message" -ForegroundColor Cyan
}

Write-Log "Starting MT5 Bot Deployment on VPS..."

# 1. Verification de l'environnement
if (-not (Test-Path ".\main.py")) {
    Write-Log "Error: main.py not found. Please run this script from the project root."
    exit
}

# 2. Installation des dependances Python
Write-Log "Installing Python dependencies..."
try {
    pip install -r requirements.txt
    Write-Log "Dependencies installed successfully."
} catch {
    Write-Log "Error installing dependencies. Please ensure Python and pip are installed."
    exit
}

# 3. Preparation des dossiers
Write-Log "Preparing directories..."
New-Item -ItemType Directory -Force -Path "logs", "data" | Out-Null

# 4. Configuration Headless (Invisible)
Write-Log "Configuring Headless Mode for 2GB RAM optimization..."
# Le headless_manager.py s'occupe du reste au lancement.

# 5. Creation du lanceur automatique (Auto-Restart)
Write-Log "Creating Auto-Restart Task..."
$Trigger = New-ScheduledTaskTrigger -AtLogOn
$Action = New-ScheduledTaskAction -Execute "python.exe" -Argument "scripts/ultra_light_launch.py" -WorkingDirectory (Get-Location).Path
Register-ScheduledTask -TaskName "MT5_Survivor_Bot" -Trigger $Trigger -Action $Action -Force | Out-Null
Write-Log "Auto-Restart task created (MT5_Survivor_Bot)."

# 6. Lancement initial
Write-Log "Launching Bot in Ultra-Light Mode..."
Start-Process python.exe -ArgumentList "scripts/ultra_light_launch.py" -WindowStyle Hidden

Write-Log "=========================================================="
Write-Log "DEPLOYMENT COMPLETE. The bot is running in shadow mode."
Write-Log "Monitor activity in: logs/ultra_light.log"
Write-Log "=========================================================="
