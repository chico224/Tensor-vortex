import numpy as np
import logging

logger = logging.getLogger("TopologyPredictor")

class GraphTopologyPredictor:
    """
    GRAPH TOPOLOGY PREDICTOR (Spatial Shockwaves)
    Modélise le marché mondial comme un graphe non orienté pondéré.
    Calcule des corrélations de Pearson glissantes pour détecter
    les propagations de volatilité avant qu'elles n'atteignent la paire ciblée.
    """
    def __init__(self, symbols_list):
        self.symbols = symbols_list
        # Matrice d'adjacence (Corrélation) dynamique
        self.adjacency_matrix = np.eye(len(symbols_list))
        self.symbol_to_idx = {sym: i for i, sym in enumerate(symbols_list)}
        
    def update_topology(self, price_data_dict):
        """
        Met à jour le graphe avec les rendements (returns) log-périodiques recents.
        price_data_dict: dict { 'EURUSD': array_of_closes, ... }
        """
        try:
            returns = []
            valid_symbols = []
            for sym in self.symbols:
                if sym in price_data_dict and len(price_data_dict[sym]) > 10:
                    prices = np.array(price_data_dict[sym])
                    log_returns = np.diff(np.log(prices))
                    returns.append(log_returns[-10:]) # Regarde vitrès court terme (Ondes HFT)
                    valid_symbols.append(sym)
                    
            if len(returns) > 1:
                ret_matrix = np.vstack(returns)
                # Calcule la matrice de corrélation de Pearson
                corr = np.corrcoef(ret_matrix)
                
                # Mise à jour partielle pour éviter les tremblements
                momentum = 0.8
                for i, sym1 in enumerate(valid_symbols):
                    for j, sym2 in enumerate(valid_symbols):
                        idx1 = self.symbol_to_idx[sym1]
                        idx2 = self.symbol_to_idx[sym2]
                        self.adjacency_matrix[idx1, idx2] = (self.adjacency_matrix[idx1, idx2] * momentum) + (corr[i, j] * (1 - momentum))
        except Exception as e:
            logger.debug(f"Erreur update_topology: {e}")

    def detect_shockwave(self, target_symbol, volatility_dict):
        """
        Si une paire "voisine" dans le graphe subit une volatilité anormale,
        prévoit une onde de choc sur 'target_symbol'.
        volatility_dict: mapping symbol -> recent_volatility_score
        """
        if target_symbol not in self.symbol_to_idx:
            return 0.0
            
        target_idx = self.symbol_to_idx[target_symbol]
        shock_vector = 0.0
        
        for sym, vol in volatility_dict.items():
            if sym == target_symbol or sym not in self.symbol_to_idx:
                continue
            idx = self.symbol_to_idx[sym]
            correlation = self.adjacency_matrix[target_idx, idx]
            
            # Transmission de la force de l'onde via le graphe
            if abs(correlation) > 0.6: # Lien mathématique fort
                # On ajoute le vecteur avec sa charge (positive ou négative)
                shock_vector += vol * correlation
                
        if abs(shock_vector) > 2.0: # Seuil critique
            logger.warning(f"[HFT] Onde de Choc Spatiale détectée vers {target_symbol} (Vecteur: {shock_vector:.3f})")
            
        return shock_vector
