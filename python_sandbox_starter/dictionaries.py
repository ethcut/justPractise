# A Dictionary is a collection which is unordered, changeable and indexed. No duplicate members.
#simple dictionary
person = {
  'first_name': 'John',
  'last_name': 'Doe',
  'age': 30}
#using a constructor
#person = dict(frist_name= 'John',last_name='Doe'age= 30)

#access value
print(person['first_name'])
print(person.get('last_name'))
#add key/value
person['phone']= "555-555-5555"
#get keys
print(person.keys())

#get items
print(person.items())
#make copy
person2 = person.copy()
person2['city']= 'Boston'
print(person2)

#remove
del(person['age'])
person.pop('phone')
#clear dict
person.clear()

#length
print(len(person2))
print(person)

#list of dict
people = [
  {'name': 'Martha', 'age': 40},
  {'name': 'Bob', 'age': 20}
]
print(people [1]['name'])