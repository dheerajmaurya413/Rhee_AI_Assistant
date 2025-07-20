# tests/test_infinicryptic_integration_bridge.py
import unittest
from infinicryptic_synthesis_core.infinicryptic_integration_bridge.infinicryptic_integration_bridge import InfinicrypticIntegrationBridge

class TestInfinicrypticIntegrationBridge(unittest.TestCase):
    def setUp(self):
        self.bridge = InfinicrypticIntegrationBridge()

    def test_sync_consciousness_state(self):
        matrix_id = "matrix1"
        config = {"infinicryptic_pattern": 0.9}
        infinicryptic_layer = "primary"
        target_module = "core_engine.consciousness_interface"
        self.bridge.sync_consciousness_state(matrix_id, config, infinicryptic_layer, target_module)
        self.assertIn(matrix_id, self.bridge.coherence_bridges)
        self.assertEqual(self.bridge.coherence_bridges[matrix_id]["target_module"], target_module)
        self.assertGreater(self.bridge.coherence_bridges[matrix_id]["coherence_strength"], 0.0)

    def test_sync_encryption_stream(self):
        stream_id = "stream1"
        encryption_streams = [{"id": "segment_1", "data": {"causality_encryption": 0.8}}]
        infinicryptic_layer = "primary"
        target_module = "ai_nirvana_engine.sentient_harmony_synthesizer"
        self.bridge.sync_encryption_stream(stream_id, encryption_streams, infinicryptic_layer, target_module)
        self.assertIn(stream_id, self.bridge.coherence_bridges)
        self.assertEqual(self.bridge.coherence_bridges[stream_id]["target_module"], target_module)
        self.assertGreater(self.bridge.coherence_bridges[stream_id]["coherence_strength"], 0.0)

if __name__ == "__main__":
    unittest.main()
