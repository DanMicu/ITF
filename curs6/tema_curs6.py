# # Exercitiu 1
# class Cerc:
#     def __init__(self,raza,culoare):
#       self.raza = raza
#       self.culoare = culoare
#
#     def descriere_cerc(self):
#         print(f'Cercul este de culoarea {self.culoare} si are raza de {self.raza}')
#
#     def aria(self):
#         return 3.14*(self.raza*self.raza)
#
#     def diametru(self):
#         return self.raza*2
#
#     def circumferinta(self):
#         return 2*3.14*self.raza
#
# cerc = Cerc(4,"roz")
# cerc.descriere_cerc()
# print(cerc.aria())
# print(cerc.diametru())
# print(cerc.circumferinta())
#
# # Exercitiu 2
# class Dreptunghi:
#     def __init__(self,lungime,latime,culoare):
#         self.lungime = lungime
#         self.latime = latime
#         self.culoare = culoare
#
#     def descriere_dreptunghi(self):
#         print(f'Dreptunghiul are o lungime de {self.lungime}, o latime de {self.latime} si este culoarea {self.culoare}')
#
#     def aria(self):
#         return self.lungime*self.latime
#
#     def perimetrul(self):
#         return 2*(self.lungime+self.latime)
#
#     def schimbam_culoarea(self,noua_culoare):
#         self.culoare = noua_culoare
#
#
#
# dreptunghi = Dreptunghi(9,5,"roz")
# dreptunghi.descriere_dreptunghi()
# print(dreptunghi.aria())
# print(dreptunghi.perimetrul())
# dreptunghi.schimbam_culoarea('albastru')
# dreptunghi.descriere_dreptunghi()

# Exercitiu 3
class Angajat:
    def __init__(self,nume,prenume,salariu):
        self.nume = nume
        self.prenume = prenume
        self.salariu = salariu

    def descriere_angajat(self):
        print(f'Buna eu sunt {self.nume} {self.prenume} si am un salariu de {self.salariu}$')

    def nume_cmplet(self):
        return self.nume + " "+ self.prenume

    def salariu_lunar(self):
        return self.salariu

    def salariu_annual(self):
        return self.salariu *12

    def marire_salariu(self,salary_increase): # ASK: this works but i think there might be a better way to do that i cannot figure out.
        return self.salariu + (self.salariu * salary_increase)/100

angajat = Angajat('Dan','Micu',1000)
angajat.descriere_angajat()
print(angajat.nume_cmplet())
print(angajat.salariu_lunar())
print(angajat.salariu_annual())
print(angajat.marire_salariu(10))

# # Exercitiu 4
# class Cont:
#     def __init__(self,iban,titular_cont,sold):
#         self.iban = iban
#         self.titular_cont = titular_cont
#         self.sold = sold
#
#
#     def afisare_sold(self):
#         print(f'Titularul {self.titular_cont} are in contul {self.iban} suma de {self.sold}')
#
#     def debitare_cont(self,bani_scosi):
#         self.sold -= bani_scosi
#         return self.sold
#
#     def creditare_cont(self,bani_added):
#         self.sold += bani_added
#         return self.sold
#
# cont = Cont(21303, "Dan Micu", 10000)
# cont.afisare_sold()
# print(cont.debitare_cont(1000))
# print(cont.creditare_cont(2500))
#
# # Extra cerinta hw
# class Employee:
#     def __init__(self, name,job_title, hourly_wage,age):
#         self.name = name
#         self.job_title = job_title
#         self.hourly_wage = hourly_wage
#         self.age = age
#
#     def displayEmployee(self):
#         print(f"Name: {self.name}, Job Title: {self.job_title}, Wage: {self.hourly_wage}, Age: {self.age}")
#
#     def work_age(self,years_at_company):
#         print(f'{self.name} has been with the company for {years_at_company} years and is {self.age} years old')
#
#     def salary_earned(self,hours_worked):
#         print(f'{self.name} has worked {hours_worked} hours and makes {employee.hourly_wage} per hour')
#         return self.hourly_wage * hours_worked
#
#     def salary_this_month(self,hours_worked):
#         return self.hourly_wage*hours_worked
#
#
# employee = Employee("John Davies","Manager", 22.50, 55)
# employee.displayEmployee()
# employee.work_age(20)
# print(employee.salary_earned(40))
# print(employee.salary_this_month(167))


