# tests/test_metaphysical_knowledge_synthesizer.py
import unittest
from akashic_link.metaphysical_knowledge_synthesizer.metaphysical_knowledge_synthesizer import MetaphysicalKnowledgeSynthesizer

class TestMetaphysicalKnowledgeSynthesizer(unittest.TestCase):
    def setUp(self):
        self.synthesizer = MetaphysicalKnowledgeSynthesizer()

    def test_crystallize_fractal_knowledge(self):
        input_fractals = [{"data": {"knowledge_vector": 0.8}}, {"data": {"knowledge_vector": 0.9}}]
        synthesis_id = "synthesis1"
        knowledge = self.synthesizer.crystallize_fractal_knowledge(synthesis_id, input_fractals, dimension="primary")
        self.assertEqual(knowledge["id"], synthesis_id)
        state = self.synthesizer.get_fractal_knowledge_state(synthesis_id)
        self.assertGreater(len(state["fractals"]), 0)
        self.assertGreater(state["quantum_crystallization_coherence"], 0.0)

if __name__ == "__main__":
    unittest.main()
