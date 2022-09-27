# input_simplu = input()
# print(input_simplu)
# print(type(input_simplu))
#
# # Valoarea obtinuta prin input este mereu str, trebuie sa facem noi type casting
# varsta = input("ce varsta ai?\n")
# print(type(varsta))
#
# varsta= int(varsta)
# print(type(varsta))

# # Putem face totul intro sungura linie
# anul_nasterii = int(input("In ce an teai nascut"))
# print(type(anul_nasterii))


 # cum sa luam mai multe valori din input
data_nasterii = input("data nasterii (zz ll aaaa):")
print(data_nasterii)

# split inparte stringul in mai multe stringuri mici dupa spatii
ziua, luna, anul = data_nasterii.split()
ziua, luna, anul = int(ziua), int(luna), int(anul)
print(type(ziua), ziua)
print(type(luna), luna)
print(type(anul), anul)
