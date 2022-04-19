
# Exercise 1: Write a while loop that starts at the last character in the string and
# works its way backwards to the first character in the string, printing each letter on
# a separate line, except backwards
fruit = 'banana'
i = len(fruit)-1
while i >= 0 :
    print(fruit[i])
    i-=1

# Exercise 2: Given that fruit is a string, what does fruit[:] mean?
# it would mean that the string is going to be printed out

# Exercise 3:
# Encapsulate this code in a function named count, and generalize it so that it
# accepts the string and the letter as arguments.

def count(string, word)->int:
    count = 0
    for i in string:
        if i == word:
            count+=1
    return count
count(fruit,"a")  


# Exercise 4:
# There is a string method called count that is similar to the function
# in the previous exercise. Read the documentation of this method at
# https: // docs.python.org/3.5/library/stdtypes.html  # string-methods and write an
# invocation that counts the number of times the letter a occurs in “banana”.


# Exercise 5: Take the following Python code that stores a string: ‘
# str = ’X-DSPAM-Confidence: 0.8475’
# Use find and string slicing to extract the portion of the string after the colon
# character and then use the float function to convert the extracted string into a
# floating point number.
string = 'X-DSPAM-Confidence: 0.8475'

