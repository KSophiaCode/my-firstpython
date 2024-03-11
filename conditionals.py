# If/Else conditions are used to decide to do something based on something being True or False

x=21
y=20

#comparison operators "(==, !=, >, <, >=, <=)" - used to compare values

#if statement works if the statement is true

#if x>y:
 #   print(f'yes {x} is greater than {y}')

#if/ else statement
#if x<y:
 #   print(f'yes {x} is less than {y}')
#else:
 #   print(f'No {x} is not less than {y}')

#elseif statement

#if y>x:
 #   print(f'yes {y} is greater than {x}')
#elif y==x:
 #   print(f'yes {y} is equal to ')
#else:
   # print(f'Happy Womens Day')

    #Nested if

#if x > 2:
 #   if x<50:
  #      print(f'{x} is greater than 2 and less than 50')

#logical operators (and, or, not) - used to combine conditional statement
#logical and

#if x > 20 and x < 50:
 #   print(f'{x} is greater than 2 and lessthan 50')

#logical or

#if x > 200 or x < 50:
 #   print(f'{x} is greater than 2 and lessthan 50')

#logical not
if not(x==y):
    print(f'{x} is not equal to {y}')

#membership operators (not, not in) - Membership operators are used to test if a sequence is presented in an object

numbers = [1,2,3,4,5]

    #in 
if x in numbers:
    print(x in numbers)

# not in
if x not in numbers:
    print(x not in numbers)

#Identity operators (is. is not) - compare the objects,not if they are equal, but if they are actually same object, with the same memory location:

#is
if x is y:
    print(x is y)

#is not
if x is not y:
    print(x is not y)