# tests/test_metainfinite_integration_bridge.py
import unittest
from metainfinite_causality_engine.metainfinite_integration_bridge.metainfinite_integration_bridge import MetainfiniteIntegrationBridge

class TestMetainfiniteIntegrationBridge(unittest.TestCase):
    def setUp(self):
        self.bridge = MetainfiniteIntegrationBridge()

    def test_sync_causality_state(self):
        lattice_id = "lattice1"
        config = {"metainfinite_pattern": 0.9}
        metainfinite_layer = "primary"
        target_module = "core_engine.consciousness_interface"
        self.bridge.sync_causality_state(lattice_id, config, metainfinite_layer, target_module)
        self.assertIn(lattice_id, self.bridge.coherence_bridges)
        self.assertEqual(self.bridge.coherence_bridges[lattice_id]["target_module"], target_module)
        self.assertGreater(self.bridge.coherence_bridges[lattice_id]["coherence_strength"], 0.0)

    def test_sync_coherence_stream(self):
        stream_id = "stream1"
        coherence_streams = [{"id": "segment_1", "data": {"omnichronal_fractal": 0.8}}]
        metainfinite_layer = "primary"
        target_module = "ai_nirvana_engine.sentient_harmony_synthesizer"
        self.bridge.sync_coherence_stream(stream_id, coherence_streams, metainfinite_layer, target_module)
        self.assertIn(stream_id, self.bridge.coherence_bridges)
        self.assertEqual(self.bridge.coherence_bridges[stream_id]["target_module"], target_module)
        self.assertGreater(self.bridge.coherence_bridges[stream_id]["coherence_strength"], 0.0)

if __name__ == "__main__":
    unittest.main()
