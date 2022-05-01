# What are dictionaries? 
# dictionaries are like lists but they are more general. 
# it maps "keys" to values.

# the "dict" method creates an empty dictionary
names = dict()
print(names)

# the {} repesents an empty dictionary and to add items to it
# we have to use the [] to create the key then the value
names[1] = 'Luis'
print(names)

# to set up a dictionary we would use the {} the same way how 
# lists are made with []

# using the ":" as a seperator. the left side of the colon, it would 
# be the key and on the right side it would be the value.
names = {1 :'Luis', 2 :'Steve', 3 : 'Gold'}
# when the dictionary is printed with multiple keys and values
# it would print in  a random order
print(names)
eng2esp = {'uno':'one','dos':'two','tres':'three'}
print(eng2esp)

# sometimes the key-value pairs are not the same
# the elements of a dictionary are never indexed with 
# integer indices
print(names[2])

# some functions that the list uses can also work with dictionaries
print(len(names))
print(len(eng2esp))
# using the "in" function we can check if a certain key is in the dictionary
print("one" in eng2esp)
print("uno" in eng2esp)
# to check if there is a value that you want to check with the "in" function
# we would create a new varable creating a list type while using the values() 
# keyword on the dictionary then we would be able to see the value using the
# "in" operator
vals = list(eng2esp.values())
print('one' in vals)
# one the values are in the list
print(vals)

# we can check frequnecies in the dictionary, it is called a histogram
word = 'brontosaurus'
d = dict()
for letter in word:
    if letter not in d:
        d[letter] = 1
    else:
        d[letter] += 1
print(d)

# the dictionaries have a method called "get" that 
# gets the key and the defualt value. if a key is found then
# it would return the key's value and if it does not find it 
# then it returns the default value
counts = {'chuck': 1 ,'annie': 42, 'jan': 100}
print(counts.get('jan'))
print(counts.get('steve',0))

# instead of using for loops we can use the "get" method to do
# the check and the histogram
ge = {}
for s in word:
    ge[s] = ge.get(s,0) + 1
print(ge)

# nested loops are used to get every word on every line of an input
# file.

fname = input('Enter the file name: ')
try:
    fhand = open(fname)
except:
    print('File cannot be opened:', fname)
    exit()
counts = dict()
for line in fhand:
    words = line.split()
    for word in words:
        if word not in counts:
            counts[word] = 1
        else:
            counts[word] += 1
print(counts)


# looping with dictionaries we would use the "for" 
# statement
for keys in counts:
    print(keys,counts[keys])
    

for key in counts:
    if counts[key] > 1:
        print(key,counts[key])
        
# if we want to use the keys and put them in alphabetical order:
lst = list(counts.keys())
print(lst)
lst.sort()
for key in lst:
    print(key, counts[key])     
    
import string
fname = input("Enter file name: ")
try:
    fhand = open(fname)
except:
    print("File cannot be opened")
    exit()
    
counts = {}
for line in fhand:
    line = line.rstrip()
    line = line.translate(line.maketrans('','',string.punctuation))
    line.lower()
    words = line.split()
    for word in words:
        if word not in counts:
            counts[word] = 1
        else:
            counts[word] += 1
print(counts)