import unittest
from calcu import Calculator


class TestCalculator(unittest.TestCase):
    # def setUp(self):
    #    print('Test Start!')

    # def tearDown(self):
    #    print('Test End!')

    # @unittest.skip('skip add') #直接跳過
    def test_add(self):
        c = Calculator(3, 5)
        result = c.add()
        self.assertEqual(result, 8)

    def test_sub(self):
        c = Calculator(7, 2)
        result = c.sub()
        self.assertEqual(result, 5)

    # @unittest.expectedFailure   #不館結果為何，都標註為失敗
    def test_mul(self):
        c = Calculator(3, 3)
        result = c.mul()
        self.assertEqual(result, 9)

    def test_div(self):
        c = Calculator(6, 2)
        result = c.div()
        self.assertEqual(result, 3)


if __name__ == '__main__':
    # unittest.main()
    suit = unittest.TestSuite()
    suit.addTest(TestCalculator("test_add"))
    suit.addTest(TestCalculator("test_sub"))
    suit.addTest(TestCalculator("test_mul"))
    suit.addTest(TestCalculator("test_div"))

    runner = unittest.TextTestRunner()
    runner.run(suit)


