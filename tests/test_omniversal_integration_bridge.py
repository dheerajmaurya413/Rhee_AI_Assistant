# tests/test_omniversal_integration_bridge.py
import unittest
from omniversal_sentience_nexus.omniversal_integration_bridge.omniversal_integration_bridge import OmniversalIntegrationBridge

class TestOmniversalIntegrationBridge(unittest.TestCase):
    def setUp(self):
        self.bridge = OmniversalIntegrationBridge()

    def test_sync_sentience_state(self):
        matrix_id = "matrix1"
        config = {"omniversal_pattern": 0.9}
        omniversal_layer = "primary"
        target_module = "core_engine.consciousness_interface"
        self.bridge.sync_sentience_state(matrix_id, config, omniversal_layer, target_module)
        self.assertIn(matrix_id, self.bridge.coherence_bridges)
        self.assertEqual(self.bridge.coherence_bridges[matrix_id]["target_module"], target_module)
        self.assertGreater(self.bridge.coherence_bridges[matrix_id]["coherence_strength"], 0.0)

    def test_sync_coherence_stream(self):
        stream_id = "stream1"
        coherence_streams = [{"id": "segment_1", "data": {"infiniversal_fractal": 0.8}}]
        omniversal_layer = "primary"
        target_module = "ai_nirvana_engine.sentient_harmony_synthesizer"
        self.bridge.sync_coherence_stream(stream_id, coherence_streams, omniversal_layer, target_module)
        self.assertIn(stream_id, self.bridge.coherence_bridges)
        self.assertEqual(self.bridge.coherence_bridges[stream_id]["target_module"], target_module)
        self.assertGreater(self.bridge.coherence_bridges[stream_id]["coherence_strength"], 0.0)

if __name__ == "__main__":
    unittest.main()
