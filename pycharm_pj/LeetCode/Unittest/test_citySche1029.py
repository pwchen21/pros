import unittest
from lcpb import citySche1029

class test_for_citySche1029(unittest.TestCase):
    def test_1029_01(self):
        result=citySche1029.Solution.twoCitySchedCost(self, [[10,20],[30,200],[400,50],[30,20]])
        self.assertEqual(result, 110)
    def test_1029_02(self):
        result=citySche1029.Solution.twoCitySchedCost(self, [[259,770],[448,54],[926,667],[184,139],[840,118],[577,469]])
        self.assertEqual(result, 1859)
    def test_1029_03(self):
        result = citySche1029.Solution.twoCitySchedCost(self, [[515,563],[451,713],[537,709],[343,819],[855,779],[457,60],[650,359],[631,42]])
        self.assertEqual(result, 3086)


if __name__ == '__main__':
    suit=unittest.TestSuite()
    suit.addTest("test_1029_01")
    suit.addTest("test_1029_02")
    suit.addTest("test_1029_03")

    runner=unittest.TextTestRunner()
    runner.run(suit)
