#A list is a collection which is ordered and organized. Allows duplicate members.

#Create List
#numbers= [1,2,3,4]
#print(numbers)
#arrays count numbers from 0 till infinity
#print(numbers[1])

fruits = ['apple','orange','banana', 'mango']
#print(fruits [0])

#Get length (helps calculate total)
#print(len(fruits))

#Append to list (it means to add to the existing list)
#fruits.append('water melon')

#Remove from list
fruits.remove('mango')

#insert into position
fruits.insert(2, 'strawberries')

#change value
fruits[0] = 'Blueberries'

#remove with pop
fruits.pop(2)

#reverse list
fruits.reverse()

#sort list alphabetically
fruits.sort()

#reverse sort
fruits.sort(reverse=True)
print(fruits)