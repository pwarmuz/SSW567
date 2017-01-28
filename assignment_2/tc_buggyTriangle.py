import unittest
from buggyTriangle import classifyTriangle
from fixedTriangle import classifyTriangle

class TestTriangles(unittest.TestCase):
    """ Test Cases that can be run on both buggyTriangle and fixedTriangle """

    def test_case_00(self):
        """ Validate Right Triangle -PW"""
        self.assertEqual(classifyTriangle(3,4,5), 'Right', '3,4,5 is a Right triangle')

    def test_case_01(self):
        """ Validate Equilateral Triangle -PW"""
        self.assertEqual(classifyTriangle(1,1,1), 'Equilateral', '1,1,1 should be equilateral')


    def test_case_02(self):
        """ Validate Isosceles Triangle -PW"""
        self.assertNotEqual(classifyTriangle(10,10,10), 'Isosceles', 'Should be Equilateral')


    def test_case_03(self):
        """ Validate Scalene Triangle """
        self.assertEqual(classifyTriangle(10,15,30), 'Scalene', 'Should be Isoceles')


    def test_case_04(self):
        """ Check Values, if a or b or c > 200 should = 'InvalidInput' """


    def test_case_05(self):
        """ Check Values, if a or b or c <= 0 should = 'InvalidInput' """


    def test_case_06(self):
        """  Check input value is integer else = 'InvalidInput' """


    def test_case_07(self):
        """ Check that the sum of any 2 sides is less then the 3rd side, if it fails = 'NotATriangle' """


    def test_case_08(self):
        """ Check Values, if a or b or c <= 0 should = 'InvalidInput' """


    def test_case_09(self):
        """ Check parameter order - PW"""
        self.assertEqual(classifyTriangle(3,4,5), 'Right', '3,4,5 is a Right triangle')
        self.assertEqual(classifyTriangle(4,5,3), 'Right', '4,5,3 is a Right triangle')
        self.assertEqual(classifyTriangle(5,3,4), 'Right', '5,4,3 is a Right triangle')

        self.assertEqual(classifyTriangle(2,2,3), 'Isosceles', '2,2,3 is a Isosceles triangle')
        self.assertEqual(classifyTriangle(2,3,2), 'Isosceles', '2,3,2 is a Isosceles triangle')
        self.assertEqual(classifyTriangle(3,2,2), 'Isosceles', '3,2,2 is a Isosceles triangle')
