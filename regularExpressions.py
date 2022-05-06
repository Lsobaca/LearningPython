# using the re, regular expression, is able to search
# parts of the strings. like using the find and split 
# functions.

# example
import re
hand = open('mbox_short.txt')
for line in hand:
    line = line.rstrip()
    if re.search('From',line):
        print(line)
        

        
# the search method we can get line that we want
# to find. the "^" operator is used to match "the
# beginning" of the line

for line in hand:
    line = line.rstrip()
    if re.search('^From:',line):
        print(line)
        
# using the "." operator on the search we would be
# able to match any character.
for line in hand:
    line = line.rstrip()
    if re.search('^F..m:',line):
        print(line)


# using the "*" or "+" with the search we can match 0 or more
# characters. 
import re
hand = open('mbox_short.txt')
for line in hand:
    line = line.rstrip()
    if re.search('^From:.+@',line):
        print(line)   
        

# to be able to extract data from a string we would use the
# findall() method to extract all of the substrings

import re
S = 'A message from csev@umich.edu to cwen@iupui.edu about meeting @2PM'
lst = re.findall('\S+@\S+',S)
print(lst)
# the '\\S' matches as many non-whitespaces. having '+' after or before the S 
# is would check for one or more non-blankspaces. having the '*' after or before the S
# is would check for none or more non-blackspaces.
 
# this example is extracts the data and it would save them in a list.
import re
f = open('mbox_short.txt')
lst = []
for line in f:
    line = line.rstrip()
    x = re.findall('\S+@\S+',line)
    if len(x) > 0:
        lst.append(x)
print(len(lst))
print(lst)

# after printing the array we can see that some emails have other 
# characters. we can use [a-zA-Z0-9]\S*@\S*[a-zA-Z0-9] as a new 
# regular expression.

import re
f = open('mbox_short.txt')
lst = []
for line in f:
    line = line.rstrip()
    x = re.findall('[a-zA-Z0-9]\S+@\S+[a-zA-Z0-9]',line)
    if len(x) > 0:
        lst.append(x)
print(len(lst))
print(lst)

# this example is where we want to extract the values that start with X-, then print the line
# out one by one
import re
f = open('mbox_short.txt')
for line in f:
    line = line.rstrip()
    if re.findall('^X-\S*: [0-9.]+', line):
        print(line)
 
 
# the "()" is another special character for re. using the '()', it would ingore
# all other characters. using the last example, the output would print out only 
# the values for the lines that start X-
import re
f = open('mbox_short.txt')
for line in f:
    line = line.rstrip()
    x= re.findall('^X-\S*: ([0-9.]+)', line)
    if len(x) > 0:
        print(x)

# another example
import re
f = open('mbox_short.txt')
for line in f:
    line = line.rstrip()
    x = re.findall('^Details:.*rev=([0-9]+)', line)
    if len(x)>0:
        print(x)

# another example
import re
f =open('mbox_short.txt')
for line in f:
    line = line.rstrip()
    x = re.findall('^From .* ([0-9][0-9]):',line)
    if len(x) > 0:
        print(x)
        

# we can put any special character after '\' to look for that symbel
import re
x = 'We just received $10.00 for cookies.'
y = re.findall('\$[0-9.]+',x)
print(y)





