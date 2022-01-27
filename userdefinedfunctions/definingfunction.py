"""Defining Functions¶
Let us understand how to define functions in Python. Here are simple rules to define a function in Python.
Function blocks begin with the keyword def followed by the function name and parentheses ().
While defining functions we need to specify parameters in these parentheses (if applicable)
The function specification ends with : - (example: def add(a, b):)
We typically have return statement with expression in function body which results in exit from the function and goes back to the caller.
We can have document string in the function."""


# Defining a function.
def get_commission_amount(sales_amt, commission_pct):
    """Function to compute commission amount. commission_pct should be passed as percent notation (eg: 20%)
       20% using percent notation is equal to 0.20 in decimal notation.
    """
    commission_amt = (sales_amt * commission_pct) / 100 if commission_pct else 0
    return commission_amt


print(get_commission_amount(5000, 20))  # Calling a function.
print(help(get_commission_amount))

# Documentation is one of the key aspect related to programming. However, it should be crisp and informative.
# In Python we can use doc strings for the documentation of our code.
# One of the key aspect of documentation is to provide information about usage of a function.
# In Python we can get the information about the function by using help.
# We can get help for a class like str using help(str) and help for a function like str.startswith using help(str.startswith).
# If you want to provide help for user defined function, you can leverage the feature of Doc Strings.
# It is nothing but a string which is provided as first statement in a function.
# Here are some of the characteristics related to Doc Strings:
# By default help returns the function specification.
# Doc String should be the first line in the function body.
# The Doc String should not be assigned to any variable.
# Using """ or ''', we can have multi-line string.
# It is a good practice to provide crisp and concise Doc String for each of the custom function developed.

"""Returning Values¶
Let us understand more about returning values to the caller.
We typically have one or more return statements inside the function body.
The statement return exits a function, we can return back an expression or variable or object to the caller. 
A return statement with no expression is the same as return None.
If there is no return statement in the function body then the function returns None object.
We can return multiple expressions in Python."""


def get_phone_count(employee_id: int, phone_numbers: list):
    valid_count = 0
    invalid_count = 0
    for phone_number in phone_numbers:
        if len(phone_number) != 10:
            invalid_count += 1
        else:
            valid_count += 1
    return valid_count, invalid_count


print(get_phone_count(1, ['1234567890', '245 789 1234', '+1 156 290 1489']))
