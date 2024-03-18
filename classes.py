# A class is like a blueprint for creating Objects in python. An Object has properties and methods(functions) associated with it. Almost everything in Python is an object.

# Create class

def __init__(self, name, email, age):
        self.name = name
        self.email = email
        self.age = age

    def greetings(self):
        return f'My name is {self.name} and I am {self.age} year old'

    def has_birthday(self):
        self.age +=1

#  Init user object
soph = User('Sophia Adimalo', 'agunyenwakosisosophia@gmail.com', 35)
# print(pato.name)

soph.has_birthday()
num=soph.greetings()
print(num)