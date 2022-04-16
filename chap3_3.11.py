# Exercise 1: Rewrite your pay computation to give the employee 1.5 times the
# hourly rate for hours worked above 40 hours.
# Enter Hours: 45
# Enter Rate: 10
# Pay: 475.0
hours = int(input("Enter Hours: "))
rate  = int(input("Enter Rate: "))
if hours > 40:
    overtime = (hours - 40)
    overtimerate = rate * 1.5
    print(f"Pay: {40 * rate + (overtime * overtimerate)}" )
else:
    print(f'Pay: {rate * hours}')

# Exercise 2: Rewrite your pay program using try and except so that your program handles non-numeric input gracefully by printing a message and exiting the
# program. The following shows two executions of the program:
# Enter Hours: 20
# Enter Rate: nine
# Error, please enter numeric input
# Enter Hours: forty
# Error, please enter numeric input
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


# Exercise 3: Write a program to prompt for a score between 0.0 and 1.0. If the
# score is out of range, print an error message. If the score is between 0.0 and 1.0,
# print a grade using the following table:
# Score Grade
# >= 0.9 A
# >= 0.8 B
# >= 0.7 C
# >= 0.6 D
# < 0.6 F
# ~~~
# Enter score: 0.95 A ~~
# Enter score: perfect
# Bad score
# Enter score: 10.0
# Bad score
# Enter score: 0.75
# C
# Enter score: 0.5
# F
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