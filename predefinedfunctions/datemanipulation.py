"""Date Manipulation Functions¶
As part of our application, we often need to deal with dates.
Let us get an overview about dealing with dates in Python.
datetime is the main library to deal with dates.
datetime.datetime and datetime.date are the classes as part of datetime library that can be used to deal with dates.
datetime.datetime is primarily used for date with timestamp and datetime.date can be used for date with out timestamp.
When we try to print the date it will print as below (for datetime).
It is due to the implementation of string representation functions such as __str__ or __repr__.
datetime.datetime(2020, 10, 7, 21, 9, 1, 39414)
We need to format the date using format string to display the date the way we want.
These are typically used along with functions such as strptime and strftime.
%Y - 4 digit year
%m - 2 digit month
%d - 2 digit day with in month
There are quite a few other format strings, but these are the most important ones to begin with.
Also, datetime library provides functions such as strptime to convert strings to date objects.
Other important modules to manipulate dates.
calendar - to get the calendar related information for dates such as day name, month name etc.
datetime.timedelta - to perform date arithmetic"""

# Importing datetime
import datetime as dt

# Getting current date with timestamp.
print(dt.datetime.now())

# Getting current date without timestamp.
from datetime import date

print(date.today())

# Converting date to a string in the form of yyyy-MM-dd (2020-10-07)
print(date.today().strftime('%Y-%m-%d'))

# Converting date to a string in the form of dd-MM-yyyy (07-10-2020)
print(date.today().strftime('%d-%m-%Y'))

# Converting date to a string in the form of yyyy/MM/dd (2020/10/07)
print(date.today().strftime('%Y/%m/%d'))

# Converting date to an integer in the form of yyyyMMdd (20201007)
print(int(date.today().strftime('%Y%m%d')))

# Converting string which contains date using format yyyy-MM-dd as date
print(dt.datetime.strptime('2022-01-24', '%Y-%m-%d'))

# Converting number which contains date using format yyyyMMdd as date
# strptime expects first argument to be string which contain date
# so we need to convert datatype of number to string
print(dt.datetime.strptime(str(20220122), '%Y%m%d'))

# Converting string which contains timestamp using format yyyy-MM-dd HH:mm:ss as date
dt.datetime.strptime('2020-10-07 21:09:10', '%Y-%m-%d %H:%M:%S')

# Importing calendar
import calendar, datetime as dt

d = dt.datetime.today()
print(d)

print(list(calendar.day_name))

# Get year month and day of respective date.
print(d.year)
print(d.month)
print(d.day)

# Get weekday of respective date.
print(calendar.weekday(d.year, d.month, d.day))

# Using weekday we can get day name.
print(calendar.day_name[calendar.weekday(d.year, d.month, d.day)])
