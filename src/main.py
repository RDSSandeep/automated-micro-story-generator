"""
CLI entry point for the Automated Micro Story Generator (V1).
"""

from .input_handler import get_user_input
from .story_generator import generate_story


def main() -> None:
    """Run the story generator in a loop."""
    print("Welcome to the Automated Micro Story Generator!\n")

    while True:
        result = get_user_input()

        if not result["valid"]:
            print(f"Error: {result['error']}\n")
            continue

        story = generate_story(result["keywords"], result["genre"])
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
