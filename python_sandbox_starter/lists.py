# A List is a collection which is ordered and changeable. Allows duplicate members.
#create list
#numbers = [1.2,3,4,5]
#using a constructor
numbers = list((1,2,3,4,5))
fruits = ['apples', 'oranges', 'Grapes', 'pears', ]

#Get value
print( fruits[1])
#get length
print(len(fruits))
#append to list
fruits.append('mangos')

#remove from list
fruits.remove('Grapes')

#inser into position
fruits.insert(2, 'strwaberries')

#remove from position
fruits.pop(3)

#reverse list
fruits.reverse()
#sort list
fruits.sort()

#reverse sort
fruits.sort(reverse=True)
print(fruits)
