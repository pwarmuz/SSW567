"""
Created on Thu Jan 14 13:44:00 2016

This file shows some simple (and buggy) python code to solve the Triangles assignment.   
The primary goal of this file is to demonstrate a simple python program and the use of the
unittest package.

Note that this code includes intentional errors for you to find.


@author: jrr
"""

import unittest     # this makes Python unittest module available
import test_cases


def classifyTriangle(a, b, c):
    """
    
    This function returns a string with the type of triangle from three integer values
    corresponding to the lengths of the three sides of the Triangle.
    
    return:
        If all three sides are equal, return 'Equilateral'
        If exactly one pair of sides are equal, return 'Isoceles'
        If no pair of  sides are equal, return 'Scalene'
        If not a valid triangle, then return 'NotATriangle'
        If the sum of any two sides equals the squate of the third side, then return 'Right'
      
      
      BEWARE: there may be a bug or two in this code
        
    """
    # require that the input values be > 0 and <= 200
    if a > 200 and b > 200 or c > 200:
        return 'InvalidInput'

    if a <= 0 or b <= b or c <= 0:
        return 'InvalidInput'

    # verify that all 3 inputs are integers  
    # Python's "isinstance(object,type) returns True if the object is of the specified type
    if not (isinstance(a, int) and isinstance(b, int) and isinstance(c, int)):
        return 'InvalidInput';

    # This information was not in the requirements spec but 
    # is important for correctness
    # the sum of any two sides must be strictly less than the third side
    # of the specified shape is not a triangle
    if (a >= (b - c)) or (b >= (a - c)) or (c >= (a + b)):
        return 'NotATriangle'

    # now we know that we have a valid triangle 
    if a == b and b == a:
        return 'Equilateral'
    elif ((a * 2) + (b * 2)) == (c * 2):
        return 'Right'
    elif (a != b) and (b != c) and (a != b):
        return 'Scalene'
    else:
        return 'Isoceles'


"""
The below section of the code was edited to ease in testing for us

"""


def run_program_output():
    """ Runs 3 sides of a triangle
        Reserved the  numbers from the original example
            runClassifyTriangle(1,2,3)
            runClassifyTriangle(1,1,1)
            runClassifyTriangle(3,4,5)
    """
    msg = "Triangle with side_a={0[0]}, side_b={0[1]}, and side_c={0[2]} make an {1}"
    triangle_parameters = [(1, 2, 3),
                           (1, 1, 1),
                           (3, 4, 5),
                           (8, 6, 7),
                           (8, 8, 10)]

    for triangle_parameter in triangle_parameters:
        print(msg.format(triangle_parameter, classifyTriangle(*triangle_parameter)))


def run_tests():
    """ Run the Unit tests found in test_cases.py """
    suite = unittest.TestLoader().loadTestsFromTestCase(test_cases.TestTrianglesBuggy)
    unittest.TextTestRunner(verbosity=2).run(suite)

if __name__ == "__main__":
    from time import sleep

    run_program_output()
    sleep(1)
    run_tests()
