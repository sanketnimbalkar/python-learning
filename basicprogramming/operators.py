"""As any programming language Python supports all types of Operations. There are several categories of operators.
For now we will cover Arithmetic and Comparison Operators.

Arithmetic Operators
Addition (+)
Subtraction (-)
Multiplication (*)
Division (/)
Mod (%) returns reminder
+ is also used for concatenation of strings.
Comparison Operators - typically return boolean value (True or False)
Equals (==)
Not Equals (!=)
Negation (! before expression)
Greater Than (>)
Less Than (<)
Greater Than or Equals To (>=)
Less Than or Equals To (<=)"""

# Task 1 add two integer and check

i1 = 10
i2 = 20

res_i = i1 + i2

print(res_i)
print(type(res_i))

# Task 2 add two float and check.

f1 = 10.5
f2 = 15.6

res_f = f1 + f2

print(res_f)
print(type(res_f))

# Task to add float and int and check.

v1 = 5
v2 = 10.0

res_v = v1 + v2

print(res_v)
print(type(res_v))

# Create object or variable s of type string for value Hello World and print on the screen. Check the type of s.
s = "Hello 'World'"
print(s)
print(type(s))

# Create 2 string objects s1 and s2 with values Hello and World respectively and concatenate with space between them.
s1 = "Hello"
s2 = "World"
print(s1 + ' ' + s2)
print(f'{s1} {s2}')  # You can do like this also.

# Compare whether i1 and i2 are equal and assign it to a variable res_e, then check the type of it.
res_e = i1 == i2  # You can try other operations as well.
print(res_e)
print(type(res_e))

# Question
f1 = 10.1
f2 = '20.2'
res_f = f1 + float(f2)
""" Throws operand related error as there is no overloaded function +
between float and string. Convert string to float """
print(res_f)
