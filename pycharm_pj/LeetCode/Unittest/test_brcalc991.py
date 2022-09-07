import unittest
from lcpb import brcalc991

class TestBcalc991(unittest.TestCase):
    def test_991_01(self):
        result = brcalc991.Solution.brokenCalc(self, 2,5)
        self.assertEqual(result, 4)
    def test_991_02(self):
        result = brcalc991.Solution.brokenCalc(self, 9, 103)
        self.assertEqual(result, 8)

if __name__ == '__main__':
    # unittest.main()
    suit = unittest.TestSuite()
    suit.addTest("test_991_01")
    suit.addTest("test_991_02")
    runner = unittest.TextTestRunner()
    runner.run(suit)


