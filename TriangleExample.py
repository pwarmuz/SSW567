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
        return "Equilateral Triangle"

    if a == b or b == c or a == c:
        if 90.0 in angles:
            return "Isosceles Right Triangle"
        return "Isosceles Triangle"

    if 90.0 in angles:
        return "Scalene Right Triangle"
    return "Scalene Triangle"


RESPONSE_MESSAGE = "Line A: {0[0]}, Line B: {0[1]}, Line C: {0[2]} make a {1}"

triangle_parameters = [(8, 6, 7),
                       (3, 3, 3),
                       (7, 8, 7),
                       (3, 4, 5),
                       (6, 8, 10)]

for triangle_parameter in triangle_parameters:
    print RESPONSE_MESSAGE.format(triangle_parameter, classifyTriangle(*triangle_parameter))
