# files are in the secondary memory where it can be saved
# usb(s) save the program in flash memory and you are able to
# transport the program to other computers and the files come too.

# to open the file we use the "open" operator to be able to  open the 
# file. if the file exists then it would open the file but if the file 
# does not exist then the IDE would give a TraceBack call.

fhand = open('mbox.txt')
print(fhand)

# when a file is not found. it gives out an error
fhand = open("stiff.txt")
print(fhand)

# reading files
fhand = open('mbox_short.txt')
count = 0
for line in fhand:
    count+=1
print(f'Line count: {count}')

# the file closes if i do not do another action
fhand = open('mbox_short.txt')
imp = fhand.read()
# prints how many letters there are in the file.
print(len(imp))
# the same as string slices
print(imp[:20])

# searching through a file
fhand = open('mbox_short.txt')
count = 0
for line in fhand:
    if line.startswith('From:'):
        print(line)
        
# prints the above action but with no spaces inbetween
for line in fhand:
    line = line.strip()
    if line.startswith("From:"):
        print(line)
        
# the action is going to find the address then print it out 
fhand = open('mbox_short.txt')     
for line in fhand:
    line.rstrip()
    if line.find("@uct.ac.za")==-1: continue
    print(line)

# making the user choose what file should be openned
fname = input("Enter the file name: ")
fhand = open(fname)
count = 0
for line in fhand:
    if line.startswith("Subject:"):
        count+=1
print(f'There are {count} with the subject in {fname}')

# using the try catch to have the input that the user puts in is going to work
count = 0
try:
    fname = input("Enter the file name: ")
    fhand = open(fname)
except:
    print("The file cannot open")
for line in fhand:
    if line.startswith("Subject:"):
        count += 1
print(f'There are {count} with the subject in {fname}')




fhand.close()
    