"""Tests for input_handler module."""

import pytest
from src.input_handler import validate_keywords, parse_keywords


class TestValidateKeywords:
    """Test cases for validate_keywords()."""

    def test_empty_input(self):
        result, msg = validate_keywords([])
        assert result is False
        assert "empty" in msg.lower()

    def test_whitespace_only(self):
        """Whitespace-only input parses to empty, which is invalid."""
        keywords = parse_keywords("   ")
        result, msg = validate_keywords(keywords)
        assert result is False
        assert "empty" in msg.lower()

    def test_fewer_than_3_keywords(self):
        result, msg = validate_keywords(["knight", "forest"])
        assert result is False
        assert "at least" in msg.lower() and "three" in msg.lower()

    def test_duplicate_keywords(self):
        result, msg = validate_keywords(["knight", "knight", "sword"])
        assert result is False
        assert "duplicate" in msg.lower()

    def test_special_characters(self):
        result, msg = validate_keywords(["knight!", "forest", "sword"])
        assert result is False
        assert "unsupported" in msg.lower() or "character" in msg.lower() or "only contain" in msg.lower()

    def test_special_characters_in_second_keyword(self):
        result, msg = validate_keywords(["knight", "forest", "sw@rd"])
        assert result is False

    def test_valid_input(self):
        result, msg = validate_keywords(["knight", "forest", "sword"])
        assert result is True
        assert msg == ""

    def test_extra_whitespace_trimmmed(self):
        keywords = parse_keywords(" knight , forest , sword ")
        result, msg = validate_keywords(keywords)
        assert result is True
        assert keywords == ["knight", "forest", "sword"]

    def test_more_than_3_keywords_uses_first_3(self):
        keywords = parse_keywords("knight, forest, sword, dragon")
        result, msg = validate_keywords(keywords)
        assert result is True
        assert len(keywords) >= 3

    def test_keyword_too_long(self):
        long_kw = "a" * 51
        result, msg = validate_keywords(["knight", "forest", long_kw])
        assert result is False
        assert "50" in msg or "character" in msg.lower()


class TestParseKeywords:
    """Test cases for parse_keywords()."""

    def test_parses_comma_separated(self):
        assert parse_keywords("knight, forest, sword") == ["knight", "forest", "sword"]

    def test_trims_whitespace(self):
        assert parse_keywords(" knight , forest , sword ") == ["knight", "forest", "sword"]

    def test_returns_first_3_only(self):
        result = parse_keywords("a, b, c, d, e")
        assert result == ["a", "b", "c"]

    def test_allows_hyphens(self):
        result, msg = validate_keywords(["half-elf", "dark-forest", "magic-sword"])
        assert result is True
