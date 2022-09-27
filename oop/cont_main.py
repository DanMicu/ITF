from oop.cont_bancar import ContBancar

cont1 = ContBancar('Andy S', 'RO001')
cont2 = ContBancar('Crina s','RO002')

cont1.activareCont(7777)
cont2.activareCont(3333)
cont2.activareCont(7777)

cont1.alimentareCont(300)
cont2.alimentareCont(700)
cont2.alimentareCont(300)

cont1.plataCard(500)
cont1.plataCard(300) #0
cont2.plataCard(100)
cont2.plataCard(200) #700

cont2.interogareSold()
cont2.interogareSold()

#tema
#clasa angajat
#nume, prenume, salariu, vechime
#constructor : nume prenume salariua functie vechime
#metode
#descriere
#marire salariu in f de vechime
#actualizare vechime (param noua vechime)
# self.vechime=noua_vechime
# daca are vechime sub 5 ani marim cu 300 peste 5 ani 500
