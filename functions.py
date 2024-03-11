#A function is a block of code which only runs when it is called. In python, we do not use curly brackets. we use indentation with tabs or spaces

#create a function

def sayHello(greeting):
    print(f'Hello my name is {greeting}')

sayHello('Sophia')

#def Multiply(a,b):
 #   total = a+b
  #  print(total)
#Multiply(6,5)

#return statement with functions

#def Addition(num1, num2):
#        total = num1 + num2
 #       return total
#print(Addition(4,10))

#A lambda function is a small anonymous function.
#A lammbda function can take any number of argument, but can only have one expression.Very similar to JS arrow function

Addition = lambda num1,num2: num1 + num2

print(Addition(3,9))