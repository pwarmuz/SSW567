# coding=utf-8
import unittest
from math import sqrt
from itertools import permutations


class TestTriangles(unittest.TestCase):

    """ Test Cases that can be run on both buggyTriangle and fixedTriangle

    Requirements Document:
    1.Request Input:
        1. The program will request 3 numbers, which we call A, B, and C, which are the sides of a possible triangle
    2.Verify the Input:
        1. The 3 inputs must be real numbers, greater than 0 and not too big.
        2. Otherwise, output error message and stop
    3.Verify that the sides form a legal triangle
        1. If A + B >= C or B + C >= A or C + A >= B then a legal triangle
        2. Otherwise, output error message and stop
    4.Determine if the triangle is a right triangle
        1. If A^2 + B^2 = C^2 or B^2 + C^2 = A^2 or C^2 + A^2 = B^2, then a right triangle.
        2. Due to the issues of numerical precision, = in this case means within 1%
    5.Determine if the triangle is equilateral, isosceles, or scalene
        1. If the sides are all equal, then the triangle is “Equilateral”
        2. Else if two side are equal, but not three, then the triangle is “Isosceles”
    6. Display type of triangle
        1. If it is a right and Isosceles – Print “Right Isosceles Triangle”
        2. If it is a right and Scalene – Print “Right Scalene Triangle”
        3. If is a right and Equilateral – Print “Equilateral Triangle”
        4. If it is not a right and Isosceles – Print “Isosceles Triangle”
    7. Return

    """

    def setUp(self):
        self.func = None

    @classmethod
    def yield_right_isosceles_triangles(cls):
        """ Generate Right Isosceles Triangles (all values <= 200) """
        for i in range(1, 142):
            yield 1 * i, 1 * i, sqrt(2) * i

    @classmethod
    def yield_right_scalene_triangles(cls):
        """ Generate Right Scalene Triangles (all values <= 200) """
        for n in range(1, 10):
            m = n + 1
            while True:
                a, b, c = 2 * m * n, m * m - n * n, m * m + n * n
                if a <= 200 and b <= 200 and c <= 200:
                    yield a, b, c
                    m += 1
                else:
                    break

    @classmethod
    def yield_equilateral_triangles(cls):
        """ Generate Right Equilateral Triangles (all values <= 200) """
        for i in range(1, 201):
            yield i-.5, i-.5, i-.5
            yield i, i, i

    @classmethod
    def yield_isosceles_triangles(cls):
        """ Generate Isosceles (Non-Right) Triangles (all values <= 200) """
        for a in range(1, 101):
            for c in range(a + 1, 2 * a):
                if 2 * (a ** 2) != c ** 2:
                    yield a, a, c

    def __assert_equals_test_case(self, values, expected_value):
        for triangle in values:
            for a, b, c in permutations(triangle):
                try:
                    self.assertEquals(self.func(a, b, c), expected_value)
                except AssertionError as e:
                    raise AssertionError('For triangle with parameters {0}, {1}'.format((a, b, c), e.message))

    def __assert_not_equal_test_case(self, values, expected_value):
        for triangle in values:
            for a, b, c in permutations(triangle):
                try:
                    self.assertNotEqual(self.func(a, b, c), expected_value)
                except AssertionError as e:
                    raise AssertionError('For triangle with parameters {0}, {1}'.format((a, b, c), e.message))

    def test_case_00_right_isosceles(self):
        """ Validate Right Isosceles Triangle R6.1 R4.1"""
        self.__assert_equals_test_case(self.yield_right_isosceles_triangles(), 'Right Isosceles Triangle')

    def test_case_01_right_scalene(self):
        """ Validate Right Scalene Triangle R6.2 R4.1"""
        self.__assert_equals_test_case(self.yield_right_scalene_triangles(), 'Right Scalene Triangle')

    def test_case_02_equilateral(self):
        """ Validate Equilateral Triangle R6.3 & R5.1"""
        self.__assert_equals_test_case(self.yield_equilateral_triangles(), 'Equilateral Triangle')

    def test_case_03_isosceles(self):
        """ Validate Isosceles Triangle R6.4 & R5.2"""
        self.__assert_equals_test_case(self.yield_isosceles_triangles(), 'Isosceles Triangle')

    def test_case_04_legal_triangle(self):
        """ Verify that the sides form a legal triangle (Triangle Inequality) R3.1"""
        self.__assert_not_equal_test_case([(4, 4, 8), (4, 5, 8)], 'NotATriangle')

    def test_case_05_not_legal_triangle(self):
        """ Verify that the sides don't form a legal triangle (Triangle Inequality) R3.2"""
        self.__assert_equals_test_case([(4, 6, 11)], 'NotATriangle')

    def test_case_06_side_too_big(self):
        """ Check Values, if a or b or c > 200 should = 'InvalidInput' R2.2"""
        self.__assert_equals_test_case([(195, 10, 201)], 'InvalidInput')

    def test_case_07_side_too_small(self):
        """ Check Values, if a or b or c <= 0 should = 'InvalidInput' R2.1"""
        self.__assert_equals_test_case([(-2, 2, 3), (0, 2, 3)], 'InvalidInput')

    def test_case_08_not_a_real_number(self):
        """  Check input value can't be converted to a float R2.1 """
        self.__assert_equals_test_case([("A", 1, 1)], 'InvalidInput')

    def test_case_09_one_percent_precision(self):
        """  Check to see if precision of 2 decimal places correctly identifies Right Isosceles Triangle R4.2 """
        self.assertEquals(self.func(1, 1, 1.4142135623730951, precision=100), 'Isosceles Triangle')
        self.assertEquals(self.func(1, 1, 1.4142135623730951, precision=2), 'Right Isosceles Triangle')


class TestTrianglesFixed(TestTriangles):
    def setUp(self):
        from fixedTriangle import classifyTriangle
        self.func = classifyTriangle


