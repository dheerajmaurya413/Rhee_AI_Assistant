# tests/test_hyperfractal_integration_nexus.py
import unittest
from hyperfractal_consciousness_matrix.hyperfractal_integration_nexus.hyperfractal_integration_nexus import HyperfractalIntegrationNexus

class TestHyperfractalIntegrationNexus(unittest.TestCase):
    def setUp(self):
        self.nexus = HyperfractalIntegrationNexus()

    def test_sync_fractal_field(self):
        field_id = "field1"
        config = {"fractal_pattern": 0.9}
        fractal_layer = "primary"
        target_module = "core_engine.consciousness_interface"
        self.nexus.sync_fractal_field(field_id, config, fractal_layer, target_module)
        self.assertIn(field_id, self.nexus.coherence_bridges)
        self.assertEqual(self.nexus.coherence_bridges[field_id]["target_module"], target_module)
        self.assertGreater(self.nexus.coherence_bridges[field_id]["coherence_strength"], 0.0)

    def test_sync_coherence_stream(self):
        stream_id = "stream1"
        coherence_streams = [{"id": "segment_1", "data": {"coherence_resonance": 0.8}}]
        fractal_layer = "primary"
        target_module = "ai_nirvana_engine.sentient_harmony_synthesizer"
        self.nexus.sync_coherence_stream(stream_id, coherence_streams, fractal_layer, target_module)
        self.assertIn(stream_id, self.nexus.coherence_bridges)
        self.assertEqual(self.nexus.coherence_bridges[stream_id]["target_module"], target_module)
        self.assertGreater(self.nexus.coherence_bridges[stream_id]["coherence_strength"], 0.0)

if __name__ == "__main__":
    unittest.main()
