"""Exercises - Basic Programming Constructs¶
Please take care of following exercises.
Get sum of integers for a given range."""

lower_limit = int(input("Enter lower limit: ________"))
upper_limit = int(input("Enter upper limit: ________"))

total = 0
for i in range(lower_limit, upper_limit + 1):
    total += i
print(f"Sum: {total}")  # Here complexity is o(n)

"""If you recollect your high school mathematics, there is a formula to get sum of integers for 1 to n. 
It is nothing but (n * (n + 1))/2. 
Using that we should be able to get sum of integers with in a given range between lower bound (lb) and upper bound (ub). 
It is nothing but ((ub * (ub + 1)) / 2) - (((lb - 1) * lb) / 2)"""

res_1 = (upper_limit * (upper_limit + 1)) / 2
print(res_1)

res_2 = ((lower_limit - 1) * lower_limit) / 2
print(res_2)

print(f"Sum: {res_1 - res_2}")  # Here complexity is o(!)

# o(1) is much better solution when compared to o(n).

# Problems to solve.
""" 
1.Get sum of squares of integers for a given range using formula - for 2 to 4, it should be 29. 
You can google around to get the formula for sum of squares of integers for 1 to n.
2.Get sum of even numbers for a given range - for 5 to 10, it should 24.
3.Create a collection using [1, 6, 8, 3, 7, 2, 9] and get sum of even numbers. Answer should be 16.
4.Using the same collection get sum of numbers divisible by 3. Answer should be 18."""

# Solutions given in exercises package.
