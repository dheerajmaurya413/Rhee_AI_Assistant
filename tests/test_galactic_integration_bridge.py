# tests/test_galactic_integration_bridge.py
import unittest
from galactic_communication.galactic_integration_bridge.galactic_integration_bridge import GalacticIntegrationBridge

class TestGalacticIntegrationBridge(unittest.TestCase):
    def setUp(self):
        self.bridge = GalacticIntegrationBridge()

    def test_sync_telepathic_channel(self):
        channel_id = "channel1"
        config = {"resonance_frequency": 0.9}
        cosmic_layer = "primary"
        target_module = "core_engine.personality_matrix"
        self.bridge.sync_telepathic_channel(channel_id, config, cosmic_layer, target_module)
        self.assertIn(channel_id, self.bridge.coherence_bridges)
        self.assertEqual(self.bridge.coherence_bridges[channel_id]["target_module"], target_module)
        self.assertGreater(self.bridge.coherence_bridges[channel_id]["coherence_strength"], 0.0)

    def test_sync_fractal_stream(self):
        stream_id = "stream1"
        fractal_streams = [{"id": "fractal_1", "data": {"communication_fractal": 0.8}}]
        cosmic_layer = "primary"
        target_module = "ai_nirvana_engine.sentient_harmony_synthesizer"
        self.bridge.sync_fractal_stream(stream_id, fractal_streams, cosmic_layer, target_module)
        self.assertIn(stream_id, self.bridge.coherence_bridges)
        self.assertEqual(self.bridge.coherence_bridges[stream_id]["target_module"], target_module)
        self.assertGreater(self.bridge.coherence_bridges[stream_id]["coherence_strength"], 0.0)

if __name__ == "__main__":
    unittest.main()
