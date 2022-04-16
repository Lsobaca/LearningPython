# what are conditions in python
# they are boolean values that would
# return True or False


x = 2
print (x == 2) # would return true
print(x==3) # would return false
print(x<3) # would return true
# these are basic boolean factors that would check if they are 
# true or false.

# Boolen operators

# name and age are variables for this to work
name = "Steve"
age  = 25
# the if statement is the same as other languages. 
# it is there for when you want to check for a certian 
# value. 
#
# the operators "and" and "or" are the same as "&&" and "||" from C++
if name == "Steve" and age == 25:
    print("Your name is Steve, and you are also 25 years old.")
if name == "Steve" or name=="Rick":
    print("Your name is either Steve or Rick")
# the "in" operator is used look inside specified odjects exists
# within an iterable object contaioner like a list
if name in ["Steve","Rick", "John"]:
    print("Your name is either John or Steve")
# the "is" operator is not the same as "==". "is" compares the instances
# while the "==" compares the values themselves.
x = [1,2,3]
y = [1,2,3]
print(x==y)
print(x is y)
# the "not" operator is the same as "!" in C++
print(not True)

