import math

valuesA = [8, 3, 7, 3, 6]
valuesB = [6, 3, 8, 4, 8]
valuesC = [7, 3, 7, 5, 10]

def classifyTriangle(a,b,c):
    cosA = ( math.pow(b, 2) + math.pow(c, 2) - math.pow(a, 2)) / (2*b*c)
    radianA = math.acos(cosA)
    cosB = ( math.pow(c, 2) + math.pow(a, 2) - math.pow(b, 2)) / (2*b*a)
    radianB = math.acos(cosB)
    degreeA = round(math.degrees(radianA), 1)
    degreeB = round(math.degrees(radianB), 1)
    degreeC = 180 - (degreeA + degreeB)
    print degreeA, degreeB, degreeC
    if degreeA == degreeB == degreeC:
        typeTriangle = "Equilateral Triangle"
    elif degreeA == 90.0 or degreeB == 90.0 or degreeC == 90.0:
        typeTriangle = "Right Triangle"
    elif degreeA == degreeB or degreeA == degreeC:
        typeTriangle = "Isosceles Triangle"
    else:
        typeTriangle = "Scalene Triangle"
    return typeTriangle

for i in range(0,len(valuesA)):
    response = classifyTriangle(valuesA[i], valuesB[i], valuesC[i])
    print "Line A: ", valuesA[i], "Line B: ", valuesB[i], "Line C: ", valuesC[i], " make a ", response
