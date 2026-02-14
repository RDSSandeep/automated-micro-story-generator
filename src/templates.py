"""
Story templates organized by genre.
Each genre has opening, middle, and ending templates for multi-paragraph narratives.
All templates use {character}, {place}, and {object} placeholders.
"""

templates = {
    "adventure": {
        "opening": [
            "Once upon a time, a {character} set out on a quest into the {place}, seeking a legendary {object}.",
            "A {character} ventured deep into the {place}, where rumor spoke of a powerful {object}.",
        ],
        "middle": [
            "As they pressed onward, the {character} faced trials that tested their resolve. The {place} seemed to come alive around them, and thoughts of the {object} kept them going.",
            "The journey through the {place} was treacherous, but the {character} pressed on, driven by the hope of finding the {object}.",
        ],
        "ending": [
            "At last, the {character} discovered the {object} gleaming in a hidden grove of the {place}. Their adventure had only just begun.",
            "With the {object} finally in their grasp, the {character} knew the {place} would forever hold a special place in their heart.",
        ],
    },
    "mystery": {
        "opening": [
            "In the heart of the {place}, a {character} stumbled upon a clue connected to a vanished {object}.",
            "The {character} had come to the {place} to investigate the strange disappearance of a {object}.",
        ],
        "middle": [
            "Piece by piece, the {character} unraveled the mystery. The {place} held secrets about the missing {object} that had been buried for decades.",
            "Every corner of the {place} seemed to whisper hints. The {character} followed the trail, each clue leading closer to the {object}.",
        ],
        "ending": [
            "The truth emerged at last: the {object} had been hidden in plain sight in the {place} all along. The {character} smiled, case closed.",
            "Mystery solved. The {character} stood in the {place}, the {object} finally returned to its rightful place.",
        ],
    },
    "fantasy": {
        "opening": [
            "Long ago, a {character} guarded a magical {object} hidden deep within the enchanted {place}.",
            "In the mystical {place}, there lived a {character} who dreamed of wielding a legendary {object}.",
        ],
        "middle": [
            "Magic flowed through the {place} like a river of light. The {character} felt the presence of the {object} calling to them.",
            "The {place} was a realm of wonder, where the ordinary rules did not apply. The {character} drew closer to the fabled {object}.",
        ],
        "ending": [
            "With a burst of enchantment, the {character} claimed the {object}. The {place} sang with ancient power.",
            "The {object} shimmered in the {character}'s hands. In the heart of the {place}, a new legend was born.",
        ],
    },
    "sci-fi": {
        "opening": [
            "On a distant colony in the {place}, a {character} discovered a prototype {object} of unknown origin.",
            "The {character} had been assigned to the {place} research station to analyze an anomalous {object}.",
        ],
        "middle": [
            "The {character} studied the readings. The {place} hummed with energy that defied known physics. The {object} pulsed with an inner light.",
            "The {character} ran simulations in the lab. The {place} stretched across the viewscreen—and the {object} held the key to everything.",
        ],
        "ending": [
            "The {character} activated the {object}. The {place} transformed, reality bending to its design. A new era had begun.",
            "With the {object} now understood, the {character} transmitted their findings from the {place}. Mankind would never be the same.",
        ],
    },
    "comedy": {
        "opening": [
            "A {character} walked into the {place} and somehow managed to trip over a very inconvenient {object}.",
            "The {character} had one job: deliver a {object} to the {place}. It did not go as planned.",
        ],
        "middle": [
            "Chaos ensued. The {place} became a scene of slapstick disaster as the {character} tried—and failed—to get a grip on the situation. And the {object}.",
            "Every attempt to fix things made them worse. The {character} wondered how a simple {object} in a simple {place} could cause such havoc.",
        ],
        "ending": [
            "In the end, the {character} sat in the {place}, covered in chaos, holding the {object}. At least they had a story to tell.",
            "Somehow, against all odds, the {character} succeeded. The {place} was a mess, but the {object} was exactly where it needed to be. Sort of.",
        ],
    },
}

# Flat list of all genres for random selection
GENRES = list(templates.keys())
