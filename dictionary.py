# A dictionary is a collection which is unordered, changable and indexed. no duplicate members.

person = {
    'first_name':'ojo',
    'last_name' : 'Nnamdi',
    'age' :20
}
#print(type(person))

#use constructor
#person2 = dict(first_name='sara', last_name='Jean')

#get value
print(person['first_name'])
print(person.get('last_name'))

#add key/value
#person['phone' = '555-555-5555']

#get dict keys
print(person.keys())

#get dict items
print(person.items())

#copy dict
person2 = person.copy()
person2['city'] = 'Boston'

#Remove item
del(person['age'])
person.pop('phone')

#clear
person.clear()

#get length
print(len(person2))

#list of dict
people = [
    {'name': 'Martha', 'age': 30},
    {'name': 'Kelvin', 'age': 25}
]
print(people[1]['name'])


