import json


def load_data():
    with open("data/words.json", "r") as file:
        data = json.load(file)
    with open("data/quotes.json", "r") as file:
        quotes = json.load(file)
    return data, quotes
