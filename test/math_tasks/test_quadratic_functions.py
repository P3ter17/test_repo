from unittest import TestCase


from math_tasks.quadratic_functions import root_of_quadratic_fun

class TestQuadraticFunction(TestCase):

    def test_root_of_quadratic_fun_D_less_than_zero(self):
        result = root_of_quadratic_fun(2, 2, 1)
        self.assertEqual(None, result[0])
        self.assertEqual(None, result[1])

    def test_root_of_quadratic_fun_D_equal_zero(self):
        result = root_of_quadratic_fun(1, 2, 1)
        self.assertEqual(-1, result[0])
        self.assertEqual(None, result[1])

    def test_root_of_quadratic_fun_D_greater_than_zero(self):
        result = root_of_quadratic_fun(1, 2, 0)
        self.assertEqual(0, result[0])
        self.assertEqual(-2, result[1])