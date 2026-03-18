import logging

logger = logging.getLogger("CommissionHandler")

class CommissionHandler:
    """
    Module d'Interopérabilité Totale pour la gestion des gains et commissions.
    Calcule 10% de prélèvement sur chaque trade gagnant.
    """
    
    def __init__(self, commission_rate=0.10):
        self.commission_rate = commission_rate

    def calculate_commission(self, profit):
        """
        Calcule la commission due sur un profit.
        N'applique la commission que sur les bénéfices nets.
        """
        if profit <= 0:
            return 0.0
            
        commission = profit * self.commission_rate
        logger.info(f"Profit détecté: {profit:.2f}$ | Commission (10%): {commission:.2f}$")
        return round(commission, 2)

    def report_to_saas(self, trade_id, profit, commission):
        """
        Prépare les données pour le rapportage en temps réel vers le backend SaaS.
        C'est ici que la valeur ajoutée et les risques sont quantifiés.
        """
        payload = {
            "trade_id": trade_id,
            "net_profit": profit,
            "commission_due": commission,
            "status": "ETHICAL_REPORT_GENERATED"
        }
        # Logique de transmission API à implémenter dans le module SaaS communication
        return payload
