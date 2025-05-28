from unittest import TestCase


from math_tasks.sqrt import sqrt_number

class TestSqrt(TestCase):
    def test_sqrt_number(self):
        result = sqrt_number(9)
        self.assertEqual(3, result)

    def test_sqrt_neg_number(self):
        result = sqrt_number(-3)
        self.assertEqual(None, result)

