#whether double quote or single quote, it still produces a string
name = 'Patrick'
surname = "Chukwudifu"
age = 29
#print(type(name))

#concatenation is a method that adds new string to an old string and returns overall string
#print('The name of my tutor in Web development calss is' + name + " " + surname)

#string Formatting

#Argument by position
#print('The name of my tutor is {name} {surname} and he is {age} years old'.format(name=name,surname=surname,age=age))

#F-String
print(f'The name of my Facilitator for SID program is Mr {name} {surname} and he is {age} years old')

s = 'Solution is here'

#string method
#print(s.capitalize())

#uppercase
print(s.upper())

#lowercase
print(s.lower())

#Get length
print(len(s))

#Replace
print(s.replace('world', 'everyone'))


#count
sub = 'h'
print(s.count(sub))

#starts with
print(s.startswith('hello'))

#Ends with
print(s.endswith('d'))

#split into a list
print(s.split())

#Find position
print(s.find('r'))

#is all alphabet
print(s.isalpha())

#is all numeric
print(s.isnumeric())
