"""Tests for story_generator module (V1)."""

import pytest
from src.story_generator import generate_story


class TestGenerateStory:
    """Test cases for generate_story()."""

    def test_valid_3_keywords_returns_string_with_all_keywords(self):
        story = generate_story(["knight", "forest", "sword"])
        assert isinstance(story, str)
        assert "knight" in story
        assert "forest" in story
        assert "sword" in story or "mysterious sword" in story or "ancient sword" in story

    def test_genre_selection_mystery(self):
        story = generate_story(["knight", "forest", "sword"], genre="mystery")
        assert "knight" in story and "forest" in story
        mystery_markers = ["clue", "mystery", "investigate", "disappearance", "unraveled", "truth"]
        assert any(m in story.lower() for m in mystery_markers)

    def test_random_genre_with_none(self):
        story = generate_story(["knight", "forest", "sword"], genre=None)
        assert isinstance(story, str)
        assert len(story) > 0
        assert "knight" in story and "forest" in story

    def test_too_few_keywords_returns_error(self):
        story = generate_story(["knight"])
        assert "at least three" in story.lower() or "three" in story.lower()

    def test_multi_paragraph_output(self):
        story = generate_story(["wizard", "tower", "crystal"], genre="fantasy")
        paragraphs = [p.strip() for p in story.split("\n\n") if p.strip()]
        assert len(paragraphs) >= 2
