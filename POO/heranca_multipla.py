"""
POO - Herança Multipla (Multiderivação)

Herança multipla nada mais é do que a possibilidade de uma classe herdar de multiplas classes,
fazendo com que a classe filha herde todos os atributos e métodos de todas as classes herdadas.

OBS: A herança multipla pode ser feita de duas maneiras:
    - Por Multiderivação Direta;
    - Por Multiderivação Indireta.

OBS: Não importa se a devivação é direta ou indireta, a classe que realizar a herança herdará todos
os atributos e métodos das super classes.

"""


class Animal:

    def __init__(self, nome):
        self.__nome = nome

    def cumprimentar(self):
        return f'Eu sou {self.__nome}'


class Aquatico(Animal):

    def __init__(self, nome):
        super().__init__(nome)

    def nadar(self):
        return f'{self._Animal__nome} está nadando!'

    def cumprimentar(self):
        return f'Eu sou {self._Animal__nome} do mar!'


class Terrestre(Animal):

    def __init__(self, nome):
        super().__init__(nome)

    def andar(self):
        return f'O {self._Animal__nome} está andando.'

    def cumprimentar(self):
        return f'Eu sou {self._Animal__nome} da terra!'


class Piguim(Terrestre, Aquatico):

    def __init__(self, nome):
        super().__init__(nome)


# Testando
baleia = Aquatico('Wally')
print(baleia.nadar())
print(baleia.cumprimentar())

tatu = Terrestre('Xim')
print(tatu.andar())
print(tatu.cumprimentar())

tux = Piguim('Tux')
print(tux.andar())
print(tux.nadar())
print(tux.cumprimentar())  # O overide do método cumprimentar está obedecendo o Method Resolution Order - MRO


# Verificando instância do objeto
print(f'Tux é instância de Piguim? {isinstance(tux, Piguim)}')  # True
print(f'Tux é instância de Aquatico? {isinstance(tux, Aquatico)}')  # True
print(f'Wally é instância de object? {isinstance(baleia, object)}')  # True
print(f'Tux é instância de Terrestre? {isinstance(tux, Terrestre)}')  # True
print(f'Tux é instância de Animal? {isinstance(tux, Animal)}')  # True
print(f'Tux é instância de object? {isinstance(tux, object)}')  # True
