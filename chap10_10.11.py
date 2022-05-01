# Exercise 1: Revise a previous program as follows: Read and parse the “From”
# lines and pull out the addresses from the line. Count the number of messages from
# each person using a dictionary.
# After all the data has been read, print the person with the most commits by
# creating a list of (count, email) tuples from the dictionary. Then sort the list in
# reverse order and print out the person who has the most commits.
# Sample Line:
# From stephen.marquard@uct.ac.za Sat Jan 5 09:14:16 2008
# Enter a file name: mbox-short.txt
# cwen@iupui.edu 5
# Enter a file name: mbox.txt
# zqian@umich.edu 195
def ex1():
    emails = dict()
    fname = input("Enter file name: ")
    try:
        f = open(fname)
    except FileNotFoundError:
        print(f"can not open file {fname}")
    
    for lines in f:
        words = lines.split()
        if len(words) < 3 or words[0] != 'From': continue
        if words[1] not in emails:
            emails[words[1]] = 1
        else:
            emails[words[1]] += 1 
        
    lst = []
    for key,val in list(emails.items()):
        lst.append((val,key))
    lst.sort(reverse=True)
    for key,val in lst[:1]:
        print(val,key)
ex1()

# Exercise 2: This program counts the distribution of the hour of the day for each
# of the messages. You can pull the hour from the “From” line by finding the time
# string and then splitting that string into parts using the colon character. Once
# you have accumulated the counts for each hour, print out the counts, one per line,
# sorted by hour as shown below.
# Sample Execution:
# python timeofday.py
# Enter a file name: mbox-short.txt
# 04 3
# 06 1
# 07 1
# 09 2
# 10 3
# 11 6
# 14 1
# 15 2
# 16 4
# 17 2
# 18 1
# 19 1
def ex2():
    time = {}
    fhand = input('Enter a file name: ')
    try:
        f = open(fhand)
    except FileNotFoundError:
        print('Not found')
    
    for line in f:
        words = line.split()
        if len(words)<3 or words[0] != 'From':continue
        atHour = words[5].find(':')
        times = words[5][:atHour]
        if times not in time:
            time[times] = 1
        else:
            time[times] += 1
    # print(time)
    lst =[]
    for keys,val in list(time.items()):
        lst.append((keys,val))
    lst.sort()
    for key,val in lst:
        print(key,val)    
ex2()


# Exercise 3: Write a program that reads a file and prints the letters in decreasing
# order of frequency. Your program should convert all the input to lower case and
# only count the letters a-z. Your program should not count spaces, digits, punctuation, or anything other than the letters a-z. Find text samples from several different
# languages and see how letter frequency varies between languages. Compare your
# results with the tables at wikipedia.org/wiki/Letter_frequencies
import string
def ex3():
    letters = {}
    count=0
    fhand =input("Enter file name: ")
    try:
        f = open(fhand)
    except FileNotFoundError:
        print(f'{fhand} is not found')
    for line in f:
        line = line.translate(string.punctuation)
        line = line.lower()
        words = line.split()
        for word in words:
            for letter in word:
                if letter not in letters:
                 letters[letter] = 1
                 count +=1
                else:
                 letters[letter] += 1
                 count +=1
    # print(letters)
    lst = []
    for keys,val in list(letters.items()):
        lst.append((keys,val))
    lst.sort()
    for key,val in lst:
        print(f'{key} {val/count:.2f}')
    
    
ex3()
