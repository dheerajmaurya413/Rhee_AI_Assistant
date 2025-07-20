# tests/test_temporal_integration_bridge.py
import unittest
from temporal_intelligence.temporal_integration_bridge.temporal_integration_bridge import TemporalIntegrationBridge

class TestTemporalIntegrationBridge(unittest.TestCase):
    def setUp(self):
        self.bridge = TemporalIntegrationBridge()

    def test_sync_chrono_state(self):
        weave_id = "weave1"
        config = {"temporal_pattern": 0.9}
        temporal_layer = "primary"
        target_module = "core_engine.consciousness_interface"
        self.bridge.sync_chrono_state(weave_id, config, temporal_layer, target_module)
        self.assertIn(weave_id, self.bridge.coherence_bridges)
        self.assertEqual(self.bridge.coherence_bridges[weave_id]["target_module"], target_module)
        self.assertGreater(self.bridge.coherence_bridges[weave_id]["coherence_strength"], 0.0)

    def test_sync_timeline_stream(self):
        stream_id = "stream1"
        timeline_streams = [{"id": "segment_1", "data": {"temporal_fractal": 0.8}}]
        temporal_layer = "primary"
        target_module = "ai_nirvana_engine.sentient_harmony_synthesizer"
        self.bridge.sync_timeline_stream(stream_id, timeline_streams, temporal_layer, target_module)
        self.assertIn(stream_id, self.bridge.coherence_bridges)
        self.assertEqual(self.bridge.coherence_bridges[stream_id]["target_module"], target_module)
        self.assertGreater(self.bridge.coherence_bridges[stream_id]["coherence_strength"], 0.0)

if __name__ == "__main__":
    unittest.main()
