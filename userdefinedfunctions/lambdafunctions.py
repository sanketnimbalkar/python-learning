"""Lambda Functions¶
Let us get an overview of Lambda Functions in Python.
They are also known as anonymous functions in other programming languages.
A lambda function is a function which does not have name associated with it.
It starts with the keyword lambda.
Typically, we have simple one liner as part of lambda functions.
There are restrictions while passing or creating lambda functions.
You cannot have return statement
Assignment operation is not allowed
Use lambda functions only when the functionality is simple and not used very often.
"""


def my_sum(lb, ub, f):
    total = 0
    for j in range(lb, ub + 1):
        total += f(j)
    return total


def i(n): return n  # typical function, for lambda def and function are replaced by keyword lambda


print(my_sum(5, 10, i))
print(my_sum(10, 20, lambda x: x))
print(my_sum(5, 10, lambda x: x * x))


def even(n): return n if n % 2 == 0 else 0  # Another example for typical function


print(my_sum(10, 20, even))

print(my_sum(10, 20, lambda x: x if x % 2 == 0 else 0))

"""Usage of Lambda Functions¶
Lambda functions are typically used while invoking those functions which take functions as arguments. 
Here are some of the functions which take other functions as arguments.
filter
map
sorted or sort and more
There are many Python modules which have functions which take other functions as arguments. 
We will see quite a lot of examples in upcoming chapters."""

users = [
    '1,Bryn,Eaken,beaken0@cbc.ca,Female,236.34.175.186',
    '2,Smith,Combe,scombe1@xing.com,Male,',
    '3,Roland,Wallentin,rwallentin2@aboutads.info,Male,94.67.195.44',
    '4,Charlotta,Richten,crichten3@wikia.com,Female,202.51.201.1',
    '5,Berne,Coyne,bcoyne4@squarespace.com,,150.246.120.53',
    '6,Kesley,Hakonsen,khakonsen5@cbc.ca,Female,227.61.48.174',
    "7,Gray,M'Barron,gmbarron6@altervista.org,Male,190.128.200.183",
    '8,Melinde,Scarf,mscarf7@diigo.com,Female,134.41.141.5',
    '9,Arturo,Warkup,awarkup8@nifty.com,Male,',
    '10,Annette,Lowthorpe,alowthorpe9@marketwatch.com,Female,63.157.95.191',
    '11,Melinda,McOwen,mmcowena@unblog.fr,Female,73.95.183.60',
    '12,Minnie,Andrivel,mandrivelb@storify.com,,131.194.233.209',
    '13,Taryn,Medhurst,tmedhurstc@ebay.co.uk,Female,65.191.102.59',
    '14,Fanni,Whitley,fwhitleyd@who.int,Female,184.210.235.118',
    '15,Jareb,Thunderchief,jthunderchiefe@arizona.edu,Male,150.159.27.112',
    '16,Sharona,Haffard,shaffardf@kickstarter.com,Female,91.125.183.157',
    '17,Pattin,Basant,pbasantg@gov.uk,Male,162.227.228.164',
    '18,Beatrice,Butler,bbutlerh@abc.net.au,Female,139.49.169.236',
    '19,Linoel,Bucktrout,lbucktrouti@google.ru,Male,18.17.136.105',
    '20,Katee,Aveyard,kaveyardj@feedburner.com,Female,60.25.33.89'
]

print(type(users))
print(type(users[0]))

# If we want to filter based on Male.
males = filter(lambda user: user.split(',')[4] == 'Male', users)
print(len(list(males)))

# Filter based on Male and female.
male_female = filter(lambda user: user.split(',')[4] in ('Male', 'Female'), users)
# print(list(male_female))
print(f"Length------->{len(list(male_female))}")

user_ips = map(lambda user: (int(user.split(',')[0]), user.split(',')[-1]), users)
print(list(user_ips))

sort_gender = sorted(users, key=lambda user: (user.split(',')[4], user.split(',')[0]))
print(list(sort_gender))
