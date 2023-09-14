import unittest
from ..utils.generator import generate_sentence, generate_paragraph


class TestGenerator(unittest.TestCase):
    def test_generate_sentence(self):
        sentence = generate_sentence()

        # Test that a sentence is generated
        self.assertIsNotNone(sentence)

        # Test that the generated sentence is a string
        self.assertIsInstance(sentence, str)

    def test_generate_paragraph(self):
        paragraph = generate_paragraph()

        # Test that a paragraph is generated
        self.assertIsNotNone(paragraph)

        # Test that the generated paragraph is a string
        self.assertIsInstance(paragraph, str)


if __name__ == "__main__":
    unittest.main()
