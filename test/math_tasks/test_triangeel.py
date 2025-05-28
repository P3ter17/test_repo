
from unittest import TestCase


from math_tasks.triangeel import calculate_triangle_angles

class TestTriangle(TestCase):


    def test_calculate_triangle_angles(self):
        angle = calculate_triangle_angles(5, 6, 7)
        talfa = 44.42
        tbeta = 50.7
        tgama = 78.46
        self.assertEqual(talfa, angle[0])
        self.assertEqual(tbeta, angle[1])
        self.assertEqual(tgama, angle[2])

    def test_calculate_triangle_angles_negative(self):
        result = calculate_triangle_angles(-1, 0, 5)
        self.assertEqual(0, angle[0])
        self.assertEqual(0, angle[1])
        self.assertEqual(0, angle[2])


