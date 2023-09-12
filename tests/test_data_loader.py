import unittest
from utils.data_loader import load_data


class TestDataLoader(unittest.TestCase):
    def test_load_data(self):
        data, quotes = load_data()

        # Test that data and quotes are not None
        self.assertIsNotNone(data)
        self.assertIsNotNone(quotes)

        # Test that data contains expected keys
        self.assertIn("adjectives", data)
        self.assertIn("nouns", data)
        self.assertIn("verbs", data)
        self.assertIn("conjunctions", data)

        # Test that quotes is a dictionary containing a list of quotes
        self.assertIsInstance(quotes, dict)
        self.assertIn("quotes", quotes)
        self.assertIsInstance(quotes["quotes"], list)


if __name__ == "__main__":
    unittest.main()
