import pandas as pd
import numpy as np
from bot.quant_engine import QuantEnsembleEngine

def test_engine_performance():
    print("--- TEST DE PERFORMANCE & COHERENCE (Equipe 50 Experts/50 Ans) ---")
    
    # 1. Simulation de données (500 bougies)
    data = {
        'open': np.random.uniform(1.08, 1.10, 500),
        'high': np.random.uniform(1.08, 1.10, 500),
        'low': np.random.uniform(1.08, 1.10, 500),
        'close': np.random.uniform(1.08, 1.10, 500),
        'tick_volume': np.random.randint(100, 1000, 500)
    }
    df = pd.DataFrame(data)
    
    # 2. Initialisation du moteur
    engine = QuantEnsembleEngine()
    
    # 3. Test de vitesse
    import time
    start = time.time()
    signal, details = engine.evaluate_high_leverage_trade(df)
    end = time.time()
    
    print(f"Analysis of 110 experts completed in: {(end-start)*1000:.2f} ms")
    print(f"Consensus Result (Sniper): {details['confidence']} confidence")
    print(f"SQLite Memory Connected: {engine.db.db_path}")

if __name__ == "__main__":
    test_engine_performance()
