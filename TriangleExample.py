import unittest
from math import acos, degrees, sqrt


def classifyTriangle(a, b, c, angle_precision=1):
    """ Classify a triangle given the length of its 3 sides

        Equilateral Triangle:
            - Three equal sides

        Isosceles Triangle:
            - Two equal sides

        Scalene Triangle:
            - No equal sides

        Right Triangle:
            - One right angle

    :param a: Length of side a
    :param b: Length of side b
    :param c: Length of side c
    :param angle_precision: number of decimal places to round angles

    :return: whether the triangle is scalene, isosceles, or equilateral,
    and whether it is a right triangle as well.

    :rtype: str

    """

    # Convert parameters to floats
    a, b, c, = float(a), float(b), float(c)

    # Assert properties of a triangle
    assert a != 0.0
    assert b != 0.0
    assert c != 0.0
    assert a + b >= c
    assert a + c >= b
    assert b + c >= a

    # Calculate Angles
    angle_a = round(degrees(acos((b * b + c * c - a * a) / (2 * b * c))), angle_precision)
    angle_b = round(degrees(acos((c * c + a * a - b * b) / (2 * a * c))), angle_precision)
    angle_c = round(180.0 - angle_a - angle_b, angle_precision)
    angles = [angle_a, angle_b, angle_c]

    # Classify Triangle
    if a == b == c:
        return "Equilateral"
    if a == b or b == c or a == c:
        if 90.0 in angles:
            return "Isosceles Right"
        return "Isosceles"
    if 90.0 in angles:
        return "Scalene Right"
    return "Scalene"


def generate_equilateral_triangles():
    """ Generate Equilateral Triangles """
    for i in range(1, 1000, 1):
        yield i, i, i


def generate_isosceles_triangles():
    """ Generate isosceles non-right triangles
    In an isosceles right triangle the sides are in the ratio 1:1:sqrt(2)
    """
    for a in range(1, 1000, 1):
        for c in range(a + 1, 10, 1):
            if (2 * a != sqrt(c)) and (a + a > c):
                yield a, a, c


def generate_isosceles_right_triangles():
    """ Generate isosceles triangles
    In an isosceles right triangle the sides are in the ratio 1:1:sqrt(2)
    """
    a, b, c = 1, 1, 2
    for i in range(1, 1000, 1):
        yield a * i, b * i, sqrt(c) * i


def generate_scalene_triangles():
    """ Generate scalene non-right triangles """
    # TODO: Is there a formula or theorem for generating non-right scalene triangles?
    a, b, c = 8, 6, 7
    for i in range(1, 500, 1):
        yield a * i, b * i, c * i

    a, b, c = 8, 6, 14
    for i in range(1, 500, 1):
        yield a * i, b * i, c * i


def generate_scalene_right_triangles():
    """ Generate scalene right triangles

        Use formula for pythagorean triples for any m and n, such that m>n,
        (2 * m * n, m * m - n * n, m * m + n * n) is a pythagorean triple
    """
    for n in range(1, 50):
        for m in range(n + 1, 50):
            yield 2 * m * n, m * m - n * n, m * m + n * n


class ClassifyTriangleMethods(unittest.TestCase):

    def shortDescription(self):
        return None

    def test_equilateral(self):
        """ Test case for equilateral triangles """
        for triangle in generate_equilateral_triangles():
            self.assertEquals(classifyTriangle(*triangle), "Equilateral")

    def test_isosceles(self):
        """ Test case for an isosceles non-right triangles """
        for triangle in generate_isosceles_triangles():
            self.assertEquals(classifyTriangle(*triangle), "Isosceles")

    def test_isosceles_right(self):
        """ Test case for an isosceles right triangles """
        for triangle in generate_isosceles_right_triangles():
            self.assertEquals(classifyTriangle(*triangle), "Isosceles Right")

    def test_scalene(self):
        """ Test case for an scalene non-right triangles """
        for triangle in generate_scalene_triangles():
            self.assertEquals(classifyTriangle(*triangle), "Scalene")

    def test_scalene_right(self):
        """ Test case for an scalene right triangles"""
        for triangle in generate_scalene_right_triangles():
            self.assertEquals(classifyTriangle(*triangle), "Scalene Right")

    @unittest.expectedFailure
    def test_precision_fail(self):
        """ Expected fault in program where the default angle_precision of 1 in the
            classifyTriangle function will cause an Isosceles triangle to be incorrectly
            identified as isosceles right triangle
        """
        self.assertEquals(classifyTriangle(7, 4.95, 4.95), "Isosceles")

    def test_precision_fail_fix(self):
        """ Fix for the test_precision_fail unittest by increasing angle_precision from 1 to 2 """
        self.assertEquals(classifyTriangle(7, 4.95, 4.95, angle_precision=2), "Isosceles")

    def test_triangle_properties_assertions(self):
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


if __name__ == "__main__":
    suite = unittest.TestLoader().loadTestsFromTestCase(ClassifyTriangleMethods)
    unittest.TextTestRunner(verbosity=2).run(suite)

