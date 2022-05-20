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
# constructs an instance or object called PartyAnimal   
an = PartyAnimal()
# the varable is able to use the method in the class
an.party()
an.party()
an.party()
an.party()
# are able to call the party() when we use the class name
# '.' method name with the parameter of the object that was
# constructed. Each Partyanimal object/instance contains within 
# it a variable x and a method/function named party.
PartyAnimal.party(an)



# classes as types

print('Type',type(an))
print('dir',dir(an))
print('Type x',type(an.x))
print("Type",type(an.party))


# objects have a lifecycle. they are discarded when the program finishes.
# if we want to know when an object is created or discarded. we have to
# set up some specially named methods to the  object
# example


class PartyAnimal:
    x = 0
    #
    def __init__(self) -> None:
        print('I am constructed')
    
    def party(self):
        self.x += 1
        print('So far',self.x)
        
    def __del__(self):
        print('I am destructed', self.x)

an = PartyAnimal()
an.party()
an.party()
#
an = 42
print('an contains',an) 
       
# print(342/891)


# the real power with objects is that we are able to 
# create more of them with differnet starting values.
# example
class Animal:
    x = 0
    name = ''
    def __init__(self,nam) -> None:
        self.name = nam
        print(f'{self.name} is born')
        
    def party(self):
        self.x += 1
        print(f'{self.x} are born')
        
a = Animal('Lion')
a.party()
j = Animal('Jackel')
j.party()
a.party()
        

# inheritance
# a powerful feature of OOP is the ability to create
# a new class by extending an existing class. we use 
# the key words 'from' and 'import'.

# example how to call a class from another file
from party import PartyAnimal
# when defining the class CricketFan we show that we are 
# extending the PartyAnimal class. how to do it, we would 
# to put the class that we want as a permater for the class.
# when we inherit a class we would be able to use all the 
# methods and the variables of the class. 
class CricketFan(PartyAnimal):
    points = 0
    def six(self):
        self.points += 6
        self.party()
        print(f'{self.name} points {self.points}')
        
s = PartyAnimal('Sally')
s.party()
j = CricketFan('Jim')
j.party()
j.six()
print(dir(j))

# a child class is when a class inherits all the attributes
# and methods of the parent class. example above.



