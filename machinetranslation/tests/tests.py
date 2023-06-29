import unittest

from translator import englishToFrench, frenchToEnglish


class testTranslator (unittest.TestCase):
    def test_englishToFrench_1(self):
        self.assertEqual(englishToFrench('Hello'), 'Bonjour')

    def test_englishToFrench_2(self):
        self.assertEqual(englishToFrench('Let\'s go'), 'Allons-y')

    def test_frenchToEnglish_1(self):
        self.assertEqual(frenchToEnglish('Bonjour'), 'Hello')

    def test_frenchToEnglish_2(self):
        self.assertEqual(frenchToEnglish('Allons-y'), 'Let\'s go')


if __name__ == '__main__':
    unittest.main()
