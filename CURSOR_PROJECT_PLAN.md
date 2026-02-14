# Automated Micro Story Generator — Full Build Plan

## PROJECT CONTEXT

This is a university software engineering project (CISC 594). The deliverables are:
1. Working software with two versioned releases (V1 and V2)
2. A Risk Management Report (already written)
3. A Configuration Management Report
4. A System Testing Report (for both versions)
5. A group presentation

Team: Dhruv Sharma, Durga Sai Sandeep Rayapureddy, Isit Pokharel, Tan Nguyen

**This plan focuses on the software build. Follow it step by step.**

---

## CURRENT STATE OF THE CODE

Three files exist:
- `main.py` — CLI entry point, takes 3 comma-separated keywords, validates input
- `story_generator.py` — picks a random template and fills in keywords
- `templates.py` — 4 hardcoded story templates

The code works but is bare-bones. It needs to be expanded for a proper V1, then V2 needs to be built on top.

---

## PHASE 1: EXPAND AND POLISH VERSION 1 (Template-Based)

### 1.1 Project Structure

Reorganize the repo into this structure:

```
automated-micro-story-generator/
├── README.md
├── requirements.txt
├── .gitignore
├── src/
│   ├── __init__.py
│   ├── main.py
│   ├── story_generator.py
│   ├── templates.py
│   └── input_handler.py
├── tests/
│   ├── __init__.py
│   ├── test_story_generator.py
│   ├── test_input_handler.py
│   └── test_templates.py
└── docs/
    └── (reports go here later)
```

### 1.2 Expand `templates.py`

- Increase templates from 4 to at least **10-12** templates
- Organize templates by **genre** (adventure, mystery, fantasy, sci-fi, comedy)
- Structure should be a dictionary keyed by genre:

```python
templates = {
    "adventure": [
        "Once upon a time, a {character} found a {object} in a {place}. ...",
        ...
    ],
    "mystery": [...],
    "fantasy": [...],
    "sci-fi": [...],
    "comedy": [...]
}
```

### 1.3 Expand `story_generator.py`

Upgrade the generator to support:
- **Genre selection**: User can optionally pick a genre, or it defaults to random
- **Multi-paragraph output**: Each story should be 1-3 short paragraphs, not just one sentence. Use multiple templates chained together (an opening, a middle, and an ending template) to build a mini narrative arc
- **Randomized variation**: Add synonym/adjective pools so that even the same template produces slightly different text each run (e.g., "mysterious" / "ancient" / "forgotten" before `{object}`)

Function signature:
```python
def generate_story(keywords: list[str], genre: str = None) -> str:
```

### 1.4 Create `input_handler.py`

Extract all input validation into its own module with these functions:

```python
def get_user_input() -> dict:
    """Prompts user and returns validated keywords + options."""

def validate_keywords(keywords: list[str]) -> tuple[bool, str]:
    """
    Returns (is_valid, error_message).
    Checks for:
    - Empty input
    - Fewer than 3 keywords
    - Duplicate keywords
    - Unsupported/special characters (only allow letters, spaces, hyphens)
    - Excessively long keywords (cap at 50 chars each)
    """
```

### 1.5 Update `main.py`

Rewrite as a clean CLI app:
- Use `input_handler.py` for all input
- Let user choose a genre (or type "random")
- Display the generated story
- Ask if they want to generate another story (loop) or quit
- Wrap everything in a `main()` function with `if __name__ == "__main__":`

### 1.6 Write Unit Tests for V1

Use `pytest`. Create tests in the `tests/` folder:

**`test_input_handler.py`:**
| Test Case | Input | Expected Result |
|---|---|---|
| Empty input | `""` | Returns invalid, "empty" error |
| Whitespace only | `"   "` | Returns invalid, "empty" error |
| Fewer than 3 keywords | `"knight, forest"` | Returns invalid, "at least 3" error |
| Duplicate keywords | `"knight, knight, sword"` | Returns invalid, "duplicate" error |
| Special characters | `"knight!, forest, sw@rd"` | Returns invalid, "unsupported characters" error |
| Valid input | `"knight, forest, sword"` | Returns valid |
| Extra whitespace | `" knight , forest , sword "` | Returns valid, trimmed keywords |
| More than 3 keywords | `"knight, forest, sword, dragon"` | Returns valid, uses first 3 |

**`test_story_generator.py`:**
| Test Case | Input | Expected Result |
|---|---|---|
| Valid 3 keywords | `["knight", "forest", "sword"]` | Returns a string containing all 3 keywords |
| Genre selection | `["knight", "forest", "sword"], genre="mystery"` | Returns story from mystery templates |
| Random genre | `["knight", "forest", "sword"], genre=None` | Returns a valid story |
| Too few keywords | `["knight"]` | Returns error message |

**`test_templates.py`:**
| Test Case | Expected Result |
|---|---|
| All genres exist | templates dict has all expected genre keys |
| All templates are formattable | Each template has {character}, {place}, {object} placeholders |
| No empty genre lists | Every genre has at least 2 templates |

### 1.7 `requirements.txt` for V1

```
pytest>=7.0
```

(No external dependencies needed for V1 — it's pure Python.)

### 1.8 Git Workflow for V1

1. Create a `develop` branch from `main`
2. Create a feature branch `feature/v1-template-engine` from `develop`
3. Make all V1 changes on the feature branch
4. When complete, merge `feature/v1-template-engine` → `develop`
5. Run all tests on `develop`
6. When all tests pass, merge `develop` → `main`
7. Tag the release: `git tag -a v1.0 -m "Version 1.0: Template-based story generator"`
8. Push the tag: `git push origin v1.0`

---

## PHASE 2: BUILD VERSION 2 (AI-Enhanced Story Generation)

### 2.1 Choose Option A: AI-Driven Generation via Anthropic Claude API

This is the simpler and more impressive path. The user provides keywords, and the system calls the Claude API to generate a creative, multi-paragraph story.

### 2.2 New Files and Changes

Add these files:

```
src/
├── ai_generator.py      # NEW — handles Claude API calls
├── config.py             # NEW — API key and settings management
├── story_generator.py    # MODIFIED — add mode switching (template vs AI)
├── main.py               # MODIFIED — add mode selection
```

### 2.3 Create `config.py`

```python
import os

# Load API key from environment variable
ANTHROPIC_API_KEY = os.environ.get("ANTHROPIC_API_KEY", "")

# Model settings
AI_MODEL = "claude-sonnet-4-5-20250514"
MAX_TOKENS = 500

# Mode
DEFAULT_MODE = "template"  # "template" or "ai"
```

### 2.4 Create `ai_generator.py`

This is the core new module. It should:

```python
import anthropic
from config import ANTHROPIC_API_KEY, AI_MODEL, MAX_TOKENS

def generate_ai_story(keywords: list[str], genre: str = None) -> str:
    """
    Sends keywords to Claude API and returns a generated story.
    
    - Build a prompt that instructs Claude to write a 1-3 paragraph 
      micro story using the given keywords
    - If genre is provided, include it in the prompt
    - Handle API errors gracefully
    - Return the story text
    """

def build_prompt(keywords: list[str], genre: str = None) -> str:
    """
    Constructs the prompt for the AI model.
    
    Example prompt:
    "Write a short, creative micro story (1-3 paragraphs) using these elements:
     - Character: {keywords[0]}
     - Setting: {keywords[1]}  
     - Object: {keywords[2]}
     Genre: {genre if provided, else 'any'}
     
     The story should be engaging, vivid, and self-contained. 
     Only output the story text, nothing else."
    """
```

**Error handling is critical here.** Wrap the API call in try/except:
- `anthropic.APIConnectionError` → return fallback message
- `anthropic.RateLimitError` → return fallback message  
- `anthropic.APIStatusError` → return fallback message
- Any exception → fall back to template-based generation (this is the "fallback logic" mentioned in the risk management report under R6)

### 2.5 Modify `story_generator.py`

Add a unified interface:

```python
from ai_generator import generate_ai_story
# ... existing template imports ...

def generate_story(keywords: list[str], genre: str = None, mode: str = "template") -> str:
    """
    Main entry point for story generation.
    
    mode="template" → uses template engine (V1)
    mode="ai" → uses Claude API (V2), falls back to template on failure
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
    # (existing V1 logic, renamed)
```

### 2.6 Modify `main.py`

Update the main loop to:
1. Ask user to choose mode: **Template** or **AI-Powered**
2. Ask for keywords (same as before)
3. Ask for genre (same as before)
4. Call `generate_story()` with the selected mode
5. Display the result
6. Ask to generate again or quit

### 2.7 Update `requirements.txt`

```
pytest>=7.0
anthropic>=0.40.0
python-dotenv>=1.0.0
```

### 2.8 Add `.env` support (optional but recommended)

Create a `.env.example` file:
```
ANTHROPIC_API_KEY=your-api-key-here
```

Update `config.py` to use `python-dotenv` to load from `.env`.

### 2.9 Write Unit Tests for V2

**`test_ai_generator.py`:**
| Test Case | Description | Expected Result |
|---|---|---|
| Valid API call | Mock a successful API response | Returns a non-empty story string |
| API connection error | Mock a connection failure | Returns None or fallback message |
| Rate limit error | Mock rate limit | Returns None or fallback message |
| Empty keywords | Pass empty list | Returns error message |
| Prompt construction | Check build_prompt output | Prompt contains all keywords and genre |

**`test_story_generator.py` (updated):**
| Test Case | Description | Expected Result |
|---|---|---|
| Template mode | `mode="template"` | Returns template-based story |
| AI mode success | `mode="ai"` with mocked success | Returns AI story |
| AI mode fallback | `mode="ai"` with mocked failure | Falls back to template story |

**Use `unittest.mock.patch` to mock the Anthropic API calls in tests so they don't require a real API key.**

### 2.10 Git Workflow for V2

1. Create feature branch `feature/v2-ai-generation` from `develop`
2. Make all V2 changes on the feature branch
3. When complete, merge `feature/v2-ai-generation` → `develop`
4. Run ALL tests (V1 + V2) on `develop`
5. When all tests pass, merge `develop` → `main`
6. Tag the release: `git tag -a v2.0 -m "Version 2.0: AI-enhanced story generation"`
7. Push the tag: `git push origin v2.0`

---

## PHASE 3: SYSTEM TESTING (both versions)

Run and document all tests with:

```bash
pytest tests/ -v --tb=short > test_results.txt
```

For the system testing report, document:
- Test environment (Python version, OS, dependencies)
- Test cases table (ID, description, input, expected output, actual output, pass/fail)
- Summary of results
- Any bugs found and how they were fixed

---

## PHASE 4: DOCUMENTATION

### 4.1 Update `README.md`

Include:
- Project description
- Setup instructions (clone, install dependencies, set API key)
- How to run V1 (template mode)
- How to run V2 (AI mode)
- How to run tests
- Team members

### 4.2 Configuration Management Report

Document:
- Version control system used (Git/GitHub)
- Branching strategy (`main` → `develop` → `feature/*`)
- Change control process (feature branches, code review, merge to develop, test, merge to main)
- Release tagging (v1.0, v2.0)
- Screenshots of Git log, branches, tags, and merge history

### 4.3 Presentation

5 sections (assign to team members):
1. Project intro and features (what it does, demo)
2. Roles of each member (who built what)
3. Risk identification and tracking (from risk report)
4. Configuration management approach (from CM report)
5. System testing approach and results (from test report)

---

## SUMMARY — EXECUTION ORDER

```
Step 1: Restructure the project into the folder layout above
Step 2: Expand templates.py with genres and more templates
Step 3: Create input_handler.py with full validation
Step 4: Upgrade story_generator.py for genre support and multi-paragraph output
Step 5: Rewrite main.py as a clean CLI loop
Step 6: Write all V1 tests → run them → fix any failures
Step 7: Git: branch, commit, merge, tag v1.0
Step 8: Create config.py and ai_generator.py
Step 9: Modify story_generator.py to support AI mode with fallback
Step 10: Update main.py with mode selection
Step 11: Write all V2 tests (with mocked API) → run them → fix any failures
Step 12: Git: branch, commit, merge, tag v2.0
Step 13: Run full test suite, capture results
Step 14: Update README.md
Step 15: Write configuration management report
```
