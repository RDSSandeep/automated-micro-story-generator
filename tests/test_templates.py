"""Tests for templates module."""

import pytest
from src.templates import templates, GENRES


EXPECTED_GENRES = ["adventure", "mystery", "fantasy", "sci-fi", "comedy"]


class TestTemplatesStructure:
    """Test cases for templates dict structure."""

    def test_all_genres_exist(self):
        for genre in EXPECTED_GENRES:
            assert genre in templates, f"Missing genre: {genre}"

    def test_all_templates_have_placeholders(self):
        for genre, parts in templates.items():
            for part_name, part_templates in parts.items():
                assert part_name in ("opening", "middle", "ending")
                for tmpl in part_templates:
                    assert "{character}" in tmpl, f"{genre}/{part_name}: missing {{character}}"
                    assert "{place}" in tmpl, f"{genre}/{part_name}: missing {{place}}"
                    assert "{object}" in tmpl, f"{genre}/{part_name}: missing {{object}}"

    def test_no_empty_genre_lists(self):
        for genre, parts in templates.items():
            assert "opening" in parts and len(parts["opening"]) >= 2
            assert "middle" in parts and len(parts["middle"]) >= 2
            assert "ending" in parts and len(parts["ending"]) >= 2

    def test_all_templates_are_formattable(self):
        for genre, parts in templates.items():
            for part_name, part_templates in parts.items():
                for tmpl in part_templates:
                    result = tmpl.format(character="X", place="Y", object="Z")
                    assert "X" in result and "Y" in result and "Z" in result

    def test_genres_list_matches(self):
        assert set(GENRES) == set(EXPECTED_GENRES)
