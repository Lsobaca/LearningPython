# Exercise 1: Write a program which repeatedly reads numbers until the user enters
# “done”. Once “done” is entered, print out the total, count, and average of the
# numbers. If the user enters anything other than a number, detect their mistake
# using try and except and print an error message and skip to the next number.
# Enter a number: 4
# Enter a number: 5
# Enter a number: bad data
# Invalid input
# Enter a number: 7
# Enter a number: done
# 16 3 5.333333333333333

def ex1():
    numbers = []
    count = 0
    while True:
        try:
            adding_number = input("Enter a number: ")
            if adding_number == "done":
                break
            numbers.append(int(adding_number))
        except ValueError:
            print("Invalid input")
    total = 0
    for number in numbers:
        total = total + number
        count += 1
    print(f'{total} {count} {total/count}')

ex1()


# Exercise 2: Write another program that prompts for a list of numbers as above
# and at the end prints out both the maximum and minimum of the numbers instead
# of the average
import math
def ex2():
    numbers = []
    print("Enter a list: ")
    while True:
        take_number = input()
        if take_number == "done":
            break
        
        numbers.append(int(take_number))

    minn, maxx = 0,0
    for number in numbers:
        if number>maxx:
            maxx = number
        if minn == 0 or minn > number:
            minn = number

    print(maxx)
    print(minn)
    print(max(numbers))
    print(min(numbers))

ex2()