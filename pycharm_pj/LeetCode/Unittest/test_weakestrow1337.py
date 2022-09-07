import unittest
from lcpb import weakestrow1337

class test_for_1337(unittest.TestCase):
    def test_1337_01(self):
        T=weakestrow1337.Solutions()
        result=T.kWeakestRows([[1,1,0,0,0],[1,1,1,1,0],[1,0,0,0,0],[1,1,0,0,0],[1,1,1,1,1]], 3)
        self.assertEqual(result, [2, 0, 3])
    def test_1337_02(self):
        T=weakestrow1337.Solutions()
        result=T.kWeakestRows([[1,0,0,0],[1,1,1,1],[1,0,0,0],[1,0,0,0]], 2)
        self.assertEqual(result, [0,2])
    #def test_1337_03(self):
    #    result=weakestrow1337.Solutions.kWeakestRows([[1,1,0,0,0],[1,1,1,1,0],[1,0,0,0,0],[1,1,0,0,0],[1,1,1,1,1]], 3)
    #   self.assertEqual(result, [2, 0, 3])


if __name__ == '__main__':
    suit=unittest.TestSuite()
    suit.addTest("test_1337_01")
    suit.addTest("test_1337_02")
    #suit.addTest("test_1337_03")

    runner=unittest.TextTestRunner()
    runner.run(suit)
