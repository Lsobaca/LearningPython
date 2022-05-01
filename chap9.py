# Exercise 1: [wordlist2]
# Write a program that reads the words in words.txt and stores them as keys in
# a dictionary. It doesn’t matter what the values are. Then you can use the in
# operator as a fast way to check whether a string is in the dictionary
from xml import dom


with open('words.txt') as f:
    word_dic = {}
    for line in f:
        words = line.split()
        for word in words:
            if word not in word_dic:
                word_dic[word] = 1
            else:
                word_dic[word] += 1    
print(word_dic)        

# Exercise 2: Write a program that categorizes each mail message by which day of
# the week the commit was done. To do this look for lines that start with “From”,
# then look for the third word and keep a running count of each of the days of the
# week. At the end of the program print out the contents of your dictionary (order
# does not matter).
# Sample Line:
# From stephen.marquard@uct.ac.za Sat Jan 5 09:14:16 2008
# Sample Execution:
# python dow.py
# Enter a file name: mbox-short.txt
# {'Fri': 20, 'Thu': 6, 'Sat': 1}
dictionary_days = dict()                       # Initializes the dictionary
fname = input('Enter a file name: ')
try:
    fhand = open(fname)
except FileNotFoundError:
    print('File cannot be opened:', fname)
    exit()

for line in fhand:
    words = line.split()
    if len(words) < 3 or words[0] != 'From':
        continue
    else:
        if words[2] not in dictionary_days:
            dictionary_days[words[2]] = 1       # First entry
        else:
            dictionary_days[words[2]] += 1      # Additional counts

print(dictionary_days)

# Exercise 3: Write a program to read through a mail log, build a histogram using
# a dictionary to count how many messages have come from each email address, and
# print the dictionary.
# Enter file name: mbox-short.txt
# {'gopal.ramasammycook@gmail.com': 1, 'louis@media.berkeley.edu': 3,
# 'cwen@iupui.edu': 5, 'antranig@caret.cam.ac.uk': 1,
# 'rjlowe@iupui.edu': 2, 'gsilver@umich.edu': 3,
# 'david.horwitz@uct.ac.za': 4, 'wagnermr@iupui.edu': 1,
# 'zqian@umich.edu': 4, 'stephen.marquard@uct.ac.za': 2,
# 'ray@media.berkeley.edu': 1}
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
        
print(emails)


# Exercise 4: Add code to the above program to figure out who has the most
# messages in the file.
# After all the data has been read and the dictionary has been created, look through
# the dictionary using a maximum loop (see Section [maximumloop]) to find who
# has the most messages and print how many messages the person has.
# Enter a file name: mbox-short.txt
# cwen@iupui.edu 5
# Enter a file name: mbox.txt
# zqian@umich.edu 195
def ex4():
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
    
    max_vals = max(list(emails.values()))
    for keys in emails:
        if emails[keys] == max_vals:
            print(keys,emails[keys])
        
ex4()


# Exercise 5: This program records the domain name (instead of the address) where
# the message was sent from instead of who the mail came from (i.e., the whole email
# address). At the end of the program, print out the contents of your dictionary.
# python schoolcount.py
# Enter a file name: mbox-short.txt
# {'media.berkeley.edu': 4, 'uct.ac.za': 6, 'umich.edu': 7,
# 'gmail.com': 1, 'caret.cam.ac.uk': 1, 'iupui.edu': 8}
def ex5():
    emails = dict()
    fname = input('Enter file name: ')
    try:
        f = open(fname)
    except FileNotFoundError:
        print(f'Cannot open {fname}')
        exit()
    for lines in f: 
        words = lines.split()
        if len(words) < 2 or words[0] != 'From':continue
        atpos = words[1].find('@')               # Position of '@'
        domain = words[1][atpos + 1:]  
        if domain not in emails:
            emails[domain] = 1
        else:
            emails[domain] += 1
    print((emails))
ex5()