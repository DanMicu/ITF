# Exercitiu 1
# def doua_numere(a,b):
#     return a + b
# print(doua_numere(5,6))

# # Exercitiu 2
# def numar(a):
#     if a%2 == 0:
#         return True
#     else:
#         return False
# print(numar(6))

# Exercitiu 3 # ASK ASK why can't I write nume = len(nume)/ prenume = len(prenume) / nume_mijlociu = len(nume_mijlociu)?
# def nume_complet():
#     nume = len(Nume)
#     prenume = len(Prenume)
#     nume_mijlociu = len(Nume_mijlociu)
#     return nume + prenume + nume_mijlociu
# Nume = input('write your family name')
# Prenume = input('write your given name')
# Nume_mijlociu = input('write your middle name')
# print(nume_complet())

# Exercitiu 4
# def aria_drep(a,b):
#     return a*b
#
# print(aria_drep(5,5))

# Exercitiu 5
# def aria_cerc(r):
#     return 3.14*r**2
# print(aria_cerc(10))

# Exercitiu 6 # Ask if both are okay
# First try
# string_dat = input("Write something")
# def str_1(x):
#     if x in string_dat:
#         return True
#     else:
#         return False
# print(str_1("C"))

# Second try
# def str_1(x,y):
#     if x in y:
#         return True
#     else:
#         return False
# print(str_1("C","Continue"))

# Exercitiu 7
# def number_of_chars(the_string):
#     the_string = the_string.replace(",","")
#     char_lowercase = 0
#     char_uppercase = 0
#     for char in the_string:
#         if char == char.lower():
#             char_lowercase += 1
#         elif char == char.upper():
#             char_uppercase += 1
#     print(f'number of lower case characters is {char_lowercase}')
#     print(f'number of upper case characters is {char_uppercase}')
# number_of_chars('Micu,Dan,Michael')

# Exericitiu 8 # Ask during class to re explain
# def nums_list(list):
#     for nums in range(len(list)):
#         if list[nums] < 0:
#             list[nums] = -list[nums]
#     return list
# print(nums_list([1,3,-4,-5,5]))

# Exercitiu 9
# def two_nums(x,y):
#     if x > y:
#         print(f' Primul număr {x} este mai mare decat al doilea nr {y}')
#     elif x <y:
#         print(f' Al doilea nr {y} este mai mare decat primul nr')
#     else:
#         print('Numerele sunt egale')
# two_nums(6,6) # ask if i need to write print(two_nums(6,6) but then when i press run it says "none"

# Exercitiu 10

def numar_setnumere(num, set10):
    if num in set10:
        print(f'nu am adaugat numărul în set. Acesta există deja')
        return False
    else:
        set10.add(num)
        print(f'am adaugat numărul {num} nou în set')
        return True

set10 = {2,3,4}
print(numar_setnumere(2,set10))
print(set10)
print(numar_setnumere(1,set10))
print(set10)








