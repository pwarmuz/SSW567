import unittest
from math import acos, degrees


def classifyTriangle(a, b, c):
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

    :return: whether the triangle is scalene, isosceles, or equilateral,
    and whether it is a right triangle as well.

    :rtype: str

    """

    a, b, c, = float(a), float(b), float(c)
    angle_a = round(degrees(acos((b * b + c * c - a * a) / (2 * b * c))), 3)
    angle_b = round(degrees(acos((c * c + a * a - b * b) / (2 * a * c))), 3)
    angle_c = round(180.0 - angle_a - angle_b, 3)
    angles = [angle_a, angle_b, angle_c]

    # print angles

    if a == b == c:
        return "Equilateral"

    if a == b or b == c or a == c:
        if 90.0 in angles:
            return "Isosceles Right"
        return "Isosceles"

    if 90.0 in angles:
        return "Scalene Right"
    return "Scalene"


class ClassifyTriangleMethods(unittest.TestCase):

    def test_equilateral(self):
        for i in range(1, 1000, 1):
            self.assertEquals(classifyTriangle(i, i, i), "Equilateral")

    #def test_isosceles(self):
    #    self.assertEquals(classifyTriangle(7, 8, 4), "Isosceles")

    #def test_isosceles_right(self):
    #    pass

    #def test_scalene(self):
    #    self.assertEquals(classifyTriangle(8, 6, 7), "Scalene")

    def test_scalene_right(self):
        # Test Pythagorean Triples
        
        a, b, c = 3, 4, 5
        for i in range(1, 1000, 1):
            self.assertEquals(classifyTriangle(a*i, b*i, c*i), "Scalene Right")

        a, b, c = 5, 12, 13
        for i in range(1, 1000, 1):
            self.assertEquals(classifyTriangle(a * i, b * i, c * i), "Scalene Right")

        a, b, c = 8, 15, 17
        for i in range(1, 1000, 1):
            self.assertEquals(classifyTriangle(a * i, b * i, c * i), "Scalene Right")


if __name__ == "__main__":
    suite = unittest.TestLoader().loadTestsFromTestCase(ClassifyTriangleMethods)
    unittest.TextTestRunner(verbosity=2).run(suite)

