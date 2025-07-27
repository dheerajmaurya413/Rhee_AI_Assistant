"""
voice_manager.py
Manages dynamic voice morphing and audio generation for Rhee_AI_Assistant.
Selects and modulates voice profiles based on emotion and context.
"""

import logging
from datetime import datetime
import random
from typing import Dict, Any
import os
from dotenv import load_dotenv
from elevenlabs import ElevenLabs

# Load environment variables
load_dotenv()

class VoiceManager:
    """Manages voice profiles and dynamic voice morphing."""

    def __init__(self, agent_id: str):
        """Initialize voice manager with available voice profiles and agent ID."""
        self.agent_id = agent_id
        self.voice_profiles = [
            "calm", "gentle", "melodious", "romantic", "energetic", "sad", "angry", "playful",
            "mysterious", "spiritual", "sleepy", "excited", "sarcastic", "confident", "inspirational",
            "professional", "dreamy", "fearful", "caring", "shy", "serious", "flirty", "angelic", "epic"
        ]
        self.tts = ElevenLabs(api_key=os.getenv("ELEVENLABS_API_KEY"))
        self.logger = logging.getLogger(__name__)
        self.logger.info("Voice manager for agent %s initialized with %d profiles and ElevenLabs at 05:23 PM IST, Sunday, July 27, 2025",
                         agent_id, len(self.voice_profiles))

    def generate_audio(self, text: str, emotion: str, config: Dict[str, Any]) -> bytes:
        """
        Generate audio output with emotion-based voice modulation.

        Args:
            text (str): Text to convert to speech.
            emotion (str): Detected emotion to select voice profile.
            config (Dict[str, Any]): Configuration (e.g., language, pitch).

        Returns:
            bytes: Audio data for the response.
        """
        try:
            voice_profile = self._select_voice_profile(emotion, config)
            self.logger.info("Agent %s selected voice profile %s for emotion %s at 05:23 PM IST, Sunday, July 27, 2025",
                             self.agent_id, voice_profile, emotion)
            audio_output = self._generate_tts(text, voice_profile, config)
            return audio_output
        except Exception as e:
            self.logger.error("Agent %s error generating audio for emotion %s: %s at 05:23 PM IST, Sunday, July 27, 2025",
                              self.agent_id, emotion, e)
            return b""

    def _select_voice_profile(self, emotion: str, config: Dict[str, Any]) -> str:
        """Select voice profile based on emotion and configuration."""
        if emotion.lower() in self.voice_profiles:
            return emotion.lower()
        fallback = config.get("default_voice", "calm")
        self.logger.warning("Agent %s emotion %s not found, using fallback voice %s at 05:23 PM IST, Sunday, July 27, 2025",
                            self.agent_id, emotion, fallback)
        return fallback

    def _generate_tts(self, text: str, voice_profile: str, config: Dict[str, Any]) -> bytes:
        """Generate text-to-speech with voice modulation using ElevenLabs."""
        try:
            voice_settings = {
                "pitch": config.get("pitch", 1.0),
                "speed": config.get("speed", 1.0),
                "stability": config.get("stability", 0.5)
            }
            voice_path = os.path.join("voices", f"{voice_profile}.wav")
            if os.path.exists(voice_path):
                voice_id = voice_profile
            else:
                voice_id = "default"
            audio = self.tts.generate(text=text, voice=voice_id, voice_settings=voice_settings, user=self.agent_id)
            return audio
        except Exception as e:
            self.logger.error("Agent %s TTS generation error for voice %s: %s at 05:23 PM IST, Sunday, July 27, 2025",
                              self.agent_id, voice_profile, e)
            return b"audio_data_" + voice_profile.encode()
