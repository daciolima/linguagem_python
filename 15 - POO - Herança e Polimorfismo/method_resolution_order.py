"""
POO - MRO - Method Resolution Order

Method Resolution Order (Resolução de Ordem de Método), é a ordem
de execução dos métodos (quem será executado primeiro).

# No MRO a ordem das Heranças Multiplas é da Direita pra esquerda, sendo a prioridade dada a classe Filha e em seguida
a última da esquerda.

Ex:
class Piguim(Terrestre, Aquatico, Animal):
    pass

Ordem: Piguim, Terrestre, Aquatico, Animal, object

Em Python podemos conferir a ordem de execução dos métodos (MRO) de 3 formas:
    - Via propriedade da classe __mro__
    - Via método mro()
    - Via help

Ex no console:
> Piguim.__mro__
> Piguim.mro()
> help(Piguim)

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


# Ordem de Herança é da direita pra esquerda considerando a ultima da esquerda
class Piguim(Terrestre, Aquatico):

    def __init__(self, nome):
        super().__init__(nome)


# Testando
tux = Piguim('Tux')
print(tux.andar())
print(tux.nadar())
print(tux.cumprimentar())  # O overide do método cumprimentar está obedecendo o Method Resolution Order - MRO

