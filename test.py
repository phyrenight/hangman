import unittest
import replay

class testCases(unittest.TestCase):

    def setUp(self):
        pass

    def test_wordsMatch(self):
        self.assertFalse(replay.wordsMatch("hello", "*****"))
        #self.assertFalse(replay.wordsMatch(None, None))
        self.assertTrue(replay.wordsMatch("hello", "hello"))
        self.assertFalse(replay.wordsMatch("Hello", "hello"))
        self.assertFalse(replay.wordsMatch("hello", "he**o"))

    def test_match(self):
        self.assertEqual(replay.match("a", "hello", "*****"), (1, "*****"))
        self.assertEqual(replay.match("e", "hello", "*****"), (0, "*e***"))
        #self.assertEqual(replay.match(None, None, None), (1, None))

if __name__ == "__main__":
    unittest.main()