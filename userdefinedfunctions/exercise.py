"""Exercise - User Defined Functions¶
Let us take care of exercises to check whether we understand how to define the functions.

Simple Calculator¶
Let us develop a function called as calc.

It should take 3 arguments
First argument - a of type int
Second argument - b of type int
Third argument - op of type int
If op is 1, the function should return sum of a and b
If op is 2, the function should subtract b from a and return the result
If op is 3, the function should multiply a with b and return the result
If op is 4, the function should divide a by b and return the result
If op is any other number, the function should print saying that invalid op and return nothing"""


def calc(a, b, op):
    if op == 1:
        result = add(a, b)
    elif op == 2:
        result = subtract(a, b)
    elif op == 3:
        result = multiply(a, b)
    elif op == 4:
        result = divide(a, b)
    else: result = "Invalid OP"
    return result


def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    return a / b


print(calc(5, 10, 1))

"""Sum of Integers from 1 to n¶
Develop functions to get sum of integers within a range of 1 to n.

Function Name: sum_n
Argument: n
Perform below validations. If not, raise an exception.
Check if n is integer or not.
Check if n is positive integer or not.
Exception should say {n} is not a valid integer.
You should display the value passed in place of {n} as part of the exception.
The function should return the sum of integers from 1 to n. The logic should be implemented using formula."""

"""Sum of Integers within a range¶
Develop functions to get sum of integers within a range of lower bound and upper bound.

Function Name: sum_of_integers
Argument Names: lb and ub
Check if lb and ub are integers or not. If not, raise an exception. 
Exception should be Either {lb} or {ub} are not integers.
Check if lb is less than ub or not. If not, raise an exception. 
Exception should say {lb} is not lower than {ub}.
You should display the values passed to the function in place of {lb} and {ub} as part of the exception.
The function should return the sum of integers from lb and ub. 
The function should use sum_n to get sum of integers between 1 and upper bound as well as 1 and lower bound."""
