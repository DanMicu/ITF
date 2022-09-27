# # Exercitiu 1
# note_muzicale = ['do','re','mi','fa','so','la','si','do']
# print(note_muzicale)
# note_muzicale.reverse()
# print(note_muzicale)
# note_muzicale.reverse()
# print(note_muzicale)
#
# # Exercitiu 2
# note_do = note_muzicale.count('do')
# print(note_do)
#
# # Exercitiu 3
list1 = [3,1,0,2]
list2 = [6,5,4]
list3 = list1 +list2
# print(list3)
# list1.extend(list2)
# print(list1)
list1.append(list2)
print(list1)
# # Exercitiu 4
# list1.sort()
# print(list1)
# list1.remove(0)
# print(list1)
#
# # Exercitiu 5
# if len(list3) == 0:
#     print("list is empty")
# else:
#     print("List isn't empty")
#
# # Exercitiu 6
# list3.clear()
# print(list3)
#
# # Exercitiu 7
# if len(list3) == 0:
#     print("list is empty")
# else:
#     print("List isn't empty")
#
#
#
# # Exercitiu 8
# dict1 = {'Ana': 8, 'Gigel':10, 'Dorel':5}
# print(dict1.keys())
#
# # Exercitiu 9
# print('Ana a luat nota ' + str(dict1['Ana']))
# print('Gigel a luat nota ' + str(dict1['Gigel']))
# print('Dorel a luat nota ' + str(dict1['Dorel']))
#
#
# # Exercitiu 10
# dict1.update({'Dorel':6})
# print(dict1)
#
# # Exercitiu 11
# del dict1['Gigel']
# print(dict1)
# dict1.update({'Ionica': 9})
# print(dict1)
#
# # Exercitiu 12
# zile_sapt = {'luni', 'marți', 'miercuri', 'joi', 'vineri', 'sâmbăta', 'duminică'}
# weekend = {'sâmbăta', 'duminică'}
# zile_sapt.add('luni')
# print(zile_sapt) # nu se adauga din nou luni deoarece este deja in set
#
# # Exercitiu 13 ******* check with teacher if right
# if (set(weekend).issubset(set(zile_sapt))):
#     print("Yes, this list is a subset of the other")
# else:
#     print("No, list is not subset of other." )
#
# # Exercitiu 14
# print(zile_sapt.difference(weekend))
#
# # #Exercitiu 15
# print(zile_sapt.intersection(weekend))