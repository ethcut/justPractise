# A Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
 

#sample tuple
#fruit_tuple = ('Apple', 'Orange', 'Mango')
#constructor
#fruit_tuple = tuple(('Apple', 'Orange',  'Mango'))

#single value
#print(fruit_tuple[1])
# can not change value
#fruit_tuple[1] = 'Grape'

#tuples with one value should have trailing comma
#fruit_tuple_2 = ('Apple',)
#del fruit_tuple_2

#get length of tuple
#print(len(fruit_tuple_2))


# A Set is a collection which is unordered and unindexed. No duplicate members.
#create set
fruit_set = {'Apple', 'Orange', 'Mango', 'Apple'}
#check if in set
#print('Apples' in fruit_set)

#add to set
fruit_set.add('Grape')
#remove from set
fruit_set.remove('Grape')
#clear set
fruit_set.clear()
#delete set
del fruit_set

print(fruit_set)