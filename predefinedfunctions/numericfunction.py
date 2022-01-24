"""Numeric Functions¶
Let us understand some of the common numeric functions we use with Python as programming language.
We have functions even for standard operators such as +, -, *, / under a library called as operator.
However, we use operators more often than functions.
add for +
sub for -
mul for *
truediv for /
We can use pow for getting power value.
We also have math library for some advanced mathematical operations.
Also, we have functions such as min, max to get minimum and maximum of the numbers passed."""

print(4 + 5)

print(5 % 4)

from operator import add, truediv

print(add(4, 5))

print(truediv(4, 5))

from operator import mod

print(mod(5, 4))

print(pow(2, 3))  # This is also available under math library

import math

print(math.ceil(4.4))

print(math.floor(4.7))

print(round(4.4))

print(round(4.7))

print(round(4.662, 2))

print(math.sqrt(2))

print(math.pow(2, 3))

print(min(2, 3))

print(max(2, 3, 5, 1))
