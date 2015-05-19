import random
import math
import operator
from functools import reduce
from sympy import *



# Your job is to create better version of create_expression and
# run_expression to create random art.
# Your expression should have a __str__() function defined for it.

#create_expression(): this function takes no arguments and returns an expression that will generate
# a number between -1.0 and 1.0, given x and y coordinates.

#run_expression(expression, x, y): this function takes an expression created by create_expression
#  and an x and y value. It runs the expression, passing the x and y values to it and returns
# a value between -1.0 and 1.0.

x, y = symbols('x y')


def create_expression():
    """This function takes no arguments and returns an expression that
    generates a number between -1.0 and 1.0, given x and y coordinates."""
    expr1 = lambda x, y: (x + y)/2
    expr2 = lambda x, y: (x - y)/2
    expr3 = lambda x, y: x * y
    expr4 = lambda x, y: math.sin(x)*math.sin(y)
    expr5 = lambda x, y: math.sin(x)*math.cos(y)
    expr6 = lambda x, y: math.sin(x/4)*math.sin(y/2)
    expr7 = lambda x, y: (x**2)*(y**2)
    expr8 = lambda x, y: math.sqrt(x)*math.cos(y)
    function_list = []
    function = [expr1, expr2,expr3,expr4,expr5,expr6,expr7,expr8]
    # operators = ['+', '-', '*', '/']
    # for i in range(random.randint(1,10)):
    #     function_list.append(random.choice(function))
    #     function_list.append(random.choice(operators))
    #
    # function_list.pop()
    # expr = Function(function_list)

    return random.choice(function)




def run_expression(expr, x, y):
    """This function takes an expression created by create_expression and
    an x and y value. It runs the expression, passing the x and y values
    to it and returns a value between -1.0 and 1.0."""
    return expr(x, y)
