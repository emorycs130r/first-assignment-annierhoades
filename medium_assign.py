'''

This file contains the functions that you need for completing this assignment. 

1. expression_1() --> 30%
2. expression_2() --> 40%
3. expression_3() --> 30% 

Failure to follow the variable name guides will lead to reduction of 10 points. 

DO NOT EDIT THE FUNCTION NAMES.


'''

def expression_1(x):
    answer_1 = x**3 - (2*x + (x**2)) - 100
    return answer_1

def expression_2(x, y):
    answer_2 = (x**4 / 2*y) - (3*x*y) + ((6*y) / (7*x))
    return answer_2


def expression_3(x, y):
    answer_3 = ((x**3) + (y**2)) / ((x**2) - (y**3))
    return answer_3

if __name__ == "__main__":
    print(expression_1(2))
    print(expression_2(2,3))
    print(expression_3(2,3))