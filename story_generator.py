import random
from templates import templates

def generate_story(keywords):
    if len(keywords) < 3:
        return "Please enter at least three keywords."

    character, place, object_ = keywords[:3]

    template = random.choice(templates)

    return template.format(
        character=character,
        place=place,
        object=object_
    )