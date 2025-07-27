"""
test_voice_manager.py
Unit tests for the voice_manager module in Rhee_AI_Assistant.
"""

import unittest
import logging
from datetime import datetime
from voice_ai.voice_manager import VoiceManager

class TestVoiceManager(unittest.TestCase):
    """Test suite for voice manager with dynamic voice morphing."""

    def setUp(self):
        """Set up test environment."""
        self.agent_id = "voice_agent_001"
        self.voice_manager = VoiceManager(self.agent_id)
        self.logger = logging.getLogger(__name__)
        self.logger.info("Test environment set up for VoiceManager agent %s at 05:23 PM IST, Sunday, July 27, 2025", self.agent_id)

    def test_generate_audio(self):
        """Test audio generation with emotion-based voice morphing."""
        text = "Hello, welcome to the omniverse!"
        emotion = "calm"
        config = {"language": "en-US", "pitch": 1.0, "speed": 1.0}
        audio_output = self.voice_manager.generate_audio(text, emotion, config)
        self.assertTrue(audio_output.startswith(b"audio_data_calm"))
        self.logger.info("Audio generation test passed for agent %s, emotion %s at 05:23 PM IST, Sunday, July 27, 2025",
                         self.agent_id, emotion)

    def test_select_voice_profile(self):
        """Test voice profile selection."""
        emotion = "happy"
        config = {"default_voice": "calm"}
        profile = self.voice_manager._select_voice_profile(emotion, config)
        self.assertEqual(profile, "calm")  # "happy" not in voice_profiles, uses fallback
        emotion = "excited"
        profile = self.voice_manager._select_voice_profile(emotion, config)
        self.assertEqual(profile, "excited")
        self.logger.info("Voice profile selection test passed for agent %s at 05:23 PM IST, Sunday, July 27, 2025", self.agent_id)

    def test_generate_audio_invalid_emotion(self):
        """Test audio generation with invalid emotion."""
        text = "Hello, welcome!"
        emotion = "unknown"
        config = {"default_voice": "calm", "language": "en-US"}
        audio_output = self.voice_manager.generate_audio(text, emotion, config)
        self.assertTrue(audio_output.startswith(b"audio_data_calm"))
        self.logger.info("Invalid emotion audio generation test passed for agent %s at 05:23 PM IST, Sunday, July 27, 2025",
                         self.agent_id)

if __name__ == '__main__':
    unittest.main()
