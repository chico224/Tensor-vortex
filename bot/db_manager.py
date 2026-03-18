import sqlite3
import pandas as pd
import logging
import os
from datetime import datetime

logger = logging.getLogger("DBManager")

class DBManager:
    """
    Gestionnaire de base de données SQLite pour optimiser la RAM.
    Stocke les bougies et les signaux pour libérer la mémoire vive du VPS.
    """
    
    def __init__(self, db_path="data/trading_bot.db"):
        self.db_path = db_path
        os.makedirs(os.path.dirname(self.db_path), exist_ok=True)
        self._init_db()

    def _init_db(self):
        """Initialise les tables si elles n'existent pas."""
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        
        # Table pour les bougies (Time Series)
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS market_data (
                symbol TEXT,
                timeframe TEXT,
                time INTEGER,
                open REAL,
                high REAL,
                low REAL,
                close REAL,
                tick_volume INTEGER,
                PRIMARY KEY (symbol, timeframe, time)
            )
        ''')
        
        # Table pour le journal des trades
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS trade_journal (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
                symbol TEXT,
                type TEXT,
                price REAL,
                lots REAL,
                profit REAL,
                unanimity_score INTEGER,
                comment TEXT
            )
        ''')
        
        conn.commit()
        conn.close()

    def save_market_data(self, symbol, timeframe, df):
        """Sauvegarde les DataFrames pandas dans SQLite."""
        if df.empty:
            return
            
        conn = sqlite3.connect(self.db_path)
        df = df.copy()
        df['symbol'] = symbol
        df['timeframe'] = timeframe
        
        # On utilise "REPLACE" pour éviter les doublons sur la PK
        df.to_sql('market_data', conn, if_exists='append', index=False, method='multi')
        conn.close()

    def get_latest_data(self, symbol, timeframe, limit=500):
        """Récupère les dernières données pour analyse."""
        conn = sqlite3.connect(self.db_path)
        query = f"""
            SELECT * FROM market_data 
            WHERE symbol = '{symbol}' AND timeframe = '{timeframe}'
            ORDER BY time DESC LIMIT {limit}
        """
        df = pd.read_sql_query(query, conn)
        conn.close()
        return df.sort_values(by='time')

    def log_trade(self, symbol, trade_type, price, lots, score, comment=""):
        """Enregistre un trade dans le journal."""
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        cursor.execute('''
            INSERT INTO trade_journal (symbol, type, price, lots, unanimity_score, comment)
            VALUES (?, ?, ?, ?, ?, ?)
        ''', (symbol, trade_type, price, lots, score, comment))
        conn.commit()
        conn.close()
