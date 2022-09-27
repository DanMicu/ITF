#concatenare de stringuri
str1 = 'mere'
str2 = 'pere'
print('Mie imi place sa mananc ' + str1+ ' si ' + str2)

# NU putem concatena int/float/bool si string
var_int =10
# print(str1 + var_int) # o sa dea eroare, nu putem concatena str si int
print(str1 +str(var_int))
print(f"{str1}{var_int}")
# formatare de stringuri
n1 = 10
n2 = 5
print(f"Mie imi place sa mananc  {n1} {str2} si {n2} {str1}")
# intre acolade se pot pune instruction python nu doar variabile, ca si {n1 + 5}
print(f"imi place sa mananc {n1+5} si {n2+10}")

# se pot printa mai multe variabile, cu virgula intre ele( separatorul va fi spatiu
print(str1, str2,n1, n2)
print(str1, str2,n1, n2, end=' +++ ')
print(str1, str2,n1, n2, sep= '||')

