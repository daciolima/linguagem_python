"""
POO - Propriedades - Properties

Em linguagem de programação como o Java, ao declararmos atributos privados nas classes
costumanos criar métodos publicos para manipulações desses atributos. Esses métodos
são conhecidos por getters e setters, onde os getters retornam o valor do atributo e os setters alteram o valor
dos atributos.

Com Getters e Setters Python trabalha de forma diferente.

Obs: Com relação a Getters o Python trabalha com uma tag chamada @property assinada acima do método. ex:
    @property
    def numero(self):
        return self.__numero

Obs: Com relação a Setters o Python trabalha com uma tag chamada @nome_metodo.setter assinada acima do método. ex:
    @limite.setter
    def limite(self, novo_limite):
        self.__limite = novo_limite

Obs: Você pode criar uma método é assina-lo como uma propriedade colocando uma tag @property. ex:
    @property
    def valor_total(self):
        return self.__saldo + self.__limite

Obs: Em métodos assinados como getters e setters em python não precisa usar o () no final.

"""


class Conta:

    contador = 49999

    def __init__(self, titular, saldo, limite):
        self.__numero = Conta.contador + 1
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite

    @property
    def numero(self):
        return self.__numero

    @property
    def titular(self):
        return self.__titular

    @property
    def saldo(self):
        return self.__saldo

    @property
    def limite(self):
        return self.__limite

    @limite.setter
    def limite(self, novo_limite):
        self.__limite = novo_limite

    @property
    def valor_total(self):
        return self.__saldo + self.__limite

    def extrado(self):
        return f'O saldo do titular {self.__titular} é de {self.__saldo}'

    def depositar(self, valor):
        if valor > 0:
            self.__saldo += valor
        else:
            print('Valor deve ser positivo!')

    def sacar(self, valor):
        if self.__saldo > valor:
            self.__saldo -= valor
        else:
            print('Saldo insuficiente')

    def transferir(self, valor, conta_destino):
        self.__saldo -= valor
        conta_destino.__saldo += valor


# Testando
conta1 = Conta('Dacio Lima', 500, 600)
conta2 = Conta('Waldilandia Lima', 800, 700)

print(conta1.extrado())
print(conta2.extrado())

soma = conta1.saldo + conta2.saldo
print(f'A Soma do saldo das contas é {soma}')

print(conta1.__dict__)
conta1.limite = 900
print(conta1.__dict__)