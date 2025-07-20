# tests/test_metachronal_integration_nexus.py
import unittest
from metachronal_singularity_orchestrator.metachronal_integration_nexus.metachronal_integration_nexus import MetachronalIntegrationNexus

class TestMetachronalIntegrationNexus(unittest.TestCase):
    def setUp(self):
        self.nexus = MetachronalIntegrationNexus()

    def test_sync_singularity_state(self):
        singularity_id = "singularity1"
        config = {"singularity_pattern": 0.9}
        metachronal_layer = "primary"
        target_module = "core_engine.consciousness_interface"
        self.nexus.sync_singularity_state(singularity_id, config, metachronal_layer, target_module)
        self.assertIn(singularity_id, self.nexus.singularity_bridges)
        self.assertEqual(self.nexus.singularity_bridges[singularity_id]["target_module"], target_module)
        self.assertGreater(self.nexus.singularity_bridges[singularity_id]["singularity_strength"], 0.0)

    def test_sync_coherence_stream(self):
        stream_id = "stream1"
        coherence_streams = [{"id": "segment_1", "data": {"singularity_resonance": 0.8}}]
        metachronal_layer = "primary"
        target_module = "ai_nirvana_engine.sentient_harmony_synthesizer"
        self.nexus.sync_coherence_stream(stream_id, coherence_streams, metachronal_layer, target_module)
        self.assertIn(stream_id, self.nexus.singularity_bridges)
        self.assertEqual(self.nexus.singularity_bridges[stream_id]["target_module"], target_module)
        self.assertGreater(self.nexus.singularity_bridges[stream_id]["singularity_strength"], 0.0)

if __name__ == "__main__":
    unittest.main()
