# A variable is a container for a value, which can be of various types

'''
This is a 
multiline comment
or docstring (used to define a functions purpose)
can be single or double quotes
'''

"""
VARIABLE RULES:
  - Variable names are case sensitive (name and NAME are different variables)
  - Must start with a letter or an underscore
  - Can have numbers but can not start with one
"""

#x=1                   #int
#y=2.5                 #float
#name= 'Chernet'       #string
#is_cool = true        #boolean

#Multiple assignment
x, y, name, is_cool = (1, 2.5, 'brad', True)
print(x)

#basic math
a = x+y

#casting
x = str(x)
y = int(y)
z = float(y)
#Check type
print(type(x))
print(type(z))
print(z)






