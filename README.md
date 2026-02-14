# Automated Micro Story Generator (V1)

A CLI application that generates short micro stories from three keywords: **character**, **place**, and **object**.

**Team:** Dhruv Sharma, Durga Sai Sandeep Rayapureddy, Isit Pokharel, Tan Nguyen

## Features

- Multi-paragraph stories from genre-specific templates (adventure, mystery, fantasy, sci-fi, comedy)
- Genre selection or random
- Input validation for keywords

## Setup

```bash
git clone <repo-url>
cd automated-micro-story-generator
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## Running

```bash
python run.py
```

Enter three comma-separated keywords, choose a genre (or "random"), and receive your story.

## Tests

```bash
pytest tests/ -v
```
