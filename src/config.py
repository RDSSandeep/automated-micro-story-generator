"""
Configuration for the Automated Micro Story Generator.
Loads settings from environment variables and .env file.
"""

import os

from dotenv import load_dotenv

load_dotenv()

# Load API key from environment variable
ANTHROPIC_API_KEY = os.environ.get("ANTHROPIC_API_KEY", "")

# Model settings
AI_MODEL = "claude-sonnet-4-5"
MAX_TOKENS = 500

# Mode
DEFAULT_MODE = "template"  # "template" or "ai"
