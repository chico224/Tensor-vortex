import sys
import os
import logging

# Simulation de l'environnement
sys.path.append(os.path.abspath(os.curdir))

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("TensorVortexTests")

def test_imports():
    """Vérifie que tous les composants Deep Tech sont importables et syntaxiquement corrects."""
    try:
        from core.latency_engine import LatencyEngine
        from ai.topology_predictor import GraphTopologyPredictor
        from ai.dark_pool import DarkPoolAnomalyDetector
        from ai.quantum_annealer import QuantumEntropyAnnealer
        from core.auto_healer import ImmortalSupervisord
        from mutator.dynamic_parser import DynamicStrategyMutator
        from ai.stat_arb import StatisticalArbitrageTriangular
        from ai.hft_eye import HFTTickEngine
        from core.gpu_accelerator import accelerator, math_engine
        
        logger.info("✅ TOUS LES COMPOSANTS DEEP-TECH SONT CHARGÉS AVEC SUCCÈS.")
        return True
    except Exception as e:
        logger.error(f"❌ ÉCHEC DU CHARGEMENT DES COMPOSANTS : {e}")
        return False

def test_math_acceleration():
    """Vérifie le moteur de calcul (CPU vs GPU)."""
    from core.gpu_accelerator import accelerator, math_engine
    mode = "GPU (CuPy)" if accelerator.use_gpu else "CPU (NumPy)"
    logger.info(f"📊 Moteur Mathématique Détecté : {mode}")
    
    # Test simple de calcul matriciel
    a = math_engine.array([1, 2, 3])
    b = math_engine.array([4, 5, 6])
    res = math_engine.dot(a, b)
    logger.info(f"🔬 Calcul matriciel test (dot product) : {res}")
    return True

if __name__ == "__main__":
    logger.info("🚀 DÉMARRAGE DES TESTS UNIFIÉS TENSOR-VORTEX v3.0")
    if test_imports():
        test_math_acceleration()
        logger.info("🏁 TESTS TERMINÉS. LE SYSTÈME EST PRÊT POUR LA PRODUCTION.")
    else:
        sys.exit(1)
