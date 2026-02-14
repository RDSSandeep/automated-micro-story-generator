"""
AI-powered story generation via Anthropic Claude API.
Handles API calls, error handling, and prompt construction.
"""

import anthropic
from anthropic import APIConnectionError, APIStatusError, RateLimitError

from .config import ANTHROPIC_API_KEY, AI_MODEL, MAX_TOKENS


def build_prompt(keywords: list[str], genre: str = None) -> str:
    """
    Constructs the prompt for the AI model.

    Args:
        keywords: [character, place, object]
        genre: Optional genre name

    Returns:
        Formatted prompt string
    """
    if len(keywords) < 3:
        return ""

    character, place, object_ = keywords[:3]
    genre_str = genre if genre else "any"

    return f"""Write a short, creative micro story (1-3 paragraphs) using these elements:
- Character: {character}
- Setting: {place}
- Object: {object_}
Genre: {genre_str}

The story should be engaging, vivid, and self-contained.
Only output the story text, nothing else."""


def generate_ai_story(keywords: list[str], genre: str = None) -> str | None:
    """
    Sends keywords to Claude API and returns a generated story.

    Args:
        keywords: List of [character, place, object]
        genre: Optional genre for the story

    Returns:
        Generated story string, or None on error (connection, rate limit, etc.)
    """
    if len(keywords) < 3:
        return None

    if not ANTHROPIC_API_KEY:
        return None

    prompt = build_prompt(keywords, genre)
    if not prompt:
        return None

    try:
        client = anthropic.Anthropic(api_key=ANTHROPIC_API_KEY)
        message = client.messages.create(
            model=AI_MODEL,
            max_tokens=MAX_TOKENS,
            messages=[{"role": "user", "content": prompt}],
        )

        # Extract text from the first content block
        if message.content and len(message.content) > 0:
            text = message.content[0].text
            return text.strip() if text else None
        return None

    except APIConnectionError:
        return None
    except RateLimitError:
        return None
    except APIStatusError:
        return None
    except Exception:
        return None
