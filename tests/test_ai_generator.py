"""Tests for ai_generator module. Uses mocks to avoid real API calls."""

import pytest
from unittest.mock import patch, MagicMock

from src.ai_generator import build_prompt, generate_ai_story


class TestBuildPrompt:
    """Test cases for build_prompt()."""

    def test_prompt_contains_all_keywords(self):
        prompt = build_prompt(["knight", "forest", "sword"])
        assert "knight" in prompt
        assert "forest" in prompt
        assert "sword" in prompt

    def test_prompt_contains_genre_when_provided(self):
        prompt = build_prompt(["knight", "forest", "sword"], genre="mystery")
        assert "mystery" in prompt

    def test_prompt_contains_any_when_genre_none(self):
        prompt = build_prompt(["knight", "forest", "sword"], genre=None)
        assert "any" in prompt

    def test_empty_keywords_returns_empty_string(self):
        prompt = build_prompt([])
        assert prompt == ""


class TestGenerateAiStory:
    """Test cases for generate_ai_story(). Uses mocked API."""

    @patch("anthropic.Anthropic")
    def test_valid_api_call_returns_story(self, mock_anthropic_class):
        mock_client = MagicMock()
        mock_response = MagicMock()
        mock_response.content = [MagicMock(text="A knight ventured into the forest.\n")]
        mock_client.messages.create.return_value = mock_response
        mock_anthropic_class.return_value = mock_client

        with patch("src.ai_generator.ANTHROPIC_API_KEY", "test-key"):
            story = generate_ai_story(["knight", "forest", "sword"])

        assert story == "A knight ventured into the forest."
        mock_client.messages.create.assert_called_once()

    @patch("anthropic.Anthropic")
    def test_api_connection_error_returns_none(self, mock_anthropic_class):
        mock_client = MagicMock()
        mock_client.messages.create.side_effect = ConnectionError("Connection failed")

        mock_anthropic_class.return_value = mock_client

        with patch("src.ai_generator.ANTHROPIC_API_KEY", "test-key"):
            story = generate_ai_story(["knight", "forest", "sword"])

        assert story is None

    @patch("anthropic.Anthropic")
    def test_rate_limit_error_returns_none(self, mock_anthropic_class):
        mock_client = MagicMock()
        mock_client.messages.create.side_effect = Exception("Rate limited")

        mock_anthropic_class.return_value = mock_client

        with patch("src.ai_generator.ANTHROPIC_API_KEY", "test-key"):
            story = generate_ai_story(["knight", "forest", "sword"])

        assert story is None

    def test_empty_keywords_returns_none(self):
        story = generate_ai_story([])
        assert story is None

    def test_fewer_than_3_keywords_returns_none(self):
        story = generate_ai_story(["knight", "forest"])
        assert story is None

    @patch("src.ai_generator.ANTHROPIC_API_KEY", "")
    def test_no_api_key_returns_none(self):
        story = generate_ai_story(["knight", "forest", "sword"])
        assert story is None
