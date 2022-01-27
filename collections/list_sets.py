"""Overview of list and set¶
There are 4 types of collections in Python.
While list and set fundamentally contain homogeneous elements, dict and tuple contain heterogeneous elements.

Homogeneous means of same type.
Examples of collections with homogeneous elements.
Collection of employees - list
Collection of unique employees - set
Collection of integers - list
Collection of unique integers - set
Based up on the requirement we should use appropriate type of collection.
list
Group of homogenous elements.
There can be duplicates in the list.
list can be created by enclosing elements in [] - example [1, 2, 3, 4].
Empty list can be initialized using [] or list().
set
Group of homogenous elements
No duplicates allowed in the set. Even if you add same element more than once, such elements will be ignored.
set can be created by enclosing elements in {} - example {1, 2, 3, 4}.
Empty set can be initialized using set().
We cannot initialize empty set using {} as it will be treated as empty dict.
list and set can be analogous to Table with columns and rows while dict and tuple can be analogous to a row with in a table.
list can hold duplicate values while set can only hold unique values.
If you want to have a row with column names then we use dict otherwise we use tuple.
We will deep dive into all types of collections to get better understanding about them."""

# Create List
l = [1, 2, 3, 4, 5, 6]
print(l)
print(type(l))
# Empty List.
l = []
print(l)

# Create Set.
s = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
print(s)
print(type(s))

# Empty Set.
s = set()
print(s)

"""Common Operations¶
There are some functions which can be applied on all collections. 
Here we will see details related to list and set.

in - check if element exists
len - to get the number of elements.
sorted - to sort the data (original collection will be untouched). 
Typically, we assign the result of sorting to a new collection.
sum, min, max, etc - arithmetic operations.
There can be more such functions."""

l = [6, 3, 2, 4, 1, 5]
print(1 in l)
print(8 in l)
print(len(l))
print(sorted(l))
print(sum(l))

# Similarly above functions can be used for Set.

"""Accessing Elements from list¶
Let us see how we can access elements from the list using Python as programming language.

We can access a particular element in a list by using index l[index]. Index starts with 0.
We can also pass index and length up to which we want to access elements using l[index:length]
Index can be negative and it will provide elements from the end. We can get last n elements by using l[-n:].
Let us see few examples."""