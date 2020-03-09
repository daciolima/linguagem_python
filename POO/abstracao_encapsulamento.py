"""
POO - Abstração e Encapsulamento

O grande objetivo do POO é encapsular osso código dentro de um grupo lógico e hierárquico utilizando
classes.

Encapsular vem da raiz capsula, ou seja, envolucro com várias coisas dentro.


         Classe
-------------------------
/ Atributos e Métodos   /
-------------------------

# Relembrando os atributos/métodos privados em Python

Imagine que temos uma classe chamada Pessoa contendo um atributo privado chamado __nome e um
método privado chamado __falar().

Esses elementos só devem/deveriam ser acessados dentro da classe, mas Python nãp bloqueia este
acesso fora da Classe. COm Python acontece um fenômeno chamado Name Mangling, que faz uma alteração
na forma de se acessar os elementos privados conforme essa assinatura: _Classe__elemento

Ex:
# Acessando atributo privado:
instancia._Classe__nome

# Acessando método privado
instancia._Classe__falar()

Abstração em POO é o ato de expor dados apenas relevantes de uma classe, escondendo atributos e métodos
privados do usuário.

"""

class Conta:

    contador = 49999

    def __init__(self, titular, saldo, limite):
        self.__numero = Conta.contador + 1
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite
        Conta.contador = self.__numero

    def extrato(self):
        print(f'O nome do titular é {self.__titular}. Seu saldo é de R$ {self.__saldo}. Conta com limte de R$ {self.__limite} ')

    def depositar(self, valor):
        if valor > 0:
            self.__saldo += valor
        else:
            print('Valor precisa se positivo')

    def sacar(self, valor):
        if valor > 0:
            if self.__saldo >= valor:
                self.__saldo -= valor
            else:
                print('Saldo insuficiente')
        else:
            print('Valor deve ser positivo!')

    def transferir(self, valor, conta_destino):
        # Retirar da conta origem
        self.__saldo -= valor
        self.__saldo -= 10  # Taxa de transferência paga por quem realizou a transferência
        # Depositar na conta destino
        conta_destino.__saldo += valor



# Testando
conta1 = Conta('Dácio Lima', 600, 500)
conta2 = Conta('Waldilandia Lima', 980, 700)

print(conta1.__dict__)
print(conta2.__dict__)

# Imprimindo da forma Name Mangling
print(conta1._Conta__titular)

# Alterando dados da forma Name Mangling
conta1._Conta__titular = 'Dacio David de Barros Lima'
print(conta1.__dict__)

# Depositando
conta1.depositar(1100)
print(conta1.__dict__)

# Sacando com validação de saldo
conta1.sacar(2000)

# Transferindo entre contas
conta1.transferir(100, conta2)

conta1.extrato()
conta2.extrato()







