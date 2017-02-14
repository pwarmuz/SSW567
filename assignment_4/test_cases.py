# coding=utf-8
import unittest
from math import sqrt
from itertools import permutations
from fixedTriangle import is_within_1_percent

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
    def right_isosceles_triangles(cls):
        """ Generate Right Isosceles Triangles (all values <= 200) """
        for i in range(1, 142):
            yield 1 * i, 1 * i, sqrt(2) * i

    @classmethod
    def right_scalene_triangles(cls):
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
    def equilateral_triangles(cls):
        """ Generate Right Scalene Triangles (all values <= 200) """
        for i in range(1, 201):
            yield i-.5, i-.5, i-.5
            yield i, i, i

    @classmethod
    def isosceles_triangles(cls):
        """ Generate Isosceles (Non-Right) Triangles (all values <= 200) """
        for a in range(1, 101):
            for c in range(a + 1, 2 * a):
                if 2 * (a ** 2) != c ** 2:
                    if is_within_1_percent(2 * (a ** 2), c ** 2):
                        continue
                    yield a, a, c

    @classmethod
    def isosceles_triangles_bug(cls):
        """ Generate Isosceles (Non-Right) Triangles (all values <= 200)
            These bug values will incorrectly get classified as Isosceles Right Triangle Due to precision error.
        """
        for a in range(1, 101):
            for c in range(a + 1, 2 * a):
                if 2 * (a ** 2) != c ** 2:
                    if is_within_1_percent(2 * (a ** 2), c ** 2):
                        yield a, a, c

    def __assert_equals_test_case(self, generator_name, expected_value):
        for triangle in getattr(self, generator_name)():
            for a, b, c in permutations(triangle):
                try:
                    self.assertEquals(self.func(a, b, c), expected_value)
                except AssertionError as e:
                    raise AssertionError('For triangle with parameters {0}, {1}'.format((a, b, c), e.message))

    def test_case_00_right_isosceles(self):
        """ Validate Right Isosceles Triangle R6.1 R4.1"""
        self.__assert_equals_test_case("right_isosceles_triangles", 'Right Isosceles Triangle')

    def test_case_01_right_scalene(self):
        """ Validate Right Scalene Triangle R6.2 R4.1"""
        self.__assert_equals_test_case("right_scalene_triangles", 'Right Scalene Triangle')

    def test_case_02_equilateral(self):
        """ Validate Equilateral Triangle R6.3 & R5.1"""
        self.__assert_equals_test_case("equilateral_triangles", 'Equilateral Triangle')

    def test_case_03_isosceles(self):
        """ Validate Isosceles Triangle R6.4 & R5.2"""
        self.__assert_equals_test_case("isosceles_triangles", 'Isosceles Triangle')

    def test_case_03b_isosceles_precision_bug(self):
        """ Precision of one percent leads to isosceles triangles mistaken for Right Isosceles Triangles,
            examples: (12, 12, 17), (17, 17, 24), (19, 19, 27), (22, 22, 31)
        """
        self.__assert_equals_test_case("isosceles_triangles_bug", 'Right Isosceles Triangle')

    #def test_case_04(self):
    #    """ Check that it is a legal triangle R3.1"""
    #    self.assertEqual(self.func(6, 6, 8), 'Right Isosceles', '6, 6, 8 Should Be Right')
    #    self.assertEqual(self.func(3, 4, 5), 'Right Scalene', '3, 4, 5 Should Be Right')
    #    self.assertEqual(self.func(1, 1, 1), 'Equilateral', '1, 1, 1 Should be Equilateral')
    #    self.assertEqual(self.func(10, 10, 8), 'Isosceles', '10, 10, 8 Should be Isosceles')

    #def test_case_05(self):
    #    """ Check that the sum of any 2 sides is greater than the 3rd side, if it fails = 'NotATriangle' R3.2"""
    #    self.assertEqual(self.func(11, 6, 4), 'NotATriangle', '11, 6, 4 Should be NotATriangle')
    #    self.assertEqual(self.func(6, 11, 4), 'NotATriangle', '6, 11, 4 Should be NotATriangle')
    #    self.assertEqual(self.func(6, 4, 11), 'NotATriangle', '6, 4, 11 Should be NotATriangle')

    #def test_case_06(self):
    #    """ Check Values, if a or b or c > 200 should = 'InvalidInput' R2.2"""
    #    self.assertEqual(self.func(195, 10, 201), 'InvalidInput', '195, 10, 201 Should be InvalidInput')
    #    self.assertEqual(self.func(10, 201, 195), 'InvalidInput', '10, 201, 195 Should be InvalidInput')
    #    self.assertEqual(self.func(201, 195, 10), 'InvalidInput', '201, 195, 10 Should be InvalidInput')

    #def test_case_07(self):
    #    """ Check Values, if a or b or c <= 0 should = 'InvalidInput' R2.1"""
    #    self.assertEqual(self.func(-2, 2, 3), 'InvalidInput', '-2, 2, 3 Should be InvalidInput')
    #    self.assertEqual(self.func(2, -2, 3), 'InvalidInput', '2, -2, 3 Should be InvalidInput')
    #    self.assertEqual(self.func(2, 2, -3), 'InvalidInput', '2, 2, -3 Should be InvalidInput')

    #    self.assertEqual(self.func(0, 2, 3), 'InvalidInput', '0, 2, 3 Should be InvalidInput')
    #    self.assertEqual(self.func(2, 0, 3), 'InvalidInput', '2, 0, 3 Should be InvalidInput')
    #    self.assertEqual(self.func(2, 2, 0), 'InvalidInput', '2, 2, 0 Should be InvalidInput')

    #def test_case_08(self):
    #    """  Check input value is integer else = 'InvalidInput' (str)(float) R2.1 """
    #    self.assertEqual(self.func("3", 3, 3), 'InvalidInput', '"3", 3, 3 Should be InvalidInput')
    #    self.assertEqual(self.func(3, "3", 3), 'InvalidInput', '3, "3", 3 Should be InvalidInput')
    #    self.assertEqual(self.func(3, 3, "3"), 'InvalidInput', '3, 3, "3" Should be InvalidInput')
    #    self.assertEqual(self.func(5.5, 5.5, 5.5), 'InvalidInput', '5.5, 5.5, 5.5 Should be InvalidInput')
    #    self.assertEqual(self.func(2.5, 6, 6.5), 'InvalidInput', '2.5, 6, 6.5 Should be InvalidInput')
    #    self.assertEqual(self.func(8, 8, 9.2), 'InvalidInput', '8, 8, 9.2 Should be InvalidInput')
    #    self.assertEqual(self.func(3.5, 4.5, 6), 'InvalidInput', '3.5, 4.5, 6 Should be InvalidInput')


class TestTrianglesFixed(TestTriangles):
    def setUp(self):
        from fixedTriangle import classifyTriangle
        self.func = classifyTriangle


