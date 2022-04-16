# -*- coding: utf-8 -*-
"""
Created on Tue Apr 12 14:49:21 2022

Playing with strings


@author: lsoba
"""


astring ='hello world'
astring2 = "Hello World"
alist = [1,3.9,78,3,8,0,0,3,7,9]

# prints the length of a varable if it is 
# scriptable
print(len(alist))
# finds the first time the value is located
print(alist.index(0))
# finds how many times the value is a string or in 
# array
print(alist.count(3))
# this is how to slice a string/list where the first
# number is the starting point or starting index and 
# the ":" operator is the one that comands the slice
# lastly the 2nd number is the end point of the slice
# with 'alist' the slice of [3:7] would yeld [3,8,0,0]
print(alist[3:7])
# to have the 1st number then ":" with leaving it blank
# we would slice the list where the 2nd value starts then 
# print out the rest of the list. from index 2 - index N 
# would be printed
print(alist[2:])
# to have the ":" then the number number. it would print out
# the whole list until the index of the number after the ":"
# is up. so  from 0 - 7 would be printed out in the print
# statement
print(alist[:8])
# putting a "-" on the "[]" then a number would lead to print
# the index from the end 
print(alist[-4])
# works the same way as line 37 just in reverse
print(alist[:-4])
# works the same way as line 32 just in reverse
print(alist[-4:])
# the list is going to be sliced then the number 2 is going to be 
# the amount of times an index is going to be skiped.
print(alist[3:7:2])
# this prints out the list in reverse aka the inverse
print(alist[::-1])
# returns true if the start of the string starts with 
# a word or letter in the string
print(astring.startswith("o"))
# like the startswith function, the endswith would look at the
# string then check if the string ends with whatever you are 
# looking for. it would return true if the end of the string 
# ended with what you were looking for.
print(astring.endswith("euwrwq"))
# making a new varable to see how the split function would work
# on a string. the varible becomes a list of strings
splitwords = astring.split(" ")
# prints out what splitwords is. a list should show up
print(splitwords)
