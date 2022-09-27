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
# else:
#     print("z is the biggest")


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
# new_string = coral[0:5] + coral[-5:]
# print(new_string)

# Exercitiu 8
new_variable = coral.index("rock")
output = coral[:new_variable]
print(output)

# Exercitiu 9
# string_ex9 = input("type something")
# starts_with = string_ex9[0].lower()
# ends_with = string_ex9[-1].lower()
# assert starts_with == ends_with
# print("starts and ends with same letter") # if it doesnt we get assertionerror

# Exercitiu 10
# str_ex10 = '0123456789'
# par = str_ex10[0:10:2] # de la 0 la 10 cu pas de 2
# print(par)
# impar = str_ex10[1:10:2]
# print(impar)

# str_ex10 = '23456789'
# par = str_ex10[0:10:2] # from index 0 to index 10 with 2 step
# print(par)
# impar = str_ex10[1:10:2]
# print(impar)