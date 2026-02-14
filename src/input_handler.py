"""
Input validation for the Automated Micro Story Generator.
Handles user input for keywords and genre selection.
"""

import re
from .templates import GENRES

MAX_KEYWORD_LENGTH = 50
KEYWORD_PATTERN = re.compile(r"^[a-zA-Z\s\-]+$")


def validate_keywords(keywords: list[str]) -> tuple[bool, str]:
    """
    Validates the keyword list.

    Returns:
        tuple[bool, str]: (is_valid, error_message)
        If valid, error_message is empty string.

    Checks for:
    - Empty input
    - Fewer than 3 keywords
    - Duplicate keywords
    - Unsupported/special characters (only allow letters, spaces, hyphens)
    - Excessively long keywords (cap at 50 chars each)
    """
    if not keywords:
        return False, "Input cannot be empty."

    if len(keywords) < 3:
        return False, "Please enter at least three keywords."

    if len(set(keywords)) != len(keywords):
        return False, "Duplicate keywords are not allowed."

    for kw in keywords[:3]:
        if len(kw) > MAX_KEYWORD_LENGTH:
            return False, f"Keywords must be {MAX_KEYWORD_LENGTH} characters or fewer."

        if not KEYWORD_PATTERN.match(kw):
            return False, "Keywords contain unsupported characters. Only letters, spaces, and hyphens are allowed."

    return True, ""


def parse_keywords(raw_input: str) -> list[str]:
    """
    Parses comma-separated input into a list of trimmed keywords.
    Returns first 3 keywords (or fewer if less provided).
    """
    keywords = [word.strip() for word in raw_input.split(",") if word.strip()]
    return keywords[:3]


def get_user_input() -> dict:
    """
    Prompts user for keywords and genre, returns validated data.

    Returns:
        dict with keys:
        - "keywords": list[str] (validated, first 3)
        - "genre": str or None (None = random)
        - "valid": bool
        - "error": str (empty if valid)
    """
    raw_keywords = input("Enter 3 keywords (character, place, object): ").strip()
    keywords = parse_keywords(raw_keywords)

    is_valid, error = validate_keywords(keywords)
    if not is_valid:
        return {"keywords": keywords, "genre": None, "valid": False, "error": error}

    genre_prompt = (
        f"Choose a genre ({', '.join(GENRES)}, or 'random'): "
    )
    genre_input = input(genre_prompt).strip().lower()

    genre = None
    if genre_input and genre_input != "random":
        if genre_input in GENRES:
            genre = genre_input
        else:
            # Invalid genre: default to random
            genre = None

    return {
        "keywords": keywords,
        "genre": genre,
        "valid": True,
        "error": "",
    }
