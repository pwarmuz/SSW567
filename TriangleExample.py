from math import acos, degrees


def classifyTriangle(a, b, c):
    """

    Equilateral Triangle:
        - Three equal sides
        - Three equal angles *always 60 degrees

    Isosceles Triangle:
        - Two equal sides
        - Two equal angles

    Scalene Triangle:
        - No equal sides
        - No equal angles

    :param a: Length of side a
    :param b: Length of side b
    :param c: Length of side c

    :return:
    """
    a, b, c, = float(a), float(b), float(c)
    degree_a = round(degrees(acos((b*b + c*c - a*a) / (2*b*c))), 3)
    degree_b = round(degrees(acos((c*c + a*a - b*b) / (2*a*c))), 3)
    degree_c = 180 - degree_a - degree_b

    print degree_a, degree_b, degree_c

    if degree_a == degree_b == degree_c:
        return "Equilateral Triangle"
    if degree_a == 90.0 or degree_b == 90.0 or degree_c == 90.0:
        return "Right Triangle"
    if degree_a == degree_b or degree_a == degree_c:
        return "Isosceles Triangle"
    return "Scalene Triangle"


RESPONSE_MESSAGE = "Line A: {0[0]}, Line B: {0[1]}, Line C: {0[2]} make a {1}"

triangle_parameters = [(8, 6, 7),
                       (3, 3, 3),
                       (7, 8, 7),
                       (3, 4, 5),
                       (6, 8, 10)]

for triangle_parameter in triangle_parameters:
    print RESPONSE_MESSAGE.format(triangle_parameter, classifyTriangle(*triangle_parameter))
