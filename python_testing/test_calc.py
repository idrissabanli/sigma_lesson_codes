
import unittest
from calc_cls import Calc


class CalcTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        a = 4
        b = 2
        cls.c = Calc(a, b)
        print('setUpClass')

    def test_sum(self):
        self.assertEqual(6, self.c.sum())
        print('test_sum')

    def test_divide(self):
        self.assertEqual(2, self.c.divide())
        print('test_divide')

    @classmethod
    def tearDownClass(cls):
        del cls.c
        print('tearDownClass')
        

    # def test_divide_with_zero_arg(self):
    #     a = 4
    #     b = 0
    #     c = Calc(a, b)
    #     self.assertRaises(ZeroDivisionError, c.divide)


# if __name__ == '__main__':
#     unittest.main()