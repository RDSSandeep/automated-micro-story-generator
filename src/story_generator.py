"""
Story generation for the Automated Micro Story Generator.
Supports template mode (V1) and AI mode (V2) with fallback.
"""

import random
from .templates import templates, GENRES
from .ai_generator import generate_ai_story

# Adjective pools for randomized variation before {object}
OBJECT_ADJECTIVES = ["mysterious", "ancient", "forgotten", "gleaming", "strange", "legendary"]


def generate_story(
    keywords: list[str],
    genre: str = None,
    mode: str = "template",
) -> str:
    """
    Main entry point for story generation.

    Args:
        keywords: List of [character, place, object]
        genre: Genre name or None for random
        mode: "template" for V1, "ai" for V2 (falls back to template on failure)

    Returns:
        Generated story string
    """
    if mode == "ai":
        try:
            story = generate_ai_story(keywords, genre)
            if story:
                return story
        except Exception:
            pass
        # Fallback to template mode
        print("(AI unavailable — falling back to template mode)")

    return generate_template_story(keywords, genre)


def generate_template_story(keywords: list[str], genre: str = None) -> str:
    """
    Generate a multi-paragraph micro story from templates (V1 logic).

    Args:
        keywords: List of [character, place, object]
        genre: Genre name (adventure, mystery, fantasy, sci-fi, comedy) or None for random.

    Returns:
        Generated story string, or error message if invalid input.
    """
    if len(keywords) < 3:
        return "Please enter at least three keywords."

    character, place, object_ = keywords[:3]

    # Select genre
    selected_genre = genre if genre and genre in templates else random.choice(GENRES)
    genre_templates = templates[selected_genre]

    # Build multi-paragraph story
    paragraphs = []

    # Opening
    opening = random.choice(genre_templates["opening"])
    paragraphs.append(_format_template(opening, character, place, object_))

    # Middle
    middle = random.choice(genre_templates["middle"])
    paragraphs.append(_format_template(middle, character, place, object_))

    # Ending
    ending = random.choice(genre_templates["ending"])
    paragraphs.append(_format_template(ending, character, place, object_))

    return "\n\n".join(paragraphs)


def _format_template(template: str, character: str, place: str, object_: str) -> str:
    """
    Format a template with optional adjective variation before the object.
    """
    # 50% chance to add an adjective before the object
    if random.choice([True, False]):
        adj = random.choice(OBJECT_ADJECTIVES)
        object_display = f"{adj} {object_}"
    else:
        object_display = object_

    return template.format(
        character=character,
        place=place,
        object=object_display,
    )
