# useing the "for" key word is the start of a loop where
# "in" should be used when there is the range or an iterable list 
primes = [2,3,5,7]
for prime in primes:
    print(prime)
# it is going to print the numbers from 0 - 4
# it happens since the starting number is 0 and 
# the program is going to run 5 times
for x in range(5):
    print(x)
# it is going to print numbers from 3 - 6
for x in range(3,6):
    print(x)
# when "range" has 3 numbers in it. the first 2 is going to be the 
# range and the 3rd number is the amount the numbers that are going
# to be skipped
for x in range(3,8,2):
    print (x)
# using the "while" keyword is the same of 
count = 0
while count<5:
    print(count)
    count+=1
# using a while loop with an else statement as 
count2=0
while count2<5:
    print(count2)
    count2+=1
else:
    print("count value reached %d" %(count2))
# using the break statement to get out of a for loop.
for i in range(1,10):
    if(i%5==0):
        break
    print(i)
else:
    print("this is not printed")
