import math

valuesA = [8, 3, 7, 3, 6]
valuesB = [6, 3, 8, 4, 8]
valuesC = [7, 3, 7, 5, 10]


def classifyTriangle(a,b,c):
    cos_a = (math.pow(b, 2) + math.pow(c, 2) - math.pow(a, 2)) / (2*b*c)
    radian_a = math.acos(cos_a)
    cos_b = (math.pow(c, 2) + math.pow(a, 2) - math.pow(b, 2)) / (2*b*a)
    radian_b = math.acos(cos_b)

    degree_a = round(math.degrees(radian_a), 1)
    degree_b = round(math.degrees(radian_b), 1)
    degree_c = 180 - (degree_a + degree_b)

    print degree_a, degree_b, degree_c
    if degree_a == degree_b == degree_c:
        triangle_type = "Equilateral Triangle"
    elif degree_a == 90.0 or degree_b == 90.0 or degree_c == 90.0:
        triangle_type = "Right Triangle"
    elif degree_a == degree_b or degree_a == degree_c:
        triangle_type = "Isosceles Triangle"
    else:
        triangle_type = "Scalene Triangle"

    return triangle_type


for i in range(0, len(valuesA)):
    response = classifyTriangle(valuesA[i], valuesB[i], valuesC[i])
    print "Line A: ", valuesA[i], "Line B: ", valuesB[i], "Line C: ", valuesC[i], " make a ", response
