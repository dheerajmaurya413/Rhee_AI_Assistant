"""
test_voice_core.py
Unit tests for the voice_core module with dynamic voice morphing in Rhee_AI_Assistant.
"""

import unittest
import logging
from datetime import datetime
from voice_ai.voice_core import VoiceCore

class TestVoiceCore(unittest.TestCase):
    """Test suite for voice AI agent with dynamic voice morphing."""

    def setUp(self):
        """Set up test environment."""
        self.agent_id = "voice_agent_001"
        self.voice_core = VoiceCore(self.agent_id)
        self.logger = logging.getLogger(__name__)
        self.logger.info("Test environment set up for VoiceCore agent %s at 05:23 PM IST, Sunday, July 27, 2025", self.agent_id)

    def test_process_voice_input(self):
        """Test voice input processing with dynamic voice morphing."""
        session_id = "test_session_001"
        audio_input = b"test_audio_data"
        config = {"prompt": "You are a friendly AI assistant.", "language": "en-US", "mock_transcription": "I feel happy!"}
        state = self.voice_core.process_voice_input(session_id, audio_input, config)
        self.assertIn("transcribed_text", state)
        self.assertIn("emotion", state)
        self.assertIn("response_text", state)
        self.assertIn("audio_output", state)
        self.assertEqual(state["config"], config)
        self.assertEqual(state["agent_id"], self.agent_id)
        self.assertGreater(state["coherence_strength"], 0.9)
        self.assertGreater(state["temporal_coherence"], 0.95)
        self.assertEqual(state["emotion"], "happy")
        self.logger.info("Voice input processing test passed for agent %s, session %s at 05:23 PM IST, Sunday, July 27, 2025",
                         self.agent_id, session_id)

    def test_sync_with_orchestrator(self):
        """Test synchronization with omniversal orchestrator."""
        session_id = "test_session_002"
        config = {"prompt": "You are a friendly AI assistant.", "language": "en-US"}
        target_module = "omnitemporal_coherence_lattice.temporal_integration_nexus"
        self.voice_core.sync_with_orchestrator(session_id, config, target_module)
        state = self.voice_core.get_conversation_state(session_id)
        self.assertEqual(state.get("target_module"), target_module)
        self.assertEqual(state.get("agent_id"), self.agent_id)
        self.assertGreater(state.get("temporal_coherence", 0.0), 0.9)
        self.logger.info("Orchestrator sync test passed for agent %s, session %s at 05:23 PM IST, Sunday, July 27, 2025",
                         self.agent_id, session_id)

    def test_get_conversation_state_failure(self):
        """Test retrieval of non-existent conversation state."""
        state = self.voice_core.get_conversation_state("non_existent_session")
        self.assertEqual(state, {})
        self.logger.info("Non-existent conversation state test passed for agent %s at 05:23 PM IST, Sunday, July 27, 2025",
                         self.agent_id)

if __name__ == '__main__':
    unittest.main()
