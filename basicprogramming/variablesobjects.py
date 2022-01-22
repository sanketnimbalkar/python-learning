"""Variables and Objects¶
Let us get an overview about variables and objects in Python.
In Python we need not define data types for variables or objects.
Data types are inherited based up on the values assigned to the variables.
We can check the type of the variable or object using type function.
Python is interpreter based programming language which means it does not go through compilation and
hence data types are not validated until run time.
Python variables or objects are dynamically typed.
In case of compiler based programming languages such as Java, Scala etc variables or objects are statically typed.
We can specify data types for variables or objects starting from Python 3.
However it is only informational and does not enforce."""

i = 10

print(type(i))

j: int = 10

j = 'Hello'

print(j)

print(type(j))

print(type(j) == str)
