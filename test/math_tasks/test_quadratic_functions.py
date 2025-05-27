from unittest import TestCase


from math_tasks.quadratic_functions import root_of_quadratic_fun

class TestQuadraticFunction(TestCase):

    def test_root_of_quadratic_fun(self):
        result = root_of_quadratic_fun(2, 2, 1)
        self.assertEqual(0, result)