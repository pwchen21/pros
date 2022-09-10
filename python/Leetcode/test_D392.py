import unittest
from D392 import Solution

class TestSolution(unittest.TestCase):
    def test_isSubsequence(self):
        c=Solution()
        result=c.isSubsequence("ab", "abbbbbb")
        self.assertEqual(result, True)
        result=c.isSubsequence("ab", "bbbbbba")
        self.assertEqual(result, False)
        result=c.isSubsequence("ab", "abbbbbb")
        self.assertEqual(result, True)



if __name__ == '__main__':
    #unittest.main()
    suit = unittest.TestSuite()
    suit.addTest(TestSolution("test_isSubsequence"))

    runner = unittest.TextTestRunner()
    runner.run(suit)