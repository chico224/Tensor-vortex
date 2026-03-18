import logging
import json
from datetime import datetime, timedelta
import pandas as pd

logger = logging.getLogger("ReportingEngine")

class ReportingEngine:
    """
    Moteur de journalisation Cognitive.
    Génère deux flux de données :
    1. Flux Terminal (Markdown/Log détaillé pour le propriétaire)
    2. Flux API Front-End (JSON structuré avec séries temporelles pour les graphiques Web)
    """
    
    def __init__(self, db_manager):
        self.db = db_manager

    def simulate_trades_for_report(self):
         """Simule quelques données dans un format DataFrame pour générer le rapport si la DB est vide.
         A terme, ceci fera des requêtes SQL réelles sur `self.db`."""
         dates = pd.date_range(end=datetime.now(), periods=50, freq='4H')
         profits = [10.5, -3.2, 15.0, 20.1, -5.5] * 10
         symbols = ["EURUSD", "XAUUSD", "USDJPY"] * 16 + ["EURUSD", "XAUUSD"]
         actions = ["BUY", "SELL"] * 25
         
         df = pd.DataFrame({
             "time": dates,
             "symbol": symbols,
             "action": actions,
             "profit": profits,
         })
         return df

    def _aggregate_data(self, df, timeframe="daily"):
        """Agrège les données en fonction du temps."""
        df['time'] = pd.to_datetime(df['time'])
        df = df.set_index('time')
        
        rule = 'D' if timeframe == "daily" else 'W' if timeframe == "weekly" else 'ME'
        
        # Rééchantillonage pour graphiques
        grouped = df.resample(rule).agg(
            total_trades=('profit', 'count'),
            win_trades=('profit', lambda x: (x > 0).sum()),
            loss_trades=('profit', lambda x: (x <= 0).sum()),
            gross_profit=('profit', lambda x: x[x > 0].sum()),
            gross_loss=('profit', lambda x: x[x <= 0].sum()),
            net_profit=('profit', 'sum')
        ).fillna(0)
        
        return grouped

    def generate_terminal_report(self, timeframe="monthly", account_id="ADMIN"):
        """
        Format: Texte brut analytique & détaillé (Sans Graphique).
        Idéal pour lecture dans une console Bash / Fichier texte de log.
        """
        df = self.simulate_trades_for_report()
        agg = self._aggregate_data(df, timeframe)
        
        total_net = agg['net_profit'].sum()
        win_rate = (agg['win_trades'].sum() / agg['total_trades'].sum() * 100) if agg['total_trades'].sum() > 0 else 0
        
        report = f"==============================================\n"
        report += f"📊 RAPPORT TENSOR-VORTEX CORE (Compte: {account_id})\n"
        report += f"📅 Période: {timeframe.upper()}\n"
        report += f"==============================================\n\n"
        
        report += "🔍 [RÉSUMÉ EXÉCUTIF]\n"
        report += f"- Profit Net Total : ${total_net:.2f}\n"
        report += f"- Win Rate Global  : {win_rate:.1f}%\n"
        report += f"- Total Trades     : {agg['total_trades'].sum()}\n\n"
        
        report += "📝 [DÉTAILS PÉRIODIQUES]\n"
        for date, row in agg.iterrows():
            date_str = date.strftime("%Y-%m-%d")
            report += f"[{date_str}] Profit: ${row['net_profit']:.2f} | Gagnants: {row['win_trades']} | Perdants: {row['loss_trades']}\n"
            
        report += f"\n==============================================\n"
        return report

    def generate_web_payload(self, timeframe="monthly"):
        """
        Format: JSON strict pour API Front-End.
        Sera consommé par les librairies JS (Recharts, Chart.js) sur le Dashboard utilisateur.
        """
        df = self.simulate_trades_for_report()
        agg = self._aggregate_data(df, timeframe)
        
        labels = [date.strftime("%Y-%m-%d") for date in agg.index]
        profits_data = agg['net_profit'].tolist()
        cumulative_profits = agg['net_profit'].cumsum().tolist()
        win_rates = (agg['win_trades'] / agg['total_trades'] * 100).fillna(0).tolist()
        
        payload = {
            "timeframe": timeframe,
            "charts": {
                "labels": labels, # Axe X : Dates
                "bar_chart_profit": profits_data, # Histogramme des profits/pertes par période
                "line_chart_equity": cumulative_profits, # Courbe de croissance du capital
                "line_chart_winrate": win_rates # Evolution de la précision de l'IA
            },
            "summary": {
                "total_trades": int(agg['total_trades'].sum()),
                "gross_profit": float(agg['gross_profit'].sum()),
                "net_profit": float(agg['net_profit'].sum()),
                "overall_winrate": float((agg['win_trades'].sum() / agg['total_trades'].sum() * 100) if agg['total_trades'].sum() > 0 else 0)
            }
        }
        return json.dumps(payload, indent=2)

if __name__ == "__main__":
    re = ReportingEngine(None)
    print("--- TEST TERMINAL ---")
    print(re.generate_terminal_report(timeframe="daily"))
    print("\n--- TEST API WEB (JSON) ---")
    print(re.generate_web_payload(timeframe="weekly"))
