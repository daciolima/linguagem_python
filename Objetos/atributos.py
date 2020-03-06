"""
POO - Atributos

Atributos => Atributos representam as características do objeto, ou seja, pelos atributos
conseguimos representr computacionalmente os estados de um objeto.

Em Python dividimos os a tributos em tres grupos:
    - Atributos de instância;
    - Atributo de classe;
    - Atributos Dinâmicos;

## Atributos de Instância => São atributos declarados dentro do método construtor.

OBS: Método construtor: É um método especial usado para a construção do objeto.

OBS: o Underline duplo torna a propriedade privada, ou seja, usavel somente dentro da classe.

OBS: self => É o ato do objeto executar um método da própria classe no qual pertence a sua instância
"""


"""
Em Python ficou estabelecido por convenção que todo atributo de uma classe é público, ou seja, pode ser acessado
em todo o projeto. Caso queiramos tornar um determinado atributo de forma privada, ou seja, utilizado/acessado apenas 
dentro da própria classe utiliza-se o __ duplo underscore no início do nome do atributo. 
Isso é conhecido Name Mangling.
"""

# ATRIBUTOS DE INSTÂNCIA
# Classe com atributos instância públicos
class Produto:

    def __init__(self, nome, descricao, valor):
        self.nome = nome
        self.descricao = descricao
        self.valor = valor


class Lampada:
    
    def __init__(self, voltagem, cor):
        self.voltagem = voltagem
        self.cor = cor
        self.ligada = False


# Classe com atributos instância privados
class ContaCorrente:
    
    def __init__(self, numero, limite, saldo):
        self.__numero = numero
        self.__limite = limite
        self.__saldo = saldo


class Usuario:

    def __init__(self, nome, email, senha):
        self.__nome = nome
        self.email = email
        self.__senha = senha


class Acesso:

    def __init__(self, email, senha):
        self.email = email
        self.__senha = senha

    def mostra_email(self):
        print(self.email)

    def mostra_senha(self):
        print(self.__senha)

# Exemplo de acesso a atributo privado
user = Acesso('daciolima@gmail', '12345')

# print(user.__senha) # retorna erro Attribute Error
print(user.email)

user.mostra_email()
user.mostra_senha()

print(user._Acesso__senha) # Temos acesso. Mas não deveríamos fazer este acesso. (Name Mangling)



## ATRIBUTOS DE CLASSE
# São atributos declarados diretamente na classe com determinados valores de forma que todas as instâncias
# oriundas dessa classe terão acesso a esses atributos e obviamente os mesmos valores.
# Ex:
class Produto:

    # Atributo de classe
    imposto = 1.05
    contador = 0

    def __init__(self, nome, descricao, valor):
        self.id = Produto.contador + 1
        self.nome = nome
        self.descricao = descricao
        self.valor = valor * Produto.imposto
        Produto.contador = self.id


# Teste
p1 = Produto('Sapato', 'Tenis', 180.0)
print(p1.valor) # Acesso possível, mas incorreto de um atributo de classe
p2 = Produto('Sapato', 'Tenis', 250.0)
print(p2.valor)

# Não precisamos criar uma instância de uma classe para fazer acesso a um atributo de classe
print(Produto.imposto) # Acesso correto a um atributo de classe

print(p1.id)
print(p2.id)

# OBS: Em Java os atributos de classe do Python são chamados de atributos estáticos.


# ATRIBUTOS DINÂMICOS (Esse tipo de atributo não é comum)
# É um atributo de instância que pode ser criado em tempo de execução
# OBS: O Atributo dinâmico será exclusivo da instância que o criou
p3 = Produto('Carro', 'Maverick', 105.000)
# Criando um atributo dinâmico
p3.peso = '3 Toneladas'
# Imprimindo
print(f'Tipo: {p3.nome}', f'Descrição: {p3.descricao}', f'Valor: {p3.valor}', f'Peso(Atributo Dinâmico): {p3.peso}')


# Deletando atributos dinâmicamente através do comando del
# Imprimindo a estrutura do objeto(Valores em dicionário)
print(p2.__dict__)
print(p3.__dict__)

# Deletando
del p3.peso
del p3.descricao
del p3.valor

print(p3.__dict__)