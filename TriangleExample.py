import unittest
from math import acos, degrees, sqrt


def classifyTriangle(a, b, c, angle_precision = 2):
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
    # Assert Properties of sides of a triangle
    assert a + b >= c
    assert a + c >= b
    assert b + c >= a

    # Calculate Angles
    a, b, c, = float(a), float(b), float(c)
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

    def test_equilateral(self):
        """ Test case for an equilateral triangles """
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


if __name__ == "__main__":
    suite = unittest.TestLoader().loadTestsFromTestCase(ClassifyTriangleMethods)
    unittest.TextTestRunner(verbosity=2).run(suite)

