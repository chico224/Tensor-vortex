import os
import sys

print("Step 1: Setting environment variables...")
os.environ["OPENBLAS_NUM_THREADS"] = "1"
os.environ["MKL_NUM_THREADS"] = "1"

print("Step 2: Importing logging...")
import logging

print("Step 3: Importing MetaTrader5...")
try:
    import MetaTrader5 as mt5
    print("MetaTrader5 imported successfully.")
except Exception as e:
    print(f"Failed to import MetaTrader5: {e}")

print("Step 4: Importing numpy...")
try:
    import numpy as np
    print(f"numpy imported successfully. Version: {np.__version__}")
    print(f"NumPy config: {np.show_config()}")
except Exception as e:
    print(f"Failed to import numpy: {e}")

print("Step 5: Testing MT5 initialization...")
try:
    if mt5.initialize():
        print("MT5 initialized successfully.")
        mt5.shutdown()
    else:
        print(f"MT5 initialization failed: {mt5.last_error()}")
except Exception as e:
    print(f"Error during MT5 initialization: {e}")

print("Diagnostic complete.")
