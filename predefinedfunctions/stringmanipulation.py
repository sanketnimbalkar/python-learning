"""String Manipulation Functions¶
Let us go through some of the important string manipulation functions using Python as programming language.
Splitting Strings
Converting Case
Concatenating Strings
Getting Sub String
Data Type Conversion
Let’s use below string to explore string manipulation functions."""

user = '1,123 456 789,Scott,Tiger,1989-08-15,+1 415 891 9002,Forrest City,Texas,75063'

print(type(user))

"""For split function if sep is not specified or is None, any
whitespace string is a separator and empty strings are
removed from the result. Example below"""
print(user.split())

print(user.split(","))

# Once data is splitted, we can access elements in the result using index
first_name = user.split(',')[2]
print(first_name)

last_name = user.split(',')[3]
print(last_name)

# Converting to upper and lower case.
print(f"Upper Case {first_name.upper()}")
print(f"Lower Case {first_name.lower()}")

# Concatenate string and capitalize
print("Concatenation")
full_name = (first_name + ' ' + last_name).capitalize()
print(full_name)

# Getting year part of the date (substring)
dob = user.split(',')[4]
print(dob)

print(dob[0:4])  # Year part
print(dob[-2:])  # Day part

# Convert year part to integer
print(int(dob[:4]))

# Convert date to date type
import datetime

d = datetime.datetime.strptime(user.split(',')[4], '%Y-%m-%d')
print(type(d))

help(str)  # If you want help on string you can do this. You can explore more functions here.
