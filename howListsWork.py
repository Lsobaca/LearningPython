# how lists work are like how strings work.
# lists are mutable. 
# sometimes some lists do have strings, float, integers, other lists
# inside the list. if there is a list inside of a list then it is called a nested list.

# worinking with lists
from logging import FileHandler


a = ['spam', 12, 1.2, [23, 12]]

numbers = [12, 412]
emptyy = []
print(a, numbers, emptyy)
# changing the value inside the list
numbers[1] = 69
# using the "in" operator with the list would check for the value
# then it would return True. if the value is not in the list then it
# would return false.
print(12 in numbers)
print(32 in numbers)


# List operations
# using the "+" with lists would combine the 2 lists
b = [17, 41, 42]
c = numbers + b
# this would make as much you give it
d = [0]*5

# List methods
# there are some methods that are used to add or remove
# values in a certian list

# the "append" function is used to add a value to an already
# set list.
b.append(32)
# the "extend" function is used to append values from one list
# to another
c.extend(d)
# the "pop" function is used to remove a value at a specific index
x = a.pop(1)
# the pop function would return a value.
print(x)
#the "sort" function would sort a list 
e = [4,3,2,8,97,5,67,47,0]
# pre-sorted
print(e)
e.sort()
# post-sort
print(e)
# when you want to remove a value but you do not know whats its index
e.remove(97)
# if you dont need the value when popping
del e[0]

# getting information from a file 
# with open('mbox_short.txt') as f:
#     for line in f:
#         line.rsplit()
#         if not line.startswith("From"): continue
#         word = line.split()
#         print(word)

# objects and values
# how do we know that the same string is being passed by x &y
# the 2 varables have the same string as there value, but
# are they the same?

x = "banana"
y = "banana"
# the "is" operator checks if they refer to the same object
print(x is y)

a = [1,2,3]
b = [1,2,3]
# using the "is" operator on 2 lists with them having the same values would return false since
# they are not the same object. python creates 2 differnt odjects for the lists
print(a is b)
# since b is now the a list, it would point to the same object as a
b = a
print(a is b)
