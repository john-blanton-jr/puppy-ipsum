import random
import logging
from .data_loader import load_data
import traceback

data, quotes = load_data()


def generate_sentence() -> str:
    try:
        structure = random.choice(
            [
                lambda: f"The {random.choice(data['adjectives'])} {random.choice(data['nouns'])} {random.choice(data['verbs'])} without hesitation.",
                lambda: f"Once upon a time, a {random.choice(data['nouns'])} {random.choice(data['verbs'])} {random.choice(data['conjunctions'])} {random.choice(data['verbs'])}.",
                lambda: f"In a galaxy far, far away, a {random.choice(data['nouns'])} {random.choice(data['verbs'])} {random.choice(data['conjunctions'])} {random.choice(data['verbs'])}.",
                lambda: f"The {random.choice(data['nouns'])} {random.choice(data['verbs'])} {random.choice(data['conjunctions'])} then it {random.choice(data['verbs'])}.",
                lambda: f"A {random.choice(data['adjectives'])} {random.choice(data['nouns'])} {random.choice(data['verbs'])} in the moonlight.",
                lambda: f"The {random.choice(data['nouns'])} {random.choice(data['verbs'])} {random.choice(data['conjunctions'])} suddenly {random.choice(data['verbs'])}.",
                lambda: f"Once in a blue moon, a {random.choice(data['nouns'])} {random.choice(data['verbs'])} {random.choice(data['conjunctions'])} {random.choice(data['verbs'])}.",
                lambda: f"A {random.choice(data['adjectives'])} {random.choice(data['nouns'])} {random.choice(data['verbs'])} {random.choice(data['conjunctions'])} then {random.choice(data['verbs'])}.",
                lambda: f"The {random.choice(data['nouns'])} {random.choice(data['verbs'])} while humming a {random.choice(data['nouns'])}.",
                lambda: f"In a quiet village, a {random.choice(data['nouns'])} {random.choice(data['verbs'])} every morning.",
                lambda: f"The {random.choice(data['nouns'])} {random.choice(data['verbs'])} {random.choice(data['conjunctions'])} burst into laughter.",
                lambda: f"A {random.choice(data['adjectives'])} {random.choice(data['nouns'])} {random.choice(data['verbs'])} under the starry sky.",
                lambda: f"The {random.choice(data['nouns'])} {random.choice(data['verbs'])} {random.choice(data['conjunctions'])} started to {random.choice(data['verbs'])}.",
                lambda: f"On a sunny day, a {random.choice(data['nouns'])} {random.choice(data['verbs'])} {random.choice(data['conjunctions'])} {random.choice(data['verbs'])}.",
                lambda: f"The {random.choice(data['nouns'])} {random.choice(data['verbs'])} {random.choice(data['conjunctions'])} began to dance.",
                lambda: f"A {random.choice(data['adjectives'])} {random.choice(data['nouns'])} {random.choice(data['verbs'])} in the gentle breeze.",
                lambda: f"The {random.choice(data['nouns'])} {random.choice(data['verbs'])} {random.choice(data['conjunctions'])} whispered secrets.",
                lambda: f"In the forest, a {random.choice(data['nouns'])} {random.choice(data['verbs'])} {random.choice(data['conjunctions'])} {random.choice(data['verbs'])}.",
                lambda: f"The {random.choice(data['nouns'])} {random.choice(data['verbs'])} {random.choice(data['conjunctions'])} sang a melodious tune.",
                lambda: f"A {random.choice(data['adjectives'])} {random.choice(data['nouns'])} {random.choice(data['verbs'])} {random.choice(data['conjunctions'])} then vanished.",
            ]
        )

        return structure()
    except (KeyError, IndexError) as e:
        logging.error(f"Error: {e}\n{traceback.format_exc()}")
        return "Error generating sentence."
    except Exception as e:
        logging.error(f"An unexpected error occurred: {e}\n{traceback.format_exc()}")
        return "Error generating sentence."


def generate_paragraph() -> str:
    try:
        paragraph = " ".join(generate_sentence() for _ in range(random.randint(4, 10)))
        return paragraph
    except Exception as e:
        logging.error(f"An unexpected error occurred: {e}")
        return "Error generating paragraph."
