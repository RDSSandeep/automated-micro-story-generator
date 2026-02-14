"""
CLI entry point for the Automated Micro Story Generator.
"""

from .input_handler import get_user_input
from .story_generator import generate_story


def _get_mode() -> str:
    """Prompt user for generation mode. Returns 'template' or 'ai'."""
    while True:
        choice = input("Choose mode: Template or AI-Powered (t/ai): ").strip().lower()
        if choice in ("t", "template"):
            return "template"
        if choice in ("ai", "a"):
            return "ai"
        print("Invalid choice. Enter 't' for Template or 'ai' for AI-Powered.\n")


def main() -> None:
    """Run the story generator in a loop."""
    print("Welcome to the Automated Micro Story Generator!\n")

    while True:
        mode = _get_mode()
        result = get_user_input()

        if not result["valid"]:
            print(f"Error: {result['error']}\n")
            continue

        story = generate_story(
            result["keywords"],
            result["genre"],
            mode=mode,
        )
        print("\nGenerated Story:\n")
        print(story)
        print()

        again = input("Generate another story? (y/n): ").strip().lower()
        if again not in ("y", "yes"):
            print("Thanks for using the Automated Micro Story Generator. Goodbye!")
            break
        print()


if __name__ == "__main__":
    main()
