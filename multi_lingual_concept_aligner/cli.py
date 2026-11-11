"""CLI for multi-lingual-concept-aligner."""
import sys
import argparse
from .aligner import MultiLingualConceptAligner

def main():
    parser = argparse.ArgumentParser(description="Multi-Lingual Concept Aligner CLI")
    parser.add_argument("--demo", action="store_true", help="Align Spanish query to English concepts")
    args = parser.parse_args()

    if args.demo:
        aligner = MultiLingualConceptAligner()
        q = "problema de bloqueo en base de datos"
        res = aligner.align(q)
        print(f"Query: '{q}'")
        print(f"Lang: {res.detected_language}, Normalized: {res.normalized_english_terms}, Conf: {res.confidence}")
    else:
        parser.print_help()
    sys.exit(0)

if __name__ == "__main__":
    main()
