# # Exercitiu 1
# '''
# If else este folosit pentru conditii adevarate si false, daca conidia e adevarata partea de "IF" se executa
# si daca conditia e falsa partea de else este executata
# '''
# # Exercitiu 2
# x = int(input("Introdu un numar pentru x"))
# if x > 0:
#     print("numar natural")
# else:
#     print("not numar natural")
#
# # Exercitiu 3
# if x>0:
#     print("numar pozitiv")
# elif x<0:
#     print("numar negativ")
# else:
#     print("neutru")
#
# # Exercitiu 4
# if x>-2 and x<13:
#     print("True")
# else:
#     print("False")
#
# # Exercitiu 5
# y = int(input("introdu inca un numar pentru y"))
# if x-y<5:
#     print(x - y)
#     print("answer is lower than 5")
# elif x-y>5:
#     print(x-y)
#     print('Answer is bigger than 5')
# else:
#     print(x - y)
#     print("Answer is equal to 5")
#
# # Exercitiu 6
# if not(x>5 and x<27):
#     print(x)
#     print("Nr nu este intre 5 si 27")
# else:
#     print(x)
#     print("nr este intre 5 si 27")
#
# # Exercitiu 7
# if x==y:
#     print(f'x={x},y={y}')
#     print("x is equal to y")
# elif x>y:
#     print(f'x={x},y={y}')
#     print("x is bigger than y")
# else:
#     print(f'x={x},y={y}')
#     print("y is bigger than x")
# # Exercitiu 8
# z = int(input("Intro ultimul numar pentru z"))
# if (x==y) and (x!=z):
#     print("isoscel")
# elif (x==z) and (x!=y):
#      print("isoscel")
# elif (y==z) and (x!=z):
#     print("isoscel")
# elif (x==y) and (x==z) and (y==z):
#     print("echilateral")
# else:
#     print("oarecare")
#
# # Exercitiu 9
# litera = input("Introdu o litera")
# if litera == "a" or litera=="e" or litera=="i" or litera=="o" or litera=="u" or litera=="A" or litera=="E" or litera=="I" or litera=="O" or litera=="U":
#     print(" Aceasta litera este o vocala")
# else:
#     print("Aceasta litera nu este o vocala")
#
# # Exercitiu 10
# grade = float(input("Please type your grade below"))
# if grade >= 9 and grade<=10:
#     print(f'Your grade is {grade} You got an A')
# elif grade >= 8 and grade<10:
#     print(f'Your grade is {grade} You got an B')
# elif grade >= 7 and grade<10:
#     print(f'Your grade is {grade} You got an C')
# elif grade >= 6 and grade<10:
#     print(f'Your grade is {grade} You got an D')
# elif grade >4 and grade<10:
#     print(f'Your grade is {grade} You got an E')
# elif grade <=4 and grade>=0:
#     print(f'Your grade is {grade} You got an F')
# else:
#     print("Invalid grade")

# Exercitiu 1
# x = int(input("Please type a number"))
# if x>999:
#     print("minim 4 digit")
# else:
#     print("not 4 digit")

# Exercitiu 2
# if x>99999 and x<1000000:
#     print("6 digit")
# else:
#     print("not 6 digits")

# Exercitiu 3
# if x%2==0:
#     print("even")
# else:
#     print("odd")


# Exercitiu 4
# x = int(input("type a number for x"))
# y = int(input("type 2nd number for y"))
# z = int(input("type third number for z"))
# if x>y and x>z:
#     print("x is the biggest number")
# elif y>x and y>z:
#     print("y is the biggest number")
# elif z>x and z>y:
#     print("z is the biggest")
# else:
#     print("error")

# Exercitiu 5
# if x+y+z == 180:
#     print("valid")
# else:
#     print("invalid")

# Exercitiu 6
coral = 'Coral is either the stupidest animal or the smartest rock'
# x= int(input("type a number for x"))
# size_coral = len(coral)
# cut_string = coral[:size_coral-x]
# print(cut_string)

# Exercitiu 7
# new_string = coral[0:5], coral[-5:]
# print(new_string)

# Exercitiu 8
# new_variable = coral.index("rock")
# output = coral[:new_variable]
# print(output)

# Exercitiu 9
# string_ex9 = input("type something")
# starts_with = string_ex9[0].lower()
# ends_with = string_ex9[-1].lower()
# assert starts_with == ends_with
# print("cool")

# Exercitiu 10
# str_ex10 = '0123456789'
# par = str_ex10[:10:2] # de la 0 la 10 cu pas de 2
# print(par)
# impar = str_ex10[1:10:2]
# print(impar)

