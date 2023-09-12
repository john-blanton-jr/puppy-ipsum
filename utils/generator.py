import random
import logging
from .data_loader import load_data
import traceback

data, quotes = load_data()

logging.basicConfig(level=logging.DEBUG)


def generate_sentence() -> str:
    try:
        structure = random.choice(
            [
                lambda: f"The {random.choice(data['adjectives'])} {random.choice(data['nouns'])} {random.choice(data['verbs'])} {random.choice(data['conjunctions'])} {random.choice(data['verbs'])}.",
                lambda: f"A group of {random.choice(data['nouns'])}s {random.choice(data['verbs'])} in the park.",
                lambda: f"{random.choice(data['nouns'])}s are often {random.choice(data['adjectives'])} and {random.choice(data['adjectives'])}.",
                lambda: f"Every morning, the {random.choice(data['nouns'])} {random.choice(data['verbs'])} {random.choice(data['conjunctions'])} {random.choice(data['verbs'])}.",
                lambda: f"{random.choice(quotes['quotes']) if quotes else 'No quotes available.'}",
                lambda: f"The {random.choice(data['nouns'])} {random.choice(data['verbs'])} at the {random.choice(data['nouns'])}.",
                lambda: f"In the garden, a {random.choice(data['nouns'])} {random.choice(data['verbs'])} while another {random.choice(data['verbs'])}.",
                lambda: f"The {random.choice(data['adjectives'])} {random.choice(data['nouns'])} {random.choice(data['verbs'])} {random.choice(data['conjunctions'])} the {random.choice(data['nouns'])} {random.choice(data['verbs'])}.",
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
