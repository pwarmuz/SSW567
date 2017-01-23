from math import acos, degrees

valuesA = [8, 3, 7, 3, 6]
valuesB = [6, 3, 8, 4, 8]
valuesC = [7, 3, 7, 5, 10]

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

    :param a:
    :param b:
    :param c:

    :return:
    """
    a, b, c, = float(a), float(b), float(c)
    degree_a = round(degrees(acos((b*b + c*c - a*a) / (2*b*c))), 4)
    degree_b = round(degrees(acos((c*c + a*a - b*b) / (2*b*a))), 4)
    degree_c = 180 - degree_a - degree_b

    # print degree_a, degree_b, degree_c

    if degree_a == degree_b == degree_c:
        return "Equilateral Triangle"
    if degree_a == 90.0 or degree_b == 90.0 or degree_c == 90.0:
        return "Right Triangle"
    if degree_a == degree_b or degree_a == degree_c:
        return "Isosceles Triangle"
    return "Scalene Triangle"


for i in range(0, len(valuesA)):
    response = classifyTriangle(valuesA[i], valuesB[i], valuesC[i])
    print "Line A: ", valuesA[i], "Line B: ", valuesB[i], "Line C: ", valuesC[i], " make a ", response
