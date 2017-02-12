import unittest


class TestTriangles(unittest.TestCase):
    """ Test Cases that can be run on both buggyTriangle and fixedTriangle
    1.Request Input:
    The program will request 3 numbers, which we call A, B, and C, which are the sides of a possible triangle
    2.Verify the Input:
    The 3 inputs must be real numbers, greater than 0 and not too big.
    Otherwise, output error message and stop
    3.Verify that the sides form a legal triangle
    If A + B >= C or B + C >= A or C + A >= B then a legal triangle
    Otherwise, output error message and stop
    4.Determine if the triangle is a right triangle
    If A^2 + B^2 = C^2 or B^2 + C^2 = A^2 or C^2 + A^2 = B^2, then a right triangle.
    Due to the issues of numerical precision, = in this case means within 1%
    5.Determine if the triangle is equilateral, isosceles, or scalene
    If the sides are all equal, then the triangle is “Equilateral”
    Else if two side are equal, but not three, then the triangle is “Isosceles”
    6. Display type of triangle
    If it is a right and Isosceles – Print “Right Isosceles Triangle”
    If it is a right and Scalene – Print “Right Scalene Triangle”
    If is a right and Equilateral – Print “Equilateral Triangle”
    If it is not a right and Isosceles – Print “Isosceles Triangle”
"""

    def setUp(self):
        self.func = None

    def test_case_00(self):
        """ Validate Right Isosceles Triangle R6.1 R4.1"""
        self.assertEqual(self.func(6, 6, 8), 'Right Isosceles', '6, 6, 8 Should Be Right')

    def test_case_01(self):
        """ Validate Right Scalene Triangle R6.2 R4.1"""
        self.assertEqual(self.func(3, 4, 5), 'Right Scalene', '3, 4, 5 Should Be Right')

    def test_case_02(self):
        """ Validate Equilateral Triangle R6.3 & R5.1"""
        self.assertEqual(self.func(1, 1, 1), 'Equilateral', '1, 1, 1 Should be Equilateral')

    def test_case_03(self):
        """ Validate Isosceles Triangle R6.4 & R5.2"""
        self.assertEqual(self.func(10, 10, 8), 'Isosceles', '10, 10, 8 Should be Isosceles')

    def test_case_04(self):
        """ Check that it is a legal triangle R3.1"""
        self.assertEqual(self.func(6, 6, 8), 'Right Isosceles', '6, 6, 8 Should Be Right')
        self.assertEqual(self.func(3, 4, 5), 'Right Scalene', '3, 4, 5 Should Be Right')
        self.assertEqual(self.func(1, 1, 1), 'Equilateral', '1, 1, 1 Should be Equilateral')
        self.assertEqual(self.func(10, 10, 8), 'Isosceles', '10, 10, 8 Should be Isosceles')

    def test_case_05(self):
        """ Check that the sum of any 2 sides is greater than the 3rd side, if it fails = 'NotATriangle' R3.2"""
        self.assertEqual(self.func(11, 6, 4), 'NotATriangle', '11, 6, 4 Should be NotATriangle')
        self.assertEqual(self.func(6, 11, 4), 'NotATriangle', '6, 11, 4 Should be NotATriangle')
        self.assertEqual(self.func(6, 4, 11), 'NotATriangle', '6, 4, 11 Should be NotATriangle')

    def test_case_06(self):
        """ Check Values, if a or b or c > 200 should = 'InvalidInput' R2.2"""
        self.assertEqual(self.func(195, 10, 201), 'InvalidInput', '195, 10, 201 Should be InvalidInput')
        self.assertEqual(self.func(10, 201, 195), 'InvalidInput', '10, 201, 195 Should be InvalidInput')
        self.assertEqual(self.func(201, 195, 10), 'InvalidInput', '201, 195, 10 Should be InvalidInput')

    def test_case_07(self):
        """ Check Values, if a or b or c <= 0 should = 'InvalidInput' R2.1"""
        self.assertEqual(self.func(-2, 2, 3), 'InvalidInput', '-2, 2, 3 Should be InvalidInput')
        self.assertEqual(self.func(2, -2, 3), 'InvalidInput', '2, -2, 3 Should be InvalidInput')
        self.assertEqual(self.func(2, 2, -3), 'InvalidInput', '2, 2, -3 Should be InvalidInput')

        self.assertEqual(self.func(0, 2, 3), 'InvalidInput', '0, 2, 3 Should be InvalidInput')
        self.assertEqual(self.func(2, 0, 3), 'InvalidInput', '2, 0, 3 Should be InvalidInput')
        self.assertEqual(self.func(2, 2, 0), 'InvalidInput', '2, 2, 0 Should be InvalidInput')

    def test_case_08(self):
        """  Check input value is integer else = 'InvalidInput' (str)(float) R2.1 """
        self.assertEqual(self.func("3", 3, 3), 'InvalidInput', '"3", 3, 3 Should be InvalidInput')
        self.assertEqual(self.func(3, "3", 3), 'InvalidInput', '3, "3", 3 Should be InvalidInput')
        self.assertEqual(self.func(3, 3, "3"), 'InvalidInput', '3, 3, "3" Should be InvalidInput')
        self.assertEqual(self.func(5.5, 5.5, 5.5), 'InvalidInput', '5.5, 5.5, 5.5 Should be InvalidInput')
        self.assertEqual(self.func(2.5, 6, 6.5), 'InvalidInput', '2.5, 6, 6.5 Should be InvalidInput')
        self.assertEqual(self.func(8, 8, 9.2), 'InvalidInput', '8, 8, 9.2 Should be InvalidInput')
        self.assertEqual(self.func(3.5, 4.5, 6), 'InvalidInput', '3.5, 4.5, 6 Should be InvalidInput')


class TestTrianglesFixed(TestTriangles):
    def setUp(self):
        from fixedTriangle import classifyTriangle
        self.func = classifyTriangle


class TestTrianglesBuggy(TestTriangles):
    def setUp(self):
        from buggyTriangle import classifyTriangle
        self.func = classifyTriangle
