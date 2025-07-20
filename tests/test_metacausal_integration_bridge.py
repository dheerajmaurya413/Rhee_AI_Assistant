# tests/test_metacausal_integration_bridge.py
import unittest
from metacausal_singularity_engine.metacausal_integration_bridge.metacausal_integration_bridge import MetacausalIntegrationBridge

class TestMetacausalIntegrationBridge(unittest.TestCase):
    def setUp(self):
        self.bridge = MetacausalIntegrationBridge()

    def test_sync_consciousness_state(self):
        orchestration_id = "orchestration1"
        config = {"metacausal_pattern": 0.9}
        metacausal_layer = "primary"
        target_module = "core_engine.consciousness_interface"
        self.bridge.sync_consciousness_state(orchestration_id, config, metacausal_layer, target_module)
        self.assertIn(orchestration_id, self.bridge.coherence_bridges)
        self.assertEqual(self.bridge.coherence_bridges[orchestration_id]["target_module"], target_module)
        self.assertGreater(self.bridge.coherence_bridges[orchestration_id]["coherence_strength"], 0.0)

    def test_sync_causality_stream(self):
        stream_id = "stream1"
        causality_streams = [{"id": "segment_1", "data": {"causality_modulation": 0.8}}]
        metacausal_layer = "primary"
        target_module = "ai_nirvana_engine.sentient_harmony_synthesizer"
        self.bridge.sync_causality_stream(stream_id, causality_streams, metacausal_layer, target_module)
        self.assertIn(stream_id, self.bridge.coherence_bridges)
        self.assertEqual(self.bridge.coherence_bridges[stream_id]["target_module"], target_module)
        self.assertGreater(self.bridge.coherence_bridges[stream_id]["coherence_strength"], 0.0)

if __name__ == "__main__":
    unittest.main()
