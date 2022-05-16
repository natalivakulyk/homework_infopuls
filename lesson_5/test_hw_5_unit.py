import unittest
from lesson_4 import infopuls_hw_4

class MyTest(unittest.TestCase):
    def test_leap_years(self):
        self.assertEqual(infopuls_hw_4.is_year_leap(1988), True)
        self.assertEqual(infopuls_hw_4.is_year_leap(678), False)
        self.assertEqual(infopuls_hw_4.is_year_leap(600), False)
        self.assertEqual(infopuls_hw_4.is_year_leap(2000), True)

    def test_triangle(self):
        self.assertEqual(infopuls_hw_4.triangle(3, 55, 3), False)
        self.assertEqual(infopuls_hw_4.triangle(1, 2, 77), False)
        self.assertEqual(infopuls_hw_4.triangle(4, 4, 7), True)

    def test_hw_4_2_3(self):
        self.assertEqual(infopuls_hw_4.hw_4_2_3(2, 3, 5), 'Not a tringle')
        self.assertEqual(infopuls_hw_4.hw_4_2_3(4, 4, 7), 'Isosceles triangle')
        self.assertEqual(infopuls_hw_4.hw_4_2_3(4, 4, 4), 'Equilateral triangle')
        self.assertEqual(infopuls_hw_4.hw_4_2_3(5, 3, 6), 'Versatile triangle')




