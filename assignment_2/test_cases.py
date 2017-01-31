import unittest


class TestTriangles(unittest.TestCase):
    """ Test Cases that can be run on both buggyTriangle and fixedTriangle """

    def setUp(self):
        self.func = None

    def test_case_00(self):
        """ Validate Right Triangle -PW"""
        self.assertEqual(self.func(3, 4, 5), 'Right', '3, 4, 5 Should Be Right')

    def test_case_01(self):
        """ Validate Equilateral Triangle -PW"""
        self.assertEqual(self.func(1, 1, 1), 'Equilateral', '1, 1, 1 Should be Equilateral')

    def test_case_02(self):
        """ Validate Isosceles Triangle -PW"""
        self.assertNotEqual(self.func(10, 10, 10), 'Isosceles', '10, 10, 10 Should be Equilateral')
        self.assertEqual(self.func(10, 10, 8), 'Isosceles', '10, 10, 8 Should be Isosceles')

    def test_case_03(self):
        """ Validate Scalene Triangle -CD"""
        self.assertEqual(self.func(8, 6, 7), 'Scalene', '8, 6, 7 Should be Scalene')

    def test_case_04(self):
        """ Check Values, if a or b or c > 200 should = 'InvalidInput' -CD"""
        self.assertEqual(self.func(195, 10, 201), 'InvalidInput', '195, 10, 201 Should be InvalidInput')
        self.assertEqual(self.func(10, 201, 195), 'InvalidInput', '10, 201, 195 Should be InvalidInput')
        self.assertEqual(self.func(201, 195, 10), 'InvalidInput', '201, 195, 10 Should be InvalidInput')

    def test_case_05(self):
        """ Check Values, if a or b or c <= 0 should = 'InvalidInput' -CD"""
        self.assertEqual(self.func(-2, 2, 3), 'InvalidInput', '-2, 2, 3 Should be InvalidInput')
        self.assertEqual(self.func(2, -2, 3), 'InvalidInput', '2, -2, 3 Should be InvalidInput')
        self.assertEqual(self.func(2, 2, -3), 'InvalidInput', '2, 2, -3 Should be InvalidInput')

        self.assertEqual(self.func(0, 2, 3), 'InvalidInput', '0, 2, 3 Should be InvalidInput')
        self.assertEqual(self.func(2, 0, 3), 'InvalidInput', '2, 0, 3 Should be InvalidInput')
        self.assertEqual(self.func(2, 2, 0), 'InvalidInput', '2, 2, 0 Should be InvalidInput')

    def test_case_06(self):
        """  Check input value is integer else = 'InvalidInput' -CD (str) and -JT (float)"""
        self.assertEqual(self.func("3", 3, 3), 'InvalidInput', '"3", 3, 3 Should be InvalidInput')
        self.assertEqual(self.func(3, "3", 3), 'InvalidInput', '3, "3", 3 Should be InvalidInput')
        self.assertEqual(self.func(3, 3, "3"), 'InvalidInput', '3, 3, "3" Should be InvalidInput')
        self.assertEqual(self.func(5.5, 5.5, 5.5), 'InvalidInput', '5.5, 5.5, 5.5 Should be InvalidInput')
        self.assertEqual(self.func(2.5, 6, 6.5), 'InvalidInput', '2.5, 6, 6.5 Should be InvalidInput')
        self.assertEqual(self.func(8, 8, 9.2), 'InvalidInput', '8, 8, 9.2 Should be InvalidInput')
        self.assertEqual(self.func(3.5, 4.5, 6), 'InvalidInput', '3.5, 4.5, 6 Should be InvalidInput')

    def test_case_08(self):
        """ Check that the sum of any 2 sides is greather than the 3rd side, if it fails = 'NotATriangle' -JT"""
        self.assertEqual(self.func(11, 6, 4), 'NotATriangle', '11, 6, 4 Should be NotATriangle')
        self.assertEqual(self.func(6, 11, 4), 'NotATriangle', '6, 11, 4 Should be NotATriangle')
        self.assertEqual(self.func(6, 4, 11), 'NotATriangle', '6, 4, 11 Should be NotATriangle')

    def test_case_09(self):
        """ Check parameter order - PW"""
        self.assertEqual(self.func(3, 4, 5), 'Right', '3,4,5 is a Right triangle')
        self.assertEqual(self.func(4, 5, 3), 'Right', '4,5,3 is a Right triangle')
        self.assertEqual(self.func(5, 3, 4), 'Right', '5,4,3 is a Right triangle')

        self.assertEqual(self.func(2, 2, 3), 'Isosceles', '2,2,3 is a Isosceles triangle')
        self.assertEqual(self.func(2, 3, 2), 'Isosceles', '2,3,2 is a Isosceles triangle')
        self.assertEqual(self.func(3, 2, 2), 'Isosceles', '3,2,2 is a Isosceles triangle')

        self.assertEqual(self.func(1, 1, 1), 'Equilateral', '1, 1, 1 Should be Equilateral')

        self.assertEqual(self.func(8, 6, 7), 'Scalene', '8, 6, 7 Should be Scalene')
        self.assertEqual(self.func(8, 7, 6), 'Scalene', '8, 7, 6 Should be Scalene')
        self.assertEqual(self.func(6, 7, 8), 'Scalene', '6, 7, 8 Should be Scalene')
        self.assertEqual(self.func(6, 8, 7), 'Scalene', '6, 8, 7 Should be Scalene')
        self.assertEqual(self.func(7, 8, 6), 'Scalene', '7, 8, 6 Should be Scalene')
        self.assertEqual(self.func(7, 6, 8), 'Scalene', '7, 6, 8 Should be Scalene')

class TestTrianglesFixed(TestTriangles):
    def setUp(self):
        from fixedTriangle import classifyTriangle
        self.func = classifyTriangle


class TestTrianglesBuggy(TestTriangles):
    def setUp(self):
        from buggyTriangle import classifyTriangle
        self.func = classifyTriangle
