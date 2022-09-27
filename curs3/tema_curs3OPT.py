# jucatori = ["one", "two", "three","four","five"]
# print(jucatori)
# schimbari_max = 2
#
# while schimbari_max <3:
#     i = input("introdu numele jucatorului pe care doresti sa il schimbi")
#     if i not in jucatori:
#         print("nu se poare efectua schimbarea deoarece jucatorul nu este in teren")
#     else:
#         x = input("Introdu numele jucatorului pe care doresti sa il adaugi: ")
#         jucatori.pop(jucatori.index(i))
#         jucatori.append(x)
#         print('Noua lista cu jucatori este: ', jucatori)
#         print(f'A intrat {x} si a iesit {i}')
#         schimbari_max = schimbari_max + 1
#         print('Mai ai schimbari de efectuat maxim: ', 3 - schimbari_max)

# meciul
jucatori = ['Madalina', 'Arthur', 'Meli', 'Nandi', 'Gimi']
print(jucatori)
schimbari_max = 0

while schimbari_max < 3:
    i = input("Introdu numele jucatorului pe care doresti sa il schimbi: ")
    if i not in jucatori:
        print(f'nu se poate efectua schimbarea deoarece jucătorul cu  nu e înteren')
    else:
        x = input("Introdu numele jucatorului pe care doresti sa il adaugi: ")
        jucatori.pop(jucatori.index(i))
        jucatori.append(x)
        print('Noua lista cu jucatori este: ', jucatori)
        print(f'A intrat {x} si a iesit {i}')
        schimbari_max = schimbari_max + 1
        print('Mai ai schimbari de efectuat maxim: ', 3-schimbari_max)

