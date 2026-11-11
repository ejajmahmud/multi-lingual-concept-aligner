"""Core Multi-Lingual Concept Aligner implementation."""
import re
from dataclasses import dataclass
from typing import Dict, List, Optional, Set

@dataclass
class AlignedConcept:
    detected_language: str
    original_terms: List[str]
    normalized_english_terms: List[str]
    confidence: float

class MultiLingualConceptAligner:
    """Projects non-English technical keywords into standardized English technical terminology."""
    
    # Pre-computed technical multilingual lexicon
    LEXICON = {
        # Spanish
        "base de datos": "database", "servidor": "server", "memoria": "memory",
        "bloqueo": "deadlock", "red": "network", "archivo": "file",
        # German
        "datenbank": "database", "speicher": "memory", "netzwerk": "network",
        "abfrage": "query", "fehlermeldung": "error message",
        # French
        "serveur": "server", "fichier": "file", "requete": "query", "connexion": "connection"
    }

    def detect_language(self, text: str) -> str:
        text_lower = text.lower()
        if any(w in text_lower for w in ["datenbank", "speicher", "netzwerk"]):
            return "de"
        if any(w in text_lower for w in ["base de datos", "servidor", "bloqueo"]):
            return "es"
        if any(w in text_lower for w in ["fichier", "serveur", "requete"]):
            return "fr"
        return "en"

    def align(self, query: str) -> AlignedConcept:
        lang = self.detect_language(query)
        words = query.lower().split()
        normalized = []
        original = []

        query_lower = query.lower()
        for phrase, eng in self.LEXICON.items():
            if phrase in query_lower:
                original.append(phrase)
                normalized.append(eng)

        if not normalized:
            normalized = words
            conf = 0.5
        else:
            conf = 0.95

        return AlignedConcept(
            detected_language=lang,
            original_terms=original if original else words,
            normalized_english_terms=normalized,
            confidence=conf
        )
