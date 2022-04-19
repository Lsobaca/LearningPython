# Exercise 4: What is the purpose of the “def” keyword in Python?
# a) It is slang that means “the following code is really cool”
# b) It indicates the start of a function        this is the answer
# c) It indicates that the following indented section of code is to be stored for later
# d) b and c are both true 
# e) None of the above

# Exercise 5: What will the following Python program print out?
def fred():
    print("Zap")
def jane():
    print("ABC")
jane()
fred()
jane()
# a) Zap ABC jane fred jane
# b) Zap ABC Zap
# c) ABC Zap jane
# d) ABC Zap ABC    this is the answer
# e) Zap Zap Zap

# Exercise 6: Rewrite your pay computation with time-and-a-half for overtime and
# create a function called computepay which takes two parameters (hours and rate).
# Enter Hours: 45
# Enter Rate: 10
# Pay: 475.0

def comutepay():
    try:
        hours = int(input("Enter Hours: "))
        rate  = int(input("Enter Rate: "))
        if hours > 40:
            overtime = (hours - 40)
            overtimerate = rate * 1.5
            print(f"Pay: {40 * rate + (overtime * overtimerate)}" )
        else:
            print(f'Pay: {rate * hours}')
    except:
        print("Enter a number: ")
comutepay()

# Exercise 7: Rewrite the grade program from the previous chapter using a function
# called computegrade that takes a score as its parameter and returns a grade as a
# string.
# Score Grade
# > 0.9 A
# > 0.8 B
# > 0.7 C
# > 0.6 D
# <= 0.6 F
# Program Execution:
# Enter score: 0.95
# A
# Enter score: perfect
# Bad score
# Enter score: 10.0
# Bad score
# Enter score: 0.75
# C
# Enter score: 0.5
# F
def computegrade():
    try:
        score = float(input("Enter score: "))
        if score >=0.9:
            print("A")
        elif 0.90 > score >= 0.8:
            print("B")
        elif 0.9 > score >= 0.8:
            print("B")
        elif 0.8 > score >= 0.7:
            print("C")
        elif 0.7 > score >= 0.6:
            print("D")
        else:
            print("F")
    except:
        print("Bad score")
computegrade()