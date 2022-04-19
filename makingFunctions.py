# what is a function?
# a function is a sequence of statements
# that does computation. we can call on them
# later or reuse them many more times. sometimes
# they can have arguments or not take in anything

# some functions are already built in such as the math
# module
import math
# would print "w" since w has the highest value
max("hello word")

# type casting is a built in function that would convert 
# the value to the disired value
# this would return '32' 
int('32')+1

# the "." operator on a library module
# would get you acuess to functions from it.
print(math.gcd(3,4))

# creating a new functions or personal. the "def" keyword is
# the function definition.
# the first line of the definition is called the header and the
# rest is called the body.
def printsong():
    print("I'm a lumberjack, and I'm okay.")
    print("I sleep all night and I work all day.")
# would print the address of the function in the memory
print(printsong)
# prints <class function>
print(type(printsong))
# functions that return nothing are called void functions
def repeatSong():
    printsong()
    printsong()

repeatSong()

# this is a function that takes a parameters then it would print out 
# what ever it has un the body.
def takesSomething(secs)->str:
    return(f'It would take {secs} seconds to print.')
# runs the function with 3 as a parameter
takesSomething(3)

print(type(takesSomething))