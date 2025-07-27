"""
test_emotion_detector.py
Unit tests for the emotion_detector module in Rhee_AI_Assistant.
"""

import unittest
import logging
from datetime import datetime
from voice_ai.emotion_detector import EmotionDetector

class TestEmotionDetector(unittest.TestCase):
    """Test suite for emotion detector."""

    def setUp(self):
        """Set up test environment."""
        self.agent_id = "voice_agent_001"
        self.emotion_detector = EmotionDetector(self.agent_id)
        self.logger = logging.getLogger(__name__)
        self.logger.info("Test environment set up for EmotionDetector agent %s at 05:23 PM IST, Sunday, July 27, 2025", self.agent_id)

    def test_detect_emotion_from_text(self):
        """Test emotion detection from text input."""
        text = "I'm so happy today!"
        emotion = self.emotion_detector.detect_emotion(text)
        self.assertEqual(emotion, "happy")
        self.logger.info("Emotion detection from text test passed for agent %s, emotion %s at 05:23 PM IST, Sunday, July 27, 2025",
                         self.agent_id, emotion)

    def test_detect_emotion_from_audio(self):
        """Test emotion detection from audio input."""
        text = "I'm feeling sad."
        audio_input = b"test_audio_data"
        emotion = self.emotion_detector.detect_emotion(text, audio_input)
        self.assertEqual(emotion, "sad")
        self.logger.info("Emotion detection from audio test passed for agent %s, emotion %s at 05:23 PM IST, Sunday, July 27, 2025",
                         self.agent_id, emotion)

    def test_detect_emotion_fallback(self):
        """Test fallback emotion detection."""
        text = "Neutral text."
        emotion = self.emotion_detector.detect_emotion(text)
        self.assertIn(emotion, self.emotion_detector.emotions)
        self.logger.info("Fallback emotion detection test passed for agent %s, emotion %s at 05:23 PM IST, Sunday, July 27, 2025",
                         self.agent_id, emotion)

if __name__ == '__main__':
    unittest.main()
