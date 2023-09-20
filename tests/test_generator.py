import unittest
from utils.generator import generate_sentence, generate_paragraph


class TestGenerator(unittest.TestCase):
    def test_generate_sentence(self):
        sentence = generate_sentence()
        self.assertIsNotNone(sentence)
        self.assertIsInstance(sentence, str)

    def test_generate_paragraph(self):
        paragraph = generate_paragraph()
        self.assertIsNotNone(paragraph)
        self.assertIsInstance(paragraph, str)


if __name__ == "__main__":
    unittest.main()
