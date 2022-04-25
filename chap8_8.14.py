# Exercise 1:
# Write a function called chop that takes a list and modifies it, removing the first
# and last elements, and returns None.
# Then write a function called middle that takes a list and returns a new list that
# contains all but the first and last elements.
from xml.dom import ValidationErr


def chop(lite):
    del lite[0]
    del lite[-1]
    
ar = [1,2,3,4,5]
chop(ar)
print(ar)

def middle(art):
    return art[0:-1]
print(ar)

# Exercise 2: Figure out which line of the above program is still not properly guarded.
# See if you can construct a text file which causes the program to fail and then modify
# the program so that the line is properly guarded and test it to make sure it handles
# your new text file.
# fhand = open('mbox_short.txt')
# count = 0
# for line in fhand:
#     words = line.split()
# # print 'Debug:', words
#     if len(words) == 0 : continue
#     if words[0] != 'From' : continue
# print(words[2])



# Exercise 3: Rewrite the guardian code in the above example without two if statements. Instead, use a compound logical expression using the and logical operator
# with a single if statement.
fhand = open('mbox_short.txt')
count = 0
for line in fhand:
    words = line.split()
    if len(words) == 0 and words[0] != 'From': continue
    print(words) 



# Exercise 4: Download a copy of the file from www.pythonlearn.com/code3/romeo.txt
# Write a program to open the file romeo.txt and read it line by line. For each line,
# split the line into a list of words using the split function.
# For each word, check to see if the word is already in a list. If the word is not in
# the list, add it to the list.
# When the program completes, sort and print the resulting words in alphabetical
# order.
# Enter file: romeo.txt
# ['Arise', 'But', 'It', 'Juliet', 'Who', 'already',
#  'and', 'breaks', 'east', 'envious', 'fair', 'grief',
#  'is', 'kill', 'light', 'moon', 'pale', 'sick', 'soft',
#  'sun', 'the', 'through', 'what', 'window',
#  'with', 'yonder']
def ex4():
    the_list =[]
    fhand = open('romeo.txt')
    for lines in fhand:
        words = lines.split()
        for word in words:
            if word == the_list: continue
            the_list.append(word)
    the_list.sort()   
    print(the_list)
ex4()
# Exercise 5: Write a program to read through the mail box data and when you
# find line that starts with “From”, you will split the line into words using the split
# function. We are interested in who sent the message, which is the second word on
# the From line.
# From stephen.marquard@uct.ac.za Sat Jan 5 09: 14: 16 2008
# You will parse the From line and print out the second word for each From line,
# then you will also count the number of From (not From:) lines and print out a
# count at the end.
# This is a good sample output with a few lines removed:
# python fromcount.py
# Enter a file name: mbox-short.txt
# stephen.marquard@uct.ac.za
# louis@media.berkeley.edu
# zqian@umich.edu
# [...some output removed...]
# ray@media.berkeley.edu
# cwen@iupui.edu
# cwen@iupui.edu
# cwen@iupui.edu
# There were 27 lines in the file with From as the first word
def ex5():
    try:
        count = 0
        fhand = open(input('Enter a file name: '))
        for lines in fhand:
            words = lines.split()
            if len(words) < 3 or words[0] != 'From': continue
            count+=1
            print(f'{words[1]}')
        print(f'There are {count} lines in the file with From as the first word')
    except ValidationErr:
        print("Error")
ex5()




# Exercise 6: Rewrite the program that prompts the user for a list of numbers and
# prints out the maximum and minimum of the numbers at the end when the user
# enters “done”. Write the program to store the numbers the user enters in a list
# and use the max() and min() functions to compute the maximum and minimum
# numbers after the loop completes.
# Enter a number: 6
# Enter a number: 2
# Enter a number: 9
# Enter a number: 3
# Enter a number: 5
# Enter a number: done
# Maximum: 9.0
# Minimum: 2.0
def ex6():
    number_list = []
    while True:
        try:
            num = (input('Enter a number: '))
            if num == 'done': break
            number_list.append(float(num))
        except ValueError:
            print('Not a number!')
    print(f'Maximun: {max(number_list)}')
    print(f'Minimum: {min(number_list)}')
ex6()