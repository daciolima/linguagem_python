"""
POO - POO

POO -> Sâo instâncias da Classe, ou seja, após o mapeamneto do objeto do mundo real para sua
representação computacional, devemos poder criar quantos objetos forem necessários.
Podemos pensar nos objetos/Instâncias de uma classe como variáveis do tipo definido na classe
"""



class Lampada:

    def __init__(self, cor, voltagem, luminosidade):
        self.__cor = cor
        self.__voltagem = voltagem
        self.__ligada = False

    def checa_lampada(self):
        return self.__ligada

    def liga_desliga(self):
        if self.__ligada:
            self.__ligada = False
        else:
            self.__ligada = True


class Cliente:

    def __init__(self, nome, cpf):
        self.__nome = nome
        self.__cpf = cpf

    def diz(self):
        print(f'O cliente {self.__nome} diz oi!')


class ContaCorrente:

    contador = 49999

    def __init__(self, limite, saldo, cliente):
        self.__id = ContaCorrente.contador + 1
        self.__limite = limite
        self.__saldo = saldo
        self.__cliente = cliente
        ContaCorrente.contador = self.__id

    def mostra_cliente(self):
        print(f'O cliente dessa conta é {self.__cliente._Cliente__nome}')


class Usuario:

    def __init__(self, nome, email, senha):
        self.__nome = nome
        self.__email = email
        self.__senha = senha


# Instância/Objeto
lamp1 = Lampada('Branca', 110, 60)
cli1 = Cliente('daciolima', '12345678922')
cc1 = ContaCorrente(5000, 200000, cli1)
user1 = Usuario('Dacio', 'daciolima@email.com', '1234')

print(lamp1.checa_lampada())
print(lamp1.liga_desliga())
print(lamp1.checa_lampada())

cli2 = Cliente('isaaclima', '12345678922')

cc2 = ContaCorrente(6000, 10000, cli2)

print(cc1.mostra_cliente())

print(cc2.mostra_cliente())

cc1._ContaCorrente__cliente.diz()

