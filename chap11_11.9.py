# xercise 1: Write a simple program to simulate the operation of the grep command on Unix. Ask the user to enter a regular expression and count the number
# of lines that matched the regular expression:
# $ python grep.py
# Enter a regular expression: ^Author
# mbox.txt had 1798 lines that matched ^Author
# $ python grep.py
# Enter a regular expression: ^Xmbox.txt had 14368 lines that matched ^X-
# $ python grep.py
# Enter a regular expression: java$
# mbox.txt had 4218 lines that matched java$

def ex1():
    import re
    f = open('mbox.txt')
    regEx = input('Enter a regular expression: ')
    count = 0
    for line in f:
        line = line.rstrip()
        x = re.findall(f'{regEx}',line)
        if len(x) > 0: count += 1
    print(f'mbox.txt had {count} lines that matched {regEx}')
ex1()    






# Exercise 2: Write a program to look for lines of the form
# `New Revision: 39772`
# and extract the number from each of the lines using a regular expression and
# the findall() method. Compute the average of the numbers and print out the
# average.
# Enter file:mbox.txt
# 38549.7949721
# Enter file:mbox-short.txt
# 39756.9259259

def ex2():
    import re
    total,count = [],0
    fname = input('Enter file name: ')
    try:
        f = open(fname)
    except FileNotFoundError:
        print(f'cant open {fname}')
        
    for line in f:
        line = line.rstrip()
        x = re.findall('^New .*: ([0-9.]+)',line)
        if len(x) > 0: 
            count += 1
            for i in x:
                total.append(int(i))
               
    print(f' {sum(total)/count:.7f}') 
    # print(f' {count}')

ex2()
