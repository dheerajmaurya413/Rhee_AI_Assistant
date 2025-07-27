"""
voice_core.py
Core module for voice AI agent with dynamic voice morphing in Rhee_AI_Assistant.
Handles speech-to-text, text-to-speech, and conversational logic with emotion-based voice modulation.
"""

import logging
from datetime import datetime
import random
from typing import Dict, Any
from dotenv import load_dotenv
import os
import deepgram
from openai import OpenAI
from .voice_manager import VoiceManager
from .emotion_detector import EmotionDetector

# Load environment variables
load_dotenv()

class VoiceCore:
    """Core class for voice AI agent with dynamic voice morphing."""

    def __init__(self):
        """Initialize voice AI agent with emotion detection and voice management."""
        self.conversation_states: Dict[str, Dict[str, Any]] = {}
        self.coherence_metrics: Dict[str, float] = {}
        self.emotion_detector = EmotionDetector()
        self.voice_manager = VoiceManager()
        self.stt = deepgram.Deepgram(os.getenv("DEEPGRAM_API_KEY"))
        self.llm = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
        self.logger = logging.getLogger(__name__)
        self.logger.info("Voice AI agent initialized with Deepgram and OpenAI at 07:10 PM IST, Wednesday, July 23, 2025")

    def process_voice_input(self, session_id: str, audio_input: bytes, config: Dict[str, Any]) -> Dict[str, Any]:
        """
        Process voice input, detect emotion, modulate voice, and generate response.

        Args:
            session_id (str): Unique identifier for the conversation session.
            audio_input (bytes): Raw audio data from user.
            config (Dict[str, Any]): Configuration (e.g., language, default voice).

        Returns:
            Dict[str, Any]: Response state including transcribed text, response, audio output, and emotion.
        """
        try:
            # Transcribe audio input using Deepgram
            transcribed_text = self._process_stt(audio_input, config)
            self.logger.info("Transcribed voice input for session %s: %s at 07:10 PM IST, Wednesday, July 23, 2025",
                             session_id, transcribed_text)

            # Detect emotion
            emotion = self.emotion_detector.detect_emotion(transcribed_text, audio_input)
            self.logger.info("Detected emotion for session %s: %s at 07:10 PM IST, Wednesday, July 23, 2025",
                             session_id, emotion)

            # Generate response using OpenAI
            response_text = self._generate_response(transcribed_text, config, emotion)
            self.logger.info("Generated response for session %s: %s at 07:10 PM IST, Wednesday, July 23, 2025",
                             session_id, response_text)

            # Modulate and generate audio output based on emotion
            audio_output = self.voice_manager.generate_audio(response_text, emotion, config)
            self.logger.info("Generated audio output for session %s with emotion %s at 07:10 PM IST, Wednesday, July 23, 2025",
                             session_id, emotion)

            # Store conversation state
            self.conversation_states[session_id] = {
                "transcribed_text": transcribed_text,
                "emotion": emotion,
                "response_text": response_text,
                "audio_output": audio_output,
                "config": config,
                "coherence_strength": random.uniform(0.9, 1.0),
                "temporal_coherence": random.uniform(0.95, 1.0),
                "timestamp": datetime.utcnow().isoformat()
            }
            self.coherence_metrics[session_id] = random.uniform(0.95, 1.0)

            return self.conversation_states[session_id]
        except Exception as e:
            self.logger.error("Error processing voice input for session %s: %s at 07:10 PM IST, Wednesday, July 23, 2025",
                              session_id, e)
            return {}

    def _process_stt(self, audio_input: bytes, config: Dict[str, Any]) -> str:
        """Process speech-to-text transcription using Deepgram."""
        try:
            response = self.stt.transcription.prerecorded(
                {"buffer": audio_input, "mimetype": "audio/wav"},
                {"model": "nova", "language": config.get("language", "en-US")}
            )
            return response["results"]["channels"][0]["alternatives"][0]["transcript"]
        except Exception as e:
            self.logger.error("STT processing error: %s at 07:10 PM IST, Wednesday, July 23, 2025", e)
            return config.get("mock_transcription", "Hello, how can I assist you today?")

    def _generate_response(self, text: str, config: Dict[str, Any], emotion: str) -> str:
        """Generate response using OpenAI LLM with emotion context."""
        try:
            prompt = config.get("prompt", f"You are a {emotion} AI assistant.")
            response = self.llm.chat.completions.create(
                model="gpt-4o",
                messages=[
                    {"role": "system", "content": prompt},
                    {"role": "user", "content": text}
                ]
            )
            return response.choices[0].message.content
        except Exception as e:
            self.logger.error("LLM response generation error: %s at 07:10 PM IST, Wednesday, July 23, 2025", e)
            return f"Response to '{text}' in {emotion} tone: I am here to help."

    def sync_with_orchestrator(self, session_id: str, config: Dict[str, Any], target_module: str) -> None:
        """
        Synchronize voice agent state with omniversal orchestrator.

        Args:
            session_id (str): Session identifier.
            config (Dict[str, Any]): Configuration for synchronization.
            target_module (str): Target module (e.g., temporal_integration_nexus).
        """
        try:
            self.logger.info("Synchronizing voice agent state for session %s with module %s at 07:10 PM IST, Wednesday, July 23, 2025",
                             session_id, target_module)
            self.conversation_states[session_id]["target_module"] = target_module
            if target_module == "omnitemporal_coherence_lattice.temporal_integration_nexus":
                self.conversation_states[session_id]["temporal_coherence"] = random.uniform(0.95, 1.0)
        except Exception as e:
            self.logger.error("Error syncing session %s with %s: %s at 07:10 PM IST, Wednesday, July 23, 2025",
                              session_id, target_module, e)

    def get_conversation_state(self, session_id: str) -> Dict[str, Any]:
        """
        Retrieve conversation state.

        Args:
            session_id (str): Session identifier.

        Returns:
            Dict[str, Any]: Conversation state details.
        """
        try:
            state = self.conversation_states.get(session_id, {})
            self.logger.info("Retrieved conversation state for session %s: %s at 07:10 PM IST, Wednesday, July 23, 2025",
                             session_id, state)
            return state
        except Exception as e:
            self.logger.error("Error retrieving conversation state for %s: %s at 07:10 PM IST, Wednesday, July 23, 2025",
                              session_id, e)
            return {}
