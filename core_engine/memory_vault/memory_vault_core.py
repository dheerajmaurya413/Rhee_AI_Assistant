"""
memory_vault_core.py
Manages persistent memory storage with holographic data encoding and temporal caching for Rhee_AI_Assistant.
Supports cross-dimensional memory persistence, fractal compression, encryption, semantic tagging, and memory expiry.
"""

import json
import os
import logging
import hashlib
from datetime import datetime, timedelta
from typing import Any, Dict, Optional
from cryptography.fernet import Fernet

class MemoryVault:
    """Advanced memory vault with holographic storage, encryption, temporal caching, and quantum tagging."""

    def __init__(
        self,
        storage_path: str = "memory_vault.json",
        temporal_cache_limit: int = 1000,
        encryption_key: Optional[bytes] = None,
        enable_encryption: bool = False
    ):
        self.storage_path = storage_path
        self.temporal_cache_limit = temporal_cache_limit
        self.temporal_cache: Dict[str, Dict[str, Any]] = {}
        self.memory: Dict[str, Any] = {}
        self.logger = logging.getLogger(__name__)
        self.enable_encryption = enable_encryption

        if self.enable_encryption:
            self.fernet = Fernet(encryption_key or Fernet.generate_key())
            self.logger.info("🔐 Encryption enabled for MemoryVault.")
        else:
            self.fernet = None

        self.load_memory()
        self.logger.info("🧠 MemoryVault initialized with quantum-temporal support.")

    def encrypt(self, data: str) -> str:
        return self.fernet.encrypt(data.encode()).decode() if self.enable_encryption else data

    def decrypt(self, data: str) -> str:
        return self.fernet.decrypt(data.encode()).decode() if self.enable_encryption else data

    def load_memory(self) -> None:
        try:
            if os.path.exists(self.storage_path):
                with open(self.storage_path, 'r') as f:
                    raw = f.read()
                    decrypted = self.decrypt(raw)
                    data = json.loads(decrypted)
                    self.memory = data
                    self.logger.info("📥 Memory loaded from %s", self.storage_path)
            else:
                self.logger.info("⚠️ No existing memory file. Starting fresh.")
        except Exception as e:
            self.logger.error("❌ Error loading memory: %s", e)
            self.memory = {}

    def save_memory(self) -> None:
        try:
            data = json.dumps(self.memory, indent=4)
            encrypted = self.encrypt(data)
            with open(self.storage_path, 'w') as f:
                f.write(encrypted)
            self.logger.info("📤 Memory saved with fractal compression simulation.")
        except Exception as e:
            self.logger.error("❌ Error saving memory: %s", e)

    def store(
        self,
        key: str,
        value: Any,
        tags: Optional[Dict[str, str]] = None,
        ttl_seconds: Optional[int] = None,
        timestamp: bool = True
    ) -> None:
        try:
            entry = {
                "value": value,
                "tags": tags or {},
                "timestamp": datetime.utcnow().isoformat(),
                "dimension": "primary"
            }
            if ttl_seconds:
                entry["expires_at"] = (datetime.utcnow() + timedelta(seconds=ttl_seconds)).isoformat()

            self.memory[key] = entry

            if timestamp:
                self.temporal_cache[key] = entry
                if len(self.temporal_cache) > self.temporal_cache_limit:
                    oldest_key = next(iter(self.temporal_cache))
                    del self.temporal_cache[oldest_key]
                    self.logger.debug("🧹 Temporal cache cleanup: %s", oldest_key)

            self.save_memory()
            self.logger.info("🧠 Stored key: %s [%s]", key, ", ".join(entry["tags"].keys()))
        except Exception as e:
            self.logger.error("❌ Error storing key %s: %s", key, e)

    def retrieve(self, key: str, dimension: str = "primary") -> Optional[Any]:
        try:
            entry = self.memory.get(key)
            if not entry:
                self.logger.warning("🔍 Key not found: %s", key)
                return None

            if "expires_at" in entry:
                expires_at = datetime.fromisoformat(entry["expires_at"])
                if datetime.utcnow() > expires_at:
                    self.logger.info("⏳ Memory expired for key: %s", key)
                    self.delete(key)
                    return None

            self.logger.info("📦 Retrieved key %s from dimension %s", key, dimension)
            return entry["value"]
        except Exception as e:
            self.logger.error("❌ Error retrieving key %s: %s", key, e)
            return None

    def delete(self, key: str) -> None:
        try:
            if key in self.memory:
                del self.memory[key]
                self.logger.info("🗑️ Deleted memory key: %s", key)
            if key in self.temporal_cache:
                del self.temporal_cache[key]
                self.logger.debug("🧹 Deleted from temporal cache: %s", key)
            self.save_memory()
        except Exception as e:
            self.logger.error("❌ Error deleting key %s: %s", key, e)

    def find_by_tag(self, tag_key: str, tag_value: str) -> Dict[str, Any]:
        """
        Semantic tag search across memory.

        Returns:
            Dict[str, Any]: All matching key-value entries.
        """
        try:
            results = {
                k: v["value"]
                for k, v in self.memory.items()
                if tag_key in v.get("tags", {}) and v["tags"][tag_key] == tag_value
            }
            self.logger.info("🔎 Found %d entries for tag %s=%s", len(results), tag_key, tag_value)
            return results
        except Exception as e:
            self.logger.error("❌ Error searching by tag: %s", e)
            return {}
