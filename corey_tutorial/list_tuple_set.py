# LIST ############
courses = ['history', 'math', 'physics', 'compsci'] # LISTS USE SQUARE BRACKET[]
# courses.append('art') # We use .append to add art to the list
# courses.insert(0,'art') # this put art at index 0 where history was and shifted history to index 1
#courses_2=['art', 'education']
#courses.insert(0,courses_2) # this added the courses_2 list inside the courses list as a seperate list
#courses.extend(courses_2) # this added art and eduction to the first list (at the end of it)
#courses.remove('Math') # removed math from list
# popped= courses.pop() # .POP() removes the last item in the list
# print(popped) # prints just the item on the list we removed
#courses.reverse() # prints the list in reverse
#courses.sort() # prints in alphabetical order the list
#print(courses)

# nums = [1,5,2,4,3]
# nums.sort() # sorts them lowest to highest
# print(nums)
# nums.reverse() # backwards
# print(min(nums)) # smallest number
# print(max(nums)) # biggest number
# print(sum(nums)) # sum of the numbers in the list

# print(courses.index("compsci")) # finds index of compsci on the list which is 3
# for course in courses: # prints the items in our list one under the other
    #print(course)
#print('math' in courses) # it asks Hey is "THIS" in the courses list? and gives true or false responses
#for index, course in enumerate(courses): # prints all the items in the list with their index number before them
    #print(index,course)

#for index, course in enumerate(courses, start=1): #same as above but starts at 1 instead of 0
    #print(index,course)

# course_str = '|| '.join(courses) # this is how you turn a list into a string with separator of your choosing
# print(course_str)
# new_list = course_str.split((' || ')) # turns the str into a list
# print(new_list)


#Mutable regular list with big square brackets where we can add items to the list
# list_1 = ['history', 'math', 'physics', 'compsci']
# list_2 = list_1
# print(list_1)
# print(list_2)
#
# list_1[0] = 'art' # adds art to both lists since list1 = list2
# print(list_1)
# print(list_2)

#Immutable list # tuples are lists with small circle brackets that cannot be changed
tuple_1 = ('history', 'math', 'physics', 'compsci') # list with circle brackets is immutable
tuple_2 = tuple_1

print(tuple_1)
print(tuple_2)

tuple_1[0] = 'art' # gives error because this list is immutable which means it cant be changed
print(tuple_1)
print(tuple_2)

# Sets # dont care about order , throw away duplicates # only used to check if has no duplicates
cs_courses = {'History', 'Math', 'Physics', 'CompSci', 'Math'}
art_courses = {'History', 'Math', 'Art', 'Design'}
# print('Math' in cs_courses) # asks python if math is in the set
# print(cs_courses.intersection(art_courses)) # prints the courses that are on both sets
# print(cs_courses.difference(art_courses)) # prints the courses that arent in both
#print(cs_courses.union(art_courses)) # combines the two sets and prints all the values
# print(cs_courses)
# print(art_courses)

# /////////////////////////////

# Empty Lists
empty_list = []
empty_list = list()

# Empty Tuples
empty_tuple = ()
empty_tuple = tuple()

# Empty Sets
empty_set = {} # This isn't right! It's a dict
empty_set = set() # this is how you do an empty set

print(type(empty_set))