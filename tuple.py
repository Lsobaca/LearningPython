# A tuple is a sequence of values much like a list. The values stored in a tuple can
# be any type, and they are indexed by integers. The important difference is that
# tuples are immutable. Tuples are also comparable and hashable so we can sort lists
# of them and use tuples as key values in Python dictionaries.

# it is good practice to have parentheses to  help find the tuple when looking at the 
# python code
from re import M


t = ('a','b','c','d','e')
print(type(t))
# to make sure that the varable is a tuple we have to put a comma or it might be a string
t1 = tuple('lupins')
print(t1)
# printing the element with the index like how lists work
print(t[0])
# slicing also works with tuples
print(t[1:3])
# can not modify a tuple even with using the index of the tuple
#t[0] = 2
# since we cannot modify the elements in a tuple, we can replace one tuple with another
t = ('A',) + t[1:]
print(t)
# we are able to compare tuples too by using the logical operators
print((0,1,2) < (0,2,4))

# example of using DSU. geting a list of words then making them into a tuple, then sort them
# from longest to shortes.
txt = 'but soft what light in yonder window breaks'
words = txt.split()
t = list()
for word in words:
    t.append((len(word), word))
t.sort(reverse=True)
res = list()
for length, word in t:
    res.append(word)
print(res)

# assigning varables to tuple format 
m = ['have','fun']
x,y = m

print(f'{x}')

# if there more values than varables 
# then we would get an error

# using the "item" method we can get a list of tuples.
d={'a':10,'b':1,'c':22}
print(d.items())
g = list(d.items())
print(g)


for key, val in list(d.items()):
    print(val, key)

import string
fhand = open('romeo.txt')
counts = {}
for line in fhand:
    line = line.translate(string.punctuation)
    line = line.lower()
    words = line.split()
    for word in words:
        if word not in counts:
            counts[word] = 1
        else:
            counts[word] += 1
            
lst = []
for key, val in list(counts.items()):
    lst.append((val,key))
    
lst.sort(reverse=True)
for key, val in lst[:10]:
    print(key,val)
     
     
       