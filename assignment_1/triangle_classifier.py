"""
Class: SSW567 - Software Testing, Quality Assurance and Maintenance
Assignment Number: 1
"""
from math import acos, degrees
import unittest


def classifyTriangle(a, b, c, angle_precision=10):
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
    angle_a = round(degrees(acos((b ** 2 + c ** 2 - a ** 2) / (2 * b * c))), angle_precision)
    angle_b = round(degrees(acos((c ** 2 + a ** 2 - b ** 2) / (2 * a * c))), angle_precision)
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


def run_tests():
    from test_cases import ClassifyTriangleTests
    suite = unittest.TestLoader().loadTestsFromTestCase(ClassifyTriangleTests)
    unittest.TextTestRunner(verbosity=2).run(suite)


if __name__ == "__main__":
    run_tests()

