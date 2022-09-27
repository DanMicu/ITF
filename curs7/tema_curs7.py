from abc import ABC
class FormaGeometrica(ABC):
    Pi = 3.14
    def aria(self):
        raise NotImplementedError

    def descrie(self):
        print('cel mai probabil am colturi')

class Patrat(FormaGeometrica):
    def __init__(self,latura):
        self.__latura = latura

    def aria(self):
        return self.__latura ** 2

    def descrie(self):
        print('Patrat')

    @property
    def latura(self):
        return self.__latura

    @latura.getter
    def latura(self):
        print('Getting latura...')
        return self.__latura

    @latura.setter
    def latura(self,value):
        self.__latura = value
        print(f'We set the value to {value}')

    @latura.deleter
    def latura(self):
        print('deleting...')

print("-"*100)

class Cerc(FormaGeometrica):
    def __init__(self, raza):
        self.__raza = raza

    @ property
    def raza(self):
        return self.__raza

    @raza.getter
    def raza(self):
        print('Getting raza...')
        return self.__raza

    @raza.setter
    def raza(self, value):
        self.__raza = value
        print(f'We set the value to {value}')

    @raza.deleter
    def raza(self):
        print('deleting...')

    def aria(self): # ASK why i cant put this at the start after __init__
        return FormaGeometrica.Pi * self.__raza**2

    def descrie(self):
        print('Cerc')

patrat = Patrat(6)
print(patrat.aria())
patrat.descrie()
print(f' Latura este {patrat.latura}')
patrat.latura= 3
print(patrat.aria())
del patrat.latura
print('-'*100)
cerc = Cerc(6)
print(cerc.raza)
cerc.descrie()
print(f' raza este {cerc.raza}')
cerc.raza= 3
print(cerc.aria())
del cerc.raza








