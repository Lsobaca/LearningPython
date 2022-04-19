# updating a varable is used when giving a new
# value to an old varable.
"""
    this creates a problem since "x" is not initalzed.
    for x = x + 1 to work, x must be set to zero then 
    we would be able to update the varable
    """
x = 0
x = x + 1
"""
while loops use update statments as ways to end its loop.
since the while loop does not have what the for loop has, 
we have to create a way where we are able to end the loop
with a varable or by using the "break" statement to end the 
loop. the loop can also end if there is a counter on the loop

"""
n = 5
while n >= 0:
    print(n)
    n -= 1
print("Blast Off")

# inifinte loops are when in the while loop has no exit condition
# creating an inifinte loop with a break statement making it stop untill a
# value is inputed

while True:
    line = input("> ")
    if line == "done":
        break
    print(line)
print("Done!")

# sometimes we would want to go through a list of words, list of numbers or 
# through a file

friends = ["steve",'karen','hank']
for i in friends:
    print(f'Happy New Year {i}')


