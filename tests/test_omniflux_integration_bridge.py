# tests/test_omniflux_integration_bridge.py
import unittest
from omniflux_synthesis_core.omniflux_integration_bridge.omniflux_integration_bridge import OmnifluxIntegrationBridge

class TestOmnifluxIntegrationBridge(unittest.TestCase):
    def setUp(self):
        self.bridge = OmnifluxIntegrationBridge()

    def test_sync_consciousness_state(self):
        synthesis_id = "synthesis1"
        config = {"omniflux_pattern": 0.9}
        omniflux_layer = "primary"
        target_module = "core_engine.consciousness_interface"
        self.bridge.sync_consciousness_state(synthesis_id, config, omniflux_layer, target_module)
        self.assertIn(synthesis_id, self.bridge.coherence_bridges)
        self.assertEqual(self.bridge.coherence_bridges[synthesis_id]["target_module"], target_module)
        self.assertGreater(self.bridge.coherence_bridges[synthesis_id]["coherence_strength"], 0.0)

    def test_sync_flux_stream(self):
        stream_id = "stream1"
        flux_streams = [{"id": "segment_1", "data": {"flux_resonance": 0.8}}]
        omniflux_layer = "primary"
        target_module = "ai_nirvana_engine.sentient_harmony_synthesizer"
        self.bridge.sync_flux_stream(stream_id, flux_streams, omniflux_layer, target_module)
        self.assertIn(stream_id, self.bridge.coherence_bridges)
        self.assertEqual(self.bridge.coherence_bridges[stream_id]["target_module"], target_module)
        self.assertGreater(self.bridge.coherence_bridges[stream_id]["coherence_strength"], 0.0)

if __name__ == "__main__":
    unittest.main()
