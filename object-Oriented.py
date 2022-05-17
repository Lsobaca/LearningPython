# object oriented programming is a way to arrange your code so that you
# can zoom into 500 lines of the code, and understand it while ignoring the other
# 999,500 lines of code for the moment.


# python provides many built-in objects. 
# example
stuff = list()
stuff.append('python')
stuff.append('chuck')
stuff.sort()
print (stuff[0])
# stuff is calling the __getitem__() method with the parameter of zero
print (stuff.__getitem__(0))
# a verbose way to call the 0th element in the list
print (list.__getitem__(stuff,0))

print(10**.5)

# lists the methods and attributes of a object
print(dir(stuff))

# a program in the most basic form is when it takes some input
# does some process, and produces some output

# example
usf = input('Enter the US Floor Number: ')
wf = int(usf) - 1
print(f'Non - US Floor Number is {wf}')




# Encapsulation is a way to keep the program cleaner


# creating an python object. we would need to define a function
# that allows us to store a bit of code and give it a name and then
# later invoke that code using the name of the function
# example
class PartyAnimal:
    x=0
    def party(self):
        self.x = self.x + 1
        print(f'So far {self.x}')
        
an = PartyAnimal()
an.party()
an.party()
an.party()
an.party()
PartyAnimal.party(an)

