"""Unit tests for multi-lingual-concept-aligner."""
import unittest
from multi_lingual_concept_aligner.aligner import MultiLingualConceptAligner

class TestMultiLingualConceptAligner(unittest.TestCase):
    def setUp(self):
        self.aligner = MultiLingualConceptAligner()

    def test_spanish_alignment(self):
        res = self.aligner.align("consulta a base de datos")
        self.assertEqual(res.detected_language, "es")
        self.assertIn("database", res.normalized_english_terms)

    def test_german_alignment(self):
        res = self.aligner.align("fehler in der datenbank")
        self.assertEqual(res.detected_language, "de")
        self.assertIn("database", res.normalized_english_terms)
