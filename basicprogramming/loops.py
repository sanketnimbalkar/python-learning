"""All about for Loops¶
Let us understand how we can loop through using for in Python.

Go through range between 2 integers (5 and 10) and print them.
We can use range function to get range between two integers."""

print(range(5, 10))

print(list(range(5, 11)))

# If you want to increment the numbers with 2 then use.
print(list(range(5, 11, 2)))

# Use this range function in for loop and print the numbers.
for i in range(5, 11): print(i)

"""Create a list of 7 elements and print alternate numbers starting from 1. [1, 6, 8, 3, 7, 2, 9]
In this example we are using list. 
It will be covered extensively at a later point in time. list is one of the core Python Data Structures."""

list_a = [1, 6, 8, 3, 7, 2, 9]
print(type(list_a))
for i in range(0, len(list_a)):
    if i % 2 == 0:
        print(list_a[i])

# Go through range between 2 integers (5 and 15) and print even numbers.
for i in range(5, 15):
    if i % 2 == 0:
        print(i)

# Create List of months. Iterate through and print them.
list_month = ["January", "February", "March"]
for i in list_month:
    print(i)

# Other ways to iterate through months.
import calendar

print(list(calendar.month_name))

# You can exclude 1st element from list like this.
for i in list(calendar.month_name)[1:]:
    print(i)

"""Task 1¶
Take the list of ages and determine the category of the baby.
Print New Born or Infant till 6 months.
Print Toddler from 7 months to 18 months.
Print Grown up from 19 months to 144 months.
Print Youth from 145 months to 216 months"""

ages = [10, 24, 37, 100, 250]
for age in ages:
    if age <= 6:
        print("New Born or Baby")
    elif 7 < age <= 18:
        print("Toddler")
    elif 19 < age <= 144:
        print("Teenager")
    elif 145 < age <= 216:
        print("Youth")

"""Task 2¶
Check if each number in list of integers is even or divisible by 3."""
number = [3, 18, 45, 100, 99]

for n in number:
    if n % 2 == 0 or n % 3 == 0:
        print("Either number is even or divisible by 3")

"""Task 3¶
Check if the number in list of integers is even and divisible by 3"""
for n in number:
    if n % 2 == 0 and n % 3 == 0:
        print("Given number is even and divisible by 3")
    elif n % 3 == 0:
        print("Number is divisible by 3")
    elif n % 2 == 0:
        print("Number is divisible by 2")

"""Task 4¶
Check if each salary in list of salaries is valid. 
If the salary is negative or 0, then print Salary {salary_amount} is invalid. 
If the salary is None then print Salary is Not Available."""

salary = [20000, 3000000, 0, None, -20000]
for i in salary:
    if i == None:
        print("Salary is Not Available")
    elif i <= 0:
        print(f"Salary {i} is invalid")
