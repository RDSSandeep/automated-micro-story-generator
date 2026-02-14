"""
Template-based story generation for the Automated Micro Story Generator (V1).
"""

import random
from .templates import templates, GENRES

OBJECT_ADJECTIVES = ["mysterious", "ancient", "forgotten", "gleaming", "strange", "legendary"]


def generate_story(keywords: list[str], genre: str = None) -> str:
    """Generate a multi-paragraph micro story from templates."""
    if len(keywords) < 3:
        return "Please enter at least three keywords."

    character, place, object_ = keywords[:3]
    selected_genre = genre if genre and genre in templates else random.choice(GENRES)
    genre_templates = templates[selected_genre]

    paragraphs = []
    opening = random.choice(genre_templates["opening"])
    paragraphs.append(_format_template(opening, character, place, object_))
    middle = random.choice(genre_templates["middle"])
    paragraphs.append(_format_template(middle, character, place, object_))
    ending = random.choice(genre_templates["ending"])
    paragraphs.append(_format_template(ending, character, place, object_))

    return "\n\n".join(paragraphs)


def _format_template(template: str, character: str, place: str, object_: str) -> str:
    if random.choice([True, False]):
        adj = random.choice(OBJECT_ADJECTIVES)
        object_display = f"{adj} {object_}"
    else:
        object_display = object_
    return template.format(character=character, place=place, object=object_display)
