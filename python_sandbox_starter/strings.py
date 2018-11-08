# Strings in python are surrounded by either single or double quotation marks. Let's look at string formatting and some string methods

name ='Cheru'
age = 37

#concateneate
#print('Hello I am '  + name + ' and I am '+ str(age) )
# String Formatting

#Arguments by position
#print('{}, {}, {}' .format('a', 'b', 'c'))
#print('{1}, {2}, {0}' .format('a', 'b', 'c'))
#arguments by name
#print('My name is {name} and I am {age}' .format(name=name, age=age))

#F-strings
#print(f'My name is {name} and I am {age}')
# String Methods
s= 'hello there world'
#capitalize first letter
print(s.capitalize())
#all upper
print(s.upper())
#all lower
print(s.lower())
#swap case
print(s.swapcase())

#get length 
print(len(s))
#replace
print(s.replace('world', 'everyone'))
#count
sub = "h"
print(s.count(sub))

#start with
print(s.startswith('hello'))
#ends with
print(s.endswith('d'))
#split into a list
print(s.split())
#find position
print(s.find('r'))
#Is all alphanumeric
print(s.isalnum())
#is all alphabetic
print(s.isalpha())

#is all numeric
print(s.isnumeric())

