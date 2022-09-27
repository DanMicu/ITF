#list review
courses = ['history', 'math', 'physics', 'compsci']
# courses.append('art') #APPEND ADDS ITEM TO LIST
# courses.insert(0, 'art') # WE USE INSERT TO ADD VALUE TO WHATEVER INDEX WE WANT AND SHIFTS ALL
# courses_2 = ['art', 'education']
# courses.insert(0,courses_2) # added the new courses_2 list within the first list as a separate list
# courses.extend(courses_2) # added the new courses_2 list to the original list without it being separate
# courses.remove('math') # removes math - obvious
# popped = courses.pop() # .pop() removes the last item on the list which was compsci
# print(courses)
# print(popped) # prints just what we removed with .pop()
#courses.reverse() # prints values in reverse order
#courses.sort() #prints courses in alphabetical order
#print(courses)

nums = [1,5,2,4,3]
# nums.sort() # sorts 1,2,3,4,5
# nums.reverse()
# print(min(nums)) #prints smallest number
# print(max(nums)) #prints highest number
# print(sum(nums)) #adds the numbers
# print(nums)
# print(courses.index("compsci")) #prints the index of the value you write in brackets
# for course in courses: # prints all the values in the list one under the other
#     print(course) # you can use any word not just "course"
#
# print("math" in courses) # asks python if the value in between brackets is in the list => true or false
# print('art' in courses) # prints false since art isnt in the list
#
# for index, course in enumerate(courses): #prints values in the list with their index nr before them
#     print(index, course)
#
# for index, course in enumerate(courses, start=1): # same as above but starts count at 1
#     print(index,course)
#
# course_str =' | '.join(courses)
# print(course_str)
# print(type(course_str))

# course_str = ' - '.join(courses) # this is how you turn a list into a string with separator of your choosing
# print(course_str)
# print(type(course_str))  # class str
# new_list = course_str.split((' || ')) # turns a str into a list
# print(new_list)
# print(type(new_list)) # class list
#
#
# prop = 'ana are mere'
# print(prop[4:9])
from abc import ABC, abstractmethod

class FormaGeometrica(ABC):
    PI = 3.14

    @abstractmethod
    def aria(self):
        raise NotImplementedError

    @staticmethod
    def descrie():
        print('Cel mai probabil am colturi.')


class Patrat(FormaGeometrica):
    def __init__(self, latura):
        self.__latura = latura

    def aria(self):
        return self.__latura**2

    @property
    def latura(self):
        print("Getter for latura called.")
        return self.__latura

    @latura.setter
    def latura(self, value):
        self.__latura = value
        print("Setter for latura called.")

    @latura.deleter
    def latura(self):
        print("Deleter for latura called.")
        del self.__latura


class Cerc(FormaGeometrica):
    def __init__(self, raza):
        self.__raza = raza

    @property
    def raza(self):
        print("Getter for latura called.")
        return self.__raza

    @raza.setter
    def raza(self, value):
        self.__raza = value
        print("Setter for latura called.")

    @raza.deleter
    def raza(self):
        print("Deleter for latura called.")
        del self.__raza

    def aria(self):
        return FormaGeometrica.PI * self.__raza ** 2

    @staticmethod
    def descrie():
        print("Eu nu am colturi.")
p = Patrat(3)
p.descrie()

print(p.aria())
p.latura = 6
print(p.latura)
del p.latura
c = Cerc(3)
print(c.aria())
print(c.raza)
print(c.aria())
c.raza = 6
print(c.raza)
del c.raza

