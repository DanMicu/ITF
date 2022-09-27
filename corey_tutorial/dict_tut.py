student = {'name': 'John', 'age': 25, 'courses': ['Math', 'CompSci']}

student['phone'] = '555-5555' # adds this value to the dict since it didn't exist before
student['name'] = 'Jane' # since 'name' already exists in our cont it will replace it

student.update({'name': 'Jane', 'age': 26, 'phone': '555-5555'}) # does what we did above but in one
print(student)
#del student['age'] # deletes age from the cont
#age = student.pop('age')
#age = student.pop('age')
#print(student['name']) # prints the value youre asking for from the cont
#print(student.get('name', 'Not Found'))  #.get finds the value you're looking for and 'not found' is default phrase typed by us incase the value doesnt exist
#print(student)
# print(age)

# print(len(student))
# print(student.keys()) # .keys() prints all the keys in the cont
# print(student.values()) # .values prints all the values in the cont
# print(student.items()) # .items() prints keys and values
# for key, value in student.items(): # prints each key and value on separate rows
#     print(key, value)

