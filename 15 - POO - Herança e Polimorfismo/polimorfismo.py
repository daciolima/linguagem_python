"""
POO - Polimorfismo

Poli -> Muitas
Morfis -> Formas

Polimorfismo -> Ato de um objeto poder obter muitas formas, ou seja, um método escrito na classe pai, poder
ser reescrito(override) pelas classes filhas assumindo comportamentos(formas) diferentes.

Quando a gente reimplementa um método presente na classe pai em classe filhas
estamos realizando uma sobrescrita de método (Overriding)

O Overriding é a melhor representação do polimorfismo.

"""


class Animal(object):

    def __init__(self, nome):
        self.__nome = nome

    def falar(self):
        raise NotImplementedError('A classe filha precisa implementar este método.')

    def comer(self):
        print(f'{self.__nome} está comendo!')


class Cachorro(Animal):

    def __init__(self, nome):
        super().__init__(nome)

    def falar(self):
        print(f'{self._Animal__nome} fala wau wau!')


class Gato(Animal):

    def __init__(self, nome):
        super().__init__(nome)

    def falar(self):
        print(f'{self._Animal__nome} fala miau miau')


class Rato(Animal):

    def __init__(self, nome):
        super().__init__(nome)

    def falar(self):
        print(f'O {self._Animal__nome} fala algo.')


# Testando
felix = Gato('Felix')
felix.comer()
felix.falar()

pluto = Cachorro('Pluto')
pluto.comer()
pluto.falar()

mickey = Rato('Mickey')
mickey.comer()
mickey.falar()

