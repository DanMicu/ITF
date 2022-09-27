# Exercitiu 1
masini = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lăstun','Fiat', 'Trabant', 'Opel']
# for index in range(len(mașini)):
#     print(f'Mașina mea preferată este {mașini[index]}')


# for masina in masini:
#     print(f'Mașina mea preferată este {masina}')

# i = 0
# while i < len(mașini):
#     print(f'Mașina mea preferată este {masini[i]}')
#     i += 1

# Exercitiu 2
# for index in range(1,len(masini)-1):
#     print(masini[index].upper())
# else:
#     print(masini)

# Exercitiu 3
# masina_dorita = input("As dori sa cumpar un:")
# for masina in masini:
#     if masina == masina_dorita:
#         print("am gasit masina dorita de dvs")
#         break
#     else:
#         print(f'am gasit masina {masina} mai cautam')

# Exercitiu 4

# for masina in masini:
#     if masina == "Lăstun" or masina == "Trabant":
#         continue
#     else:
#         print(f'Sar putea sa va placa masina {masina}')

# Exercitiu 5
# masini_vechi = []
# for masina in masini:
#     if masina == "Lăstun":
#         masini_vechi.append(masina)
#         masini.remove("Lăstun")
#         masini.append("Tesla")
#     if masina == "Trabant":
#         masini_vechi.append(masina)
#         masini.remove("Trabant")    # nu am scris masini.append(tesla) iar pentru ca apoi apare de 2 ori tesla
#         print(f'Modelele vechi sunt{masini_vechi}')
#         print(f'Modelele noi sunt{masini}')

# Exercitiu 6 # nu am reusit sa figure out cum sa fac acest exercitiu
pret_masini = {
'Dacia': 6800,
'Lăstun': 500,
'Opel': 1100,
'Audi': 19000,
'BMW': 23000
}
buget = 15000


# Exercitiu 7
numere = [5, 7, 3, 9, 3, 3, 1, 0, -4, 3]
# numar_three = 0
# for num in numere:
#     if num == 3:
#         numar_three += 1
#         print(f' numarul 3 apare de {numar_three} ori')

# Exercitiu 8
# suma_numere= 0
# for num in numere:
#     suma_numere += num
#     print(f' suma este {suma_numere}')

# Exercitiu 9 ### ask
# nr_max = numere[0]
# for num in numere:
#     if num > nr_max:
#         nr_max = num
# print(nr_max)

# Exercitiu 10
# new_list = []
# for num in numere:
#     if num > 0:
#         new_list.append(-num)
#         print(-num)
#     else:
#         new_list.append(num)
# print(f'noua lista este {new_list}')








