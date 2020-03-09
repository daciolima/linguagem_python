"""
POO - Herança - (Inheritance)

A ideia de herança e a de reaproveitar código como também extender classes.

OBS: Com uma herança a partir de uma classe existente, nós extendemos outra classe
que passa a herdar tributos e métodos da classe herdada.

OBS: Sempre que existir entidades com atributos e métodos comuns entre si, pode-se está criando uma classe
genérica com esses atributos comuns para ser herdada pelas classes que tinham os atributos e métodos
em comum.


"""


class Pessoa:

    def __init__(self, nome, sobrenome, cpf):
        self.__nome = nome
        self.__sobrenome = sobrenome
        self.__cpf = cpf

    def nome_completo(self):
        return f'O nome completo é: {self.__nome} {self.__sobrenome}'


# Cliente herdando de Pessoa
class Cliente(Pessoa):

    def __init__(self, nome, sobrenome, cpf, renda):
        # Primeira forma de chamar o metodo construtor da classe pai(Pessoa). OBS: Forma não comum
        super().__init__(nome, sobrenome, cpf)
        self.__renda = renda


# Funcionário herdando de Pessoa
class Funcionario(Pessoa):

    def __init__(self, nome, sobrenome, cpf, matricula):
        # Segunda forma de chamar o metodo construtor da classe pai(Pessoa). OBS: Forma comum.
        Pessoa.__init__(self, nome, sobrenome, cpf)
        self.__matricula = matricula

    def nome_completo(self):
        # Linha para imprimir o metodo nome_completo vindo da classe pai
        print(super().nome_completo())
        # Linha para imprimir o metodo nome_completo modificado aqui na classe Funcionario
        return f'A matrícula é: {self.__matricula} e nome é: {self._Pessoa__nome}'

# Testando
cliente = Cliente('Dacio', 'Lima', '123.456.789-99', 1800)
funcionario = Funcionario('Waldilandia', 'Lima', '345.655.443-23', 34562311)

print(cliente.nome_completo())
print(funcionario.nome_completo())

print(cliente.__dict__)
print(funcionario.__dict__)

print(cliente.nome_completo())
print(funcionario.nome_completo())
