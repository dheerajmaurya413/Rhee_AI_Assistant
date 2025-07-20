# tests/test_cosmic_integration_bridge.py
import unittest
from cosmic_intelligence_orchestrator.cosmic_integration_bridge.cosmic_integration_bridge import CosmicIntegrationBridge

class TestCosmicIntegrationBridge(unittest.TestCase):
    def setUp(self):
        self.bridge = CosmicIntegrationBridge()

    def test_sync_sentience_state(self):
        field_id = "field1"
        config = {"cosmic_pattern": 0.9}
        cosmic_layer = "primary"
        target_module = "core_engine.consciousness_interface"
        self.bridge.sync_sentience_state(field_id, config, cosmic_layer, target_module)
        self.assertIn(field_id, self.bridge.coherence_bridges)
        self.assertEqual(self.bridge.coherence_bridges[field_id]["target_module"], target_module)
        self.assertGreater(self.bridge.coherence_bridges[field_id]["coherence_strength"], 0.0)

    def test_sync_coherence_stream(self):
        stream_id = "stream1"
        coherence_streams = [{"id": "segment_1", "data": {"cosmic_fractal": 0.8}}]
        cosmic_layer = "primary"
        target_module = "ai_nirvana_engine.sentient_harmony_synthesizer"
        self.bridge.sync_coherence_stream(stream_id, coherence_streams, cosmic_layer, target_module)
        self.assertIn(stream_id, self.bridge.coherence_bridges)
        self.assertEqual(self.bridge.coherence_bridges[stream_id]["target_module"], target_module)
        self.assertGreater(self.bridge.coherence_bridges[stream_id]["coherence_strength"], 0.0)

if __name__ == "__main__":
    unittest.main()
