import unittest
from lcpb import boatSave881

class TestBcalc881(unittest.TestCase):
    def test_881_01(self):
        result = boatSave881.Solution.numRescueBoats(self, [3,2,2,1], 3)
        self.assertEqual(result, 3)
    def test_881_02(self):
        result = boatSave881.Solution.numRescueBoats(self, [3,5,3,4], 5)
        self.assertEqual(result, 4)
    def test_881_03(self):
        result = boatSave881.Solution.numRescueBoats(self,[2,1,3,4,1,3], 5)
        self.assertEqual(result, 3)

if __name__ == '__main__':
    # unittest.main()
    suit = unittest.TestSuite()
    suit.addTest("test_881_01")
    suit.addTest("test_882_02")
    suit.addTest("test_882_03")
    runner = unittest.TextTestRunner()
    runner.run(suit)


