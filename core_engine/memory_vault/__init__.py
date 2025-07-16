# core_engine/memory_vault/__init__.py
"""
Initializes the memory_vault package.
This module provides secure, encrypted, and modular access to AI memory systems,
including long-term memory, emotional memory, and quantum-memory integration.
"""

import importlib
import logging

# Logger setup
logger = logging.getLogger("MemoryVault")
logger.setLevel(logging.INFO)

# Stream handler for output
stream_handler = logging.StreamHandler()
stream_handler.setFormatter(logging.Formatter('%(asctime)s - %(levelname)s - %(message)s'))
logger.addHandler(stream_handler)

# Core modules within memory_vault (expandable)
__all__ = [
    'memory_vault_core'
]

# Dynamically load modules in __all__
for module in __all__:
    try:
        globals()[module] = importlib.import_module(f'.{module}', __name__)
        logger.info(f"✔ MemoryVault module loaded: {module}")
    except Exception as e:
        logger.error(f"❌ Failed to load module '{module}': {e}")

# Optional: Entry-point hook function
def initialize_memory_vault():
    """
    Hook for initializing memory vault from external controllers (e.g., agent_controller).
    """
    logger.info("🔐 MemoryVault initialized and ready.")
