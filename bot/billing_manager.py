import logging
from datetime import datetime
import yaml

logger = logging.getLogger("SmartBilling")

class SmartBillingSystem:
    """
    Gestionnaire centralisé pour la facturation SaaS Web3.
    Applique la Règle du High-Water Mark (3% sur les bénéfices mensuels).
    Exempte automatiquement les comptes Administrateurs.
    """
    def __init__(self, config_path="user_config.yaml"):
        self.admin_accounts = []
        self.fee_percentage = 0.03  # 3%
        self.wallet_address = "0x..." # Devrait être configuré
        self.billing_cycle = "monthly"
        self._load_config(config_path)

    def _load_config(self, config_path):
        try:
            with open(config_path, "r") as f:
                config = yaml.safe_load(f)
                billing = config.get("billing", {})
                self.admin_accounts = [str(acc) for acc in billing.get("admin_accounts", [])]
                self.fee_percentage = billing.get("fee_percentage", 0.03)
                self.wallet_address = billing.get("crypto_wallet", "")
                self.billing_cycle = billing.get("cycle", "monthly")
        except Exception as e:
            logger.warning(f"Erreur chargement config Billing : {e}")

    def is_admin(self, account_id):
        """Vérifie si le compte bénéficie d'une immunité diplomatique totale (Pas de frais, pas de coupure)."""
        return str(account_id) in self.admin_accounts

    def check_suspension_status(self, account_id, last_payment_date, unpaid_invoices=0):
        """
        Détermine si le Cerveau VPS doit continuer de générer des trades pour ce compte.
        """
        if self.is_admin(account_id):
            return False, "Compte Administrateur : Accès Illimité."

        if unpaid_invoices > 0:
            return True, "Facture en attente. Suspendu jusqu'au paiement sur la Blockchain."

        # Si pas encore de date de paiement, c'est le 1er mois "d'essai" / d'accumulation
        if not last_payment_date:
            return False, "Cycle en cours (1er mois)."

        days_since_payment = (datetime.now() - last_payment_date).days
        
        cycle_days = 30 if self.billing_cycle == "monthly" else 7
        if days_since_payment >= cycle_days:
             return True, f"Fin du cycle de {cycle_days} jours. Facturation requise."
             
        return False, "Cycle de facturation en règle."

    def calculate_invoice(self, account_id, gross_profit, previous_high_water_mark):
        """
        Calcule la facture en fonction du vrai profit généré par l'IA.
        Utilise le système High-Water Mark des Hedge Funds :
        L'utilisateur ne paie 3% QUE sur les NOUVELLES performances.
        """
        if self.is_admin(account_id):
            return 0.0, gross_profit # L'admin garde tout, son HWM augmente au max.

        net_new_profit = gross_profit - previous_high_water_mark
        
        if net_new_profit <= 0:
            # L'IA n'a pas dépassé l'ancien record de gains. L'utilisateur ne paie RIEN ce mois-ci.
            return 0.0, previous_high_water_mark
            
        fee_to_pay = net_new_profit * self.fee_percentage
        new_high_water_mark = gross_profit
        
        return fee_to_pay, new_high_water_mark
