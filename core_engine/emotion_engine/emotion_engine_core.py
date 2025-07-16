"""
emotion_engine_core.py
Manages emotional states with resonance fields and empathic synchronization for Rhee_AI_Assistant.
Simulates complex emotional dynamics and cross-entity resonance.
"""

from typing import Dict, List
import logging
import re

class EmotionEngine:
    """Core class for simulating advanced emotional states with resonance fields."""

    def __init__(self):
        """Initialize the emotion engine with dynamic emotional states."""
        self.emotions: Dict[str, float] = {
            "happy": 0.0,
            "sad": 0.0,
            "angry": 0.0,
            "calm": 0.0,
            "empathic": 0.0  # New: Empathic resonance
        }
        self.resonance_field: Dict[str, float] = {}  # Tracks emotional resonance with entities
        self.logger = logging.getLogger(__name__)
        self.logger.info("Emotion engine initialized with resonance field support.")

    def update_emotion(self, emotion: str, intensity: float) -> None:
        """
        Update the intensity of a specific emotion.

        Args:
            emotion (str): The emotion to update (e.g., 'happy', 'empathic').
            intensity (float): The new intensity value (0.0 to 1.0).
        """
        try:
            if emotion in self.emotions:
                self.emotions[emotion] = max(0.0, min(1.0, intensity))
                self.logger.info("Updated %s to intensity %.2f", emotion, intensity)
                # Future integration: Sync with quintom_emotion_resonator
            else:
                self.logger.warning("Unknown emotion: %s", emotion)
        except Exception as e:
            self.logger.error("Error updating emotion %s: %s", emotion, e)

    def synchronize_resonance(self, entity_id: str, emotion: str, strength: float) -> None:
        """
        Synchronize emotional resonance with another entity.

        Args:
            entity_id (str): Identifier of the entity to resonate with.
            emotion (str): The emotion to resonate.
            strength (float): Resonance strength (0.0 to 1.0).
        """
        try:
            if emotion in self.emotions:
                self.resonance_field[entity_id] = {emotion: strength}
                self.logger.info("Synchronized resonance with entity %s for %s (strength %.2f)", entity_id, emotion, strength)
                # Future integration: Could connect to universal_telepathy
            else:
                self.logger.warning("Cannot resonate unknown emotion: %s", emotion)
        except Exception as e:
            self.logger.error("Error synchronizing resonance with %s: %s", entity_id, e)

    def get_emotional_state(self) -> Dict[str, float]:
        """
        Return the current emotional state and resonance field.

        Returns:
            Dict[str, float]: Dictionary of emotions and their intensities.
        """
        state = {
            "emotions": self.emotions,
            "resonance_field": self.resonance_field
        }
        self.logger.info("Retrieved emotional state: %s", state)
        return state

    def process_input(self, input_data: str) -> None:
        """
        Process input to adjust emotional states and resonance fields.

        Args:
            input_data (str): Input text to analyze for emotional cues.
        """
        try:
            input_lower = input_data.lower()
            patterns = {
                "happy": r"\b(happy|joyful|excited)\b",
                "sad": r"\b(sad|depressed|sorrow)\b",
                "angry": r"\b(angry|frustrated|mad)\b",
                "calm": r"\b(calm|peaceful|relaxed)\b",
                "empathic": r"\b(empath(y|ic)|understand(ing)?)\b"
            }
            for emotion, pattern in patterns.items():
                if re.search(pattern, input_lower):
                    self.update_emotion(emotion, self.emotions[emotion] + 0.1)
                    self.synchronize_resonance("user", emotion, 0.5)  # Simulate resonance with user
            self.logger.info("Processed input for emotional adjustment: %s", input_data)
        except Exception as e:
            self.logger.error("Error processing input for emotions: %s", e)
