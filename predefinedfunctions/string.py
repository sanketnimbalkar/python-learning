"""Overview of Strings¶
Let us get an overview of how strings are used in Python.
str is the class or type to represent a string.
A string is nothing but list of characters.
Python provides robust set of functions as part of str to manipulate strings.
As str object is nothing but list of characters,
we can also use standard functions available on top of Python collections such as list, set etc."""

s = "Hello World"

print(type(s))
print(s)

# Lets perform some operations on above string and see the result.
print(s[:5])
print(s[-5:])
print(len(s))
print(sorted(s))

# String in Python can be represented in different ways
# Enclosed in single quotes - 'Hello World'
# Enclosed in double quotes - "Hello World"
# Enclosed in triple single quotes - '''Hello World'''
# Enclosed in triple double quotes - """Hello World"""
# If your string itself have single quote, enclose the whole string in double quote.
# If your string itself have double quote, enclose the whole string in single quote.
# Triple single quotes or triple double quotes can be used for multi line strings.

