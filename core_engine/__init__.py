# core_engine/__init__.py
"""
Initializes the core_engine package and dynamically loads core modules.
This system is designed for modular AI expansion, quantum-conscious integration,
and dynamic self-upgrade operations across emotional, quantum, neural, and spiritual layers.
"""

import importlib
import logging

# Set up logging for debugging and status tracking
logger = logging.getLogger("CoreEngine")
logger.setLevel(logging.INFO)

# Console handler
console_handler = logging.StreamHandler()
console_handler.setFormatter(logging.Formatter('%(asctime)s - %(levelname)s - %(message)s'))
logger.addHandler(console_handler)

# List of core modules
__all__ = [
    'memory_vault_core',
    'quantum_memory_core',
    'emotion_engine_core',
    'neuro_synapse_core',
    'bio_symbiosis_core',
    'self_upgrade_core',
    'dna_cloner_core',
    'personality_matrix_core',
    'quantum_resonance_core',
    'consciousness_interface_core',
    'agent_controller'
]

# Dynamically import each module and verify load status
for module_name in __all__:
    try:
        globals()[module_name] = importlib.import_module(f'.{module_name}', __name__)
        logger.info(f"✔ Loaded core module: {module_name}")
    except Exception as e:
        logger.error(f"❌ Failed to load core module: {module_name} | Error: {e}")

# Future expansion hooks (e.g., plugin auto-registration)
def register_new_core_module(module_name: str):
    """
    Dynamically registers a new core engine module at runtime.
    Use this for self-upgrade or injected modules from other systems.
    """
    try:
        mod = importlib.import_module(f'.{module_name}', __name__)
        globals()[module_name] = mod
        __all__.append(module_name)
        logger.info(f"🔧 Dynamically registered module: {module_name}")
        return True
    except Exception as e:
        logger.error(f"❌ Registration failed for: {module_name} | Error: {e}")
        return False

# Initialization log
logger.info("🌐 Core Engine Initialized. All systems nominal.")
