"""
POO - Métodos
- Métodos(Funções) - Representam os comportamentos do objeto, Ou seja, as ações que este objeto pode
realizar no seu sistema.
EM Python dividimos os métodos em 2 grupos:
    - Métodos de Intância;
    - Métodos de Classe.

# Método de Instância => É todo método de uma classe e que precisa de uma instância daquela classe para
utiliza-lo.

# O método dunder __init__ é um método especial chamado de contrutor e sua função é construir o objeto
a partir da classe.

OBS: Todo elemento em Python que inicia e finaliza com duplo underline é chamado de dunder(Double Underline)
OBS: Os métodos/funções dunder em Python são chamados de métodos mágicos.

ATENÇÂO: Por mais que possamos criar funções dunder, isso não é aconcelhável visto que pode haver funções nativas
na linguagem Python com mesmo nome e isso poderá alterar o comportamento delas.

Métodos devem ser assinados com letras minusculas. Se for nome comporto, o nome deverá ser separadas por underline

"""


class Lampada:
    # Métodos Construtores
    def __init__(self, cor, voltagem, luminosidade):
        self.__cor = cor
        self.__voltagem = voltagem
        self.__luminosidade = luminosidade
        self.__ligada = False


class ContaCorrente:

    # Inicializar com esse valor
    contador = 49999

    # Métodos Construtores
    def __init__(self, limite, saida):
        # Objeto já é instanciado com valor incrementado
        self.__numero = ContaCorrente.contador + 1
        self.__limite = limite
        self.__saida = saida
        # Proximo objeto já será incrementado com o valor do anterior + 1
        ContaCorrente.contador = self.__numero


class Produto:

    contador = 8

    # Métodos Construtores
    def __init__(self, nome, descricao, valor):
        self.__id = Produto.contador + 1
        self.__nome = nome
        self.__descricao = descricao
        self.__valor = valor
        Produto.contador = self.__id

    def desconto(self, porcentagem):
        """ Retorna o valor do produto com desconto de acordo com a entrada da porcentagem"""
        return (self.__valor * (100 - porcentagem)) / 100


# Importação de Library de criptografia
from passlib.hash import pbkdf2_sha256 as crypto


class Usuario:

    # Métodos Construtores
    def __init__(self, nome, sobrenome, email, senha):
        self.__nome = nome
        self.__sobrenome = sobrenome
        self.__email = email
        self.__senha = crypto.hash(senha, rounds=200000, salt_size=18)

    def chegar_senha(self, senha):
        if crypto.verify(senha, self.__senha):
            return True
        return False

    def nome_completo(self):
        return f'{self.__nome} {self.__sobrenome}'


# Exemplo 1 de Método de instancia
p1 = Produto('PlayStation', 'Video Game', 2380)
print(p1.desconto(10))
print(Produto.desconto(p1, 50))

# Exemplo 2 de Método de instancia
user = Usuario('Dacio', 'Lima', 'dacio@email.com', '1234')
print(user.nome_completo())
print(Usuario.nome_completo(user))

# Exemplo de entrada de senha com criptografia
nome = input('Informe nome: ')
sobrenome = input('Informe sobrenome: ')
email = input('Informe email: ')
senha = input('Informe senha: ')
confirma_senha = input('Confirme sua senha: ')

if senha == confirma_senha:
    user = Usuario(nome, sobrenome, email, senha)
else:
    print('Senha não confere...')
    exit(42)

print('Usuário cadastrado com sucesso!')

senha = input('Informe sua senha: ')

if user.chegar_senha(senha):
    print('Acesso Permitido')
else:
    print('Acesso Negado!!!')
print(f'Senha do User criptografada: {user._Usuario__senha}') # Forma não recomendada


# Métodos de Classe
# Para se criar um Método de classe deve-se usar o decorator @class_method marcando o metodo a ser de classe
# recebendo o parâmetro (cls) que é a própria classe
# Metodos de Classe usa atributos apenas de classe, ele não tem acesso a atributos de instância dos
# objetos gerados dessa classe.
# Metodos de Classe em Python são conhecidos em outras linguagens também como métodos estáticos, lembrando que
# em Python tem seus próprios métodos estáticos assinados com o decorator @staticmethod
# No método de estático em Python é quando o método, criando dentro de uma classe, não tem acesso a atributos
# de instancias e nem de classe, ou seja, processa algo isolado e sendo acessivel tanto pela instância como
# pela classe.
class Aluno:

    contador = 0

    # Método de Classe
    @classmethod
    def conta_aluno(cls):
        print(f'Temos {cls.contador} alunos no sistema')

    @staticmethod
    def imprime():
        return 'Imprimindo algo do método estático'

    def __init__(self, nome, email):
        self.__id = Aluno.contador + 1
        self.__nome = nome
        self.__email = email
        Aluno.contador = self.__id

    # Criaão de um Método de instância privado
    def __gera_usuario(self):
        return f'{self.__email.split("@")[0] + str(self.__id)}'


# Chamando método de classe
aluno = Aluno('Dacio Lima', 'daciolima30@hotmail.com')
Aluno.conta_aluno() # Forma correta de uso do método de classe
aluno.conta_aluno() # Possível ser usado, mas não recomendável

# Chamando um método de instância privado
print(aluno._Aluno__gera_usuario())  # Acesso, de forma não recomendada

# Chamado um método estático
print(aluno.imprime())
print(Aluno.imprime())
