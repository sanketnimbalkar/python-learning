""" Conditionals¶
Let us go through conditionals in Python. We typically use “if else” for conditionals.
Let us perform a few tasks to understand how conditionals are developed.
Create a variable i with 5. Write a conditional to print whether i is even or odd."""

i = 5
if i % 2 == 0:
    print(f"{i} is even number")
else:
    print(f"{i} is odd number")

# Ternary operator can be used here.
print(f"{i} is even number") if i % 2 == 0 else print(f"{i} is odd number")

# Take input from user and also check if input value is 0.
number = int(input("Enter number!!!"))

if number == 0:
    print(f"{number} is 0")
elif number % 2 == 0:
    print(f"{number} is even number")
else:
    print(f"{i} is odd number")

# Object of type None is special object which represent nothing. At times we need to check against None.
n = None
print("Not None") if n else print(n)

if number:
    print("Not None")
else:
    print(n)

# We can also perform boolean operations such as boolean or boolean not and boolean and.
if not number % 2 == 0: print(f"{number} is odd")

"""Task 1¶
Determine the category of the infant.
Take age of infant in months as input and check the following.
Print New Born or Baby till 6 months.
Print Toddler from 7 months to 18 months.
Print Teenager from 19 months to 144 months.
Print Youth from 145 months to 216 months"""

age = int(input("Enter infant's age in months:__________"))
if age <= 6:
    print("New Born or Baby")
elif 7 < age <= 18:
    print("Toddler")
elif 19 < age <= 144:
    print("Teenager")
elif 145 < age <= 216:
    print("Youth")

"""Task 2¶
Check if the number is even or divisible by 3."""
if number % 2 == 0 or number % 3 == 0:
    print("Either number is even or divisible by 3")

"""Task 3¶
Check if the number is even and divisible by 3"""
if number % 2 == 0 and number % 3 == 0:
    print("Given number is even and divisible by 3")
elif number % 3 == 0:
    print("Number is divisible by 3")
elif number % 2 == 0:
    print("Number is divisible by 2")
