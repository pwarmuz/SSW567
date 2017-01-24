""" Generate Triangles With Sides that make the specified type of triangle """
from math import sqrt


def equilateral():
    """ Generate Equilateral Triangles """
    for i in range(1, 1000):
        yield i, i, i


def isosceles():
    """ Generate isosceles non-right triangles
    """
    for a in range(1, 100):
        for c in range(a + 1, 2 * a, 1):
            if 2 * (a ** 2) != c ** 2:
                yield a, a, c


def isosceles_right():
    """ Generate isosceles triangles
    In an isosceles right triangle the sides are in the ratio 1:1:sqrt(2)
    """
    a, b, c = 1, 1, 2
    for i in range(1, 1000):
        yield a * i, b * i, sqrt(c) * i


def scalene():
    """ Generate scalene non-right triangles """
    a, b, c = 8, 6, 7
    for i in range(1, 500, 1):
        yield a * i, b * i, c * i

    a, b, c = 8, 6, 14
    for i in range(1, 500, 1):
        yield a * i, b * i, c * i


def scalene_right():
    """ Generate scalene right triangles

        Use formula for pythagorean triples for any m and n, such that m>n,
        (2 * m * n, m * m - n * n, m * m + n * n) is a pythagorean triple
    """
    for n in range(1, 50):
        for m in range(n + 1, 50):
            yield 2 * m * n, m * m - n * n, m * m + n * n