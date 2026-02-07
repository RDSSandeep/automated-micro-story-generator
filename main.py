from story_generator import generate_story

print("Welcome to the Automated Micro Story Generator!")

user_input = input("Enter 3 keywords (character, place, object): ")

if not user_input.strip():
    print("Error: Input cannot be empty.")
    exit()

keywords = [word.strip() for word in user_input.split(",") if word.strip()]

if len(set(keywords)) != len(keywords):
    print("Error: Duplicate keywords are not allowed.")
    exit()

story = generate_story(keywords)

print("\nGenerated Story:\n")
print(story)