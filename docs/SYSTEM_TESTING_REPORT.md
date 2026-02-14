# System Testing Report

**Automated Micro Story Generator**  
**CISC 594 — Software Engineering**  
**Team:** Dhruv Sharma, Durga Sai Sandeep Rayapureddy, Isit Pokharel, Tan Nguyen

---

## 1. Test Environment

| Component | Version / Details |
|-----------|-------------------|
| **Operating System** | macOS (darwin) |
| **Python Version** | 3.10.8 |
| **Test Framework** | pytest 9.0.2 |
| **Test Execution** | `pytest tests/ -v --tb=short` |

### Dependencies

| Package | Version |
|---------|---------|
| anthropic | 0.79.0 |
| python-dotenv | (from requirements) |
| pytest | 9.0.2 |
| pluggy | 1.6.0 |

*Full dependency tree available via `pip list` in project `.venv`.*

---

## 2. Test Cases Summary

| Module | Test Count | Passed | Failed |
|--------|------------|--------|--------|
| test_ai_generator | 10 | 10 | 0 |
| test_input_handler | 14 | 14 | 0 |
| test_story_generator | 8 | 8 | 0 |
| test_templates | 5 | 5 | 0 |
| **Total** | **37** | **37** | **0** |

---

## 3. Test Cases Table

### 3.1 AI Generator (`test_ai_generator.py`)

| ID | Description | Input | Expected Output | Actual Output | Pass/Fail |
|----|-------------|-------|------------------|---------------|-----------|
| AI-01 | Prompt contains all keywords | `build_prompt(["knight", "forest", "sword"])` | Prompt includes knight, forest, sword | Prompt includes all three | PASS |
| AI-02 | Prompt contains genre when provided | `build_prompt(..., genre="mystery")` | Prompt includes "mystery" | Prompt includes "mystery" | PASS |
| AI-03 | Prompt contains "any" when genre is None | `build_prompt(..., genre=None)` | Prompt includes "any" | Prompt includes "any" | PASS |
| AI-04 | Empty keywords returns empty string | `build_prompt([])` | `""` | `""` | PASS |
| AI-05 | Valid API call returns story | `generate_ai_story(["knight", "forest", "sword"])` (mocked) | Non-empty story string | "A knight ventured into the forest." | PASS |
| AI-06 | API connection error returns None | Simulated connection failure | `None` | `None` | PASS |
| AI-07 | Rate limit / generic error returns None | Simulated exception | `None` | `None` | PASS |
| AI-08 | Empty keywords returns None | `generate_ai_story([])` | `None` | `None` | PASS |
| AI-09 | Fewer than 3 keywords returns None | `generate_ai_story(["knight", "forest"])` | `None` | `None` | PASS |
| AI-10 | No API key returns None | `ANTHROPIC_API_KEY=""` | `None` | `None` | PASS |

### 3.2 Input Handler (`test_input_handler.py`)

| ID | Description | Input | Expected Output | Actual Output | Pass/Fail |
|----|-------------|-------|------------------|---------------|-----------|
| IH-01 | Empty input | `validate_keywords([])` | Invalid, "empty" error | Invalid, "empty" error | PASS |
| IH-02 | Whitespace only | `parse_keywords("   ")` then validate | Invalid, "empty" error | Invalid, "empty" error | PASS |
| IH-03 | Fewer than 3 keywords | `validate_keywords(["knight", "forest"])` | Invalid, "at least three" | Invalid, "Please enter at least three keywords." | PASS |
| IH-04 | Duplicate keywords | `validate_keywords(["knight", "knight", "sword"])` | Invalid, "duplicate" | Invalid, "duplicate" error | PASS |
| IH-05 | Special characters | `validate_keywords(["knight!", "forest", "sword"])` | Invalid, unsupported chars | Invalid, unsupported characters | PASS |
| IH-06 | Special characters in second keyword | `validate_keywords(["knight", "forest", "sw@rd"])` | Invalid | Invalid | PASS |
| IH-07 | Valid input | `validate_keywords(["knight", "forest", "sword"])` | Valid | Valid | PASS |
| IH-08 | Extra whitespace trimmed | `parse_keywords(" knight , forest , sword ")` | `["knight", "forest", "sword"]` | Keywords trimmed correctly | PASS |
| IH-09 | More than 3 keywords | `validate_keywords(parse_keywords("knight, forest, sword, dragon"))` | Valid, uses first 3 | Valid | PASS |
| IH-10 | Keyword too long (>50 chars) | `validate_keywords(["knight", "forest", "a"*51])` | Invalid | Invalid, 50-char limit | PASS |
| IH-11 | Parse comma-separated | `parse_keywords("knight, forest, sword")` | `["knight", "forest", "sword"]` | Correct list | PASS |
| IH-12 | Trims whitespace | `parse_keywords(" knight , forest , sword ")` | Trimmed keywords | Correct | PASS |
| IH-13 | Returns first 3 only | `parse_keywords("a, b, c, d, e")` | `["a", "b", "c"]` | Correct | PASS |
| IH-14 | Allows hyphens | `validate_keywords(["half-elf", "dark-forest", "magic-sword"])` | Valid | Valid | PASS |

### 3.3 Story Generator (`test_story_generator.py`)

| ID | Description | Input | Expected Output | Actual Output | Pass/Fail |
|----|-------------|-------|------------------|---------------|-----------|
| SG-01 | Valid 3 keywords returns story | `generate_story(["knight", "forest", "sword"])` | String with all keywords | Story contains knight, forest, sword | PASS |
| SG-02 | Genre selection (mystery) | `generate_story(..., genre="mystery")` | Story from mystery genre | Contains mystery markers (clue, mystery, etc.) | PASS |
| SG-03 | Random genre with None | `generate_story(..., genre=None)` | Valid story | Valid story returned | PASS |
| SG-04 | Too few keywords | `generate_story(["knight"])` | Error message with "three" | "Please enter at least three keywords." | PASS |
| SG-05 | Multi-paragraph output | `generate_story(["wizard", "tower", "crystal"], genre="fantasy")` | ≥2 paragraphs | 3 paragraphs | PASS |
| SG-06 | Template mode | `generate_story(..., mode="template")` | Template-based story | Template story with keywords | PASS |
| SG-07 | AI mode success | `generate_story(..., mode="ai")` (mocked success) | AI story | "An AI-generated tale of a knight." | PASS |
| SG-08 | AI mode fallback | `generate_story(..., mode="ai")` (mocked failure) | Template story fallback | Template story returned | PASS |

### 3.4 Templates (`test_templates.py`)

| ID | Description | Input | Expected Output | Actual Output | Pass/Fail |
|----|-------------|-------|------------------|---------------|-----------|
| TM-01 | All genres exist | Inspect `templates` dict | Keys: adventure, mystery, fantasy, sci-fi, comedy | All present | PASS |
| TM-02 | All templates have placeholders | Each template | `{character}`, `{place}`, `{object}` | All contain placeholders | PASS |
| TM-03 | No empty genre lists | Each genre's opening/middle/ending | ≥2 templates each | All have ≥2 | PASS |
| TM-04 | All templates are formattable | `tmpl.format(character="X", place="Y", object="Z")` | Result contains X, Y, Z | All format correctly | PASS |
| TM-05 | GENRES list matches | `GENRES` | Same as template keys | Matches | PASS |

---

## 4. Summary of Results

- **Total test cases:** 37  
- **Passed:** 37  
- **Failed:** 0  
- **Success rate:** 100%

All tests pass for both **Version 1 (template-based)** and **Version 2 (AI-enhanced)** functionality. The test suite covers:

- Input validation (keywords, genres, edge cases)
- Template-based story generation (all genres, multi-paragraph)
- AI generation (prompt building, API mocking, error handling, fallback)
- Template structure and formattability

---

## 5. Bugs Found and Fixes

**No bugs were discovered during system testing.** All test cases passed on first execution after implementation.

During earlier development, the following were addressed:

- **Template placeholders:** Some middle/ending templates initially lacked `{character}`, `{place}`, or `{object}`. These were updated so every template includes all three placeholders for consistency and correct formatting.
- **AI generator tests:** Anthropic SDK exception constructors differ from standard Python exceptions. Tests were adjusted to use `ConnectionError` and generic `Exception` for mocking API failures, ensuring robust error-handling coverage without SDK-specific constructor requirements.

---

## 6. Raw Test Output

```
$ pytest tests/ -v --tb=short
============================= test session starts ==============================
platform darwin -- Python 3.10.8, pytest-9.0.2, pluggy-1.6.0
rootdir: /Users/isit/automated-micro-story-generator
collected 37 items

tests/test_ai_generator.py ..........
tests/test_input_handler.py ..............
tests/test_story_generator.py ........
tests/test_templates.py .....

============================== 37 passed in 0.23s ===============================
```

*Full output saved to `test_results.txt` in the project root.*
