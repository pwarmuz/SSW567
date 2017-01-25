import unittest
from triangle_classifier import classifyTriangle
from math import sqrt


class ClassifyTriangleTests(unittest.TestCase):
    """ Test Cases for the ClassifyTriangle function """

    def runTest(self):
        pass

    def test_equilateral(self):
        """ Test case for equilateral triangles """
        for i in range(1, 100):
            self.assertEquals(classifyTriangle(i, i, i), "Equilateral")

    def test_isosceles(self):
        """ Test case for an isosceles non-right triangles """
        for a in range(1, 100):
            for c in range(a + 1, 2 * a, 1):
                if 2 * (a ** 2) != c ** 2:
                    self.assertEquals(classifyTriangle(a, a, c), "Isosceles")

    def test_isosceles_right(self):
        """ Test case for an isosceles right triangles
            In an isosceles right triangle the sides are in the ratio 1:1:sqrt(2)
        """
        a, b, c = 1, 1, 2
        for i in range(1, 100):
            self.assertEquals(classifyTriangle(a * i, b * i, sqrt(c) * i), "Isosceles Right")

    def test_scalene(self):
        """ Test case for an scalene non-right triangles """
        a, b, c = 8, 6, 7
        for i in range(1, 100, 1):
            self.assertEquals(classifyTriangle(a * i, b * i, c * i), "Scalene")

        a, b, c = 8, 6, 14
        for i in range(1, 100, 1):
            self.assertEquals(classifyTriangle(a * i, b * i, c * i), "Scalene")

    def test_scalene_right(self):
        """ Test case for an scalene right triangles

         Use formula for pythagorean triples for any m and n, such that m>n,
        (2 * m * n, m * m - n * n, m * m + n * n) is a pythagorean triple
        """
        for n in range(1, 50):
            for m in range(n + 1, 50):
                self.assertEquals(classifyTriangle(2 * m * n, m * m - n * n, m * m + n * n), "Scalene Right")

    @unittest.expectedFailure
    def test_precision_fail(self):
        """ Expected Precision Failure

            Expected fault in program when the angle_precision of 1 in the
            classifyTriangle function will cause an Isosceles triangle to be incorrectly
            identified as isosceles right triangle
        """
        a, b, c = 4.95, 4.95, 7
        # Proves that these values do not form a right triangle
        assert a ** 2 + b ** 2 != c ** 2
        # classifyTriangle will return "Isosceles Right", and we are expecting the failure
        self.assertEquals(classifyTriangle(a, b, c, angle_precision=1), "Isosceles")

    def test_precision_fail_fix(self):
        """ Fix for the test_precision_fail unittest by increasing angle_precision from 1 to 3 """
        a, b, c = 4.95, 4.95, 7
        # Proves that these values do not form a right triangle
        assert a ** 2 + b ** 2 != c ** 2
        # classifyTriangle will now return "Isosceles", the correct answer
        self.assertEquals(classifyTriangle(4.95, 4.95, 7, angle_precision=3), "Isosceles")

    def test_triangle_properties_assertion_errors(self):
        """ Test case for AssertionErrors being raised when side values do not match the properties of a triangle"""

        with self.assertRaises(AssertionError):
            classifyTriangle(0, 0, 0)

        with self.assertRaises(AssertionError):
            classifyTriangle(0, 1, 1)

        with self.assertRaises(AssertionError):
            classifyTriangle(1, 0, 1)

        with self.assertRaises(AssertionError):
            classifyTriangle(1, 1, 0)

        with self.assertRaises(AssertionError):
            classifyTriangle(1, 1, 3)

        with self.assertRaises(AssertionError):
            classifyTriangle(1, 3, 1)

        with self.assertRaises(AssertionError):
            classifyTriangle(3, 1, 1)
            
        with self.assertRaises(AssertionError):
            classifyTriangle(-2, 2, 3)
            
        with self.assertRaises(AssertionError):
            classifyTriangle(2, -2, 3)
        
        with self.assertRaises(AssertionError):
            classifyTriangle(2, 2, -3)
        
    def test_letters(self):
        a, b, c = 8, 6, 'c'
        self.assertEquals(classifyTriangle(a, b, c), "Failed")

    def test_parameter_order(self):
        """ Test case for the order of the parameters """
        self.assertEquals(classifyTriangle(2, 2, 3), "Isosceles")
        self.assertEquals(classifyTriangle(2, 3, 2), "Isosceles")
        self.assertEquals(classifyTriangle(3, 2, 2), "Isosceles")

        self.assertEquals(classifyTriangle(2, 2, 2.8284271247461903), "Isosceles Right")
        self.assertEquals(classifyTriangle(2, 2.8284271247461903, 2), "Isosceles Right")
        self.assertEquals(classifyTriangle(2.8284271247461903, 2, 2), "Isosceles Right")

        self.assertEquals(classifyTriangle(16, 12, 14), "Scalene")
        self.assertEquals(classifyTriangle(16, 14, 12), "Scalene")
        self.assertEquals(classifyTriangle(12, 16, 14), "Scalene")
        self.assertEquals(classifyTriangle(12, 14, 16), "Scalene")
        self.assertEquals(classifyTriangle(14, 16, 12), "Scalene")
        self.assertEquals(classifyTriangle(14, 12, 16), "Scalene")

        self.assertEquals(classifyTriangle(6, 8, 10), "Scalene Right")
        self.assertEquals(classifyTriangle(6, 10, 8), "Scalene Right")
        self.assertEquals(classifyTriangle(8, 6, 10), "Scalene Right")
        self.assertEquals(classifyTriangle(8, 10, 6), "Scalene Right")
        self.assertEquals(classifyTriangle(10, 6, 8), "Scalene Right")
        self.assertEquals(classifyTriangle(10, 8, 6), "Scalene Right")
        

