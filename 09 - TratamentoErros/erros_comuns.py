"""
Erros mais comuns em Python

OBS:
1 - Exceptions e Erros são sinônimos na programação;
2 - Importante ler e prestar atenção na saída de erro

ATENÇÃO: è importante prestar atenção e aprender a ler as saídas de erros gerados pela execução
do nosso código.


 NameError -> Occore quando uma variável ou função não foi declarada
 Código abaixo gera erro NameError no console.
printf('Olá!')

 Erro NameError por não existencia de variável msg haja vista que a mesma só é criada após condição aceita
 a = 10
 if a > 20:
     msg = a + ' é maior!'
 print(msg)

TypeError -> Ocorre quando uma função/operação é aplicada a um tipo errado
Erro ocasionado pelo valor não ser interável
print(len(5))


IndexError -> Ocorre quando tentamos acessar um elemento em uma lista ou outr tipo de dados
 indexado utilizando um índice inválido
 lista = ['Dacio']
 print(lista[6])

ValueError -> Ocorre quando uma função/operação built-in(integrado) recebe um argumento com tipo correto
 Mas valor inapropriado
print(int('Dacio'))

KeyError -> Ocorre quando tentamos acessar um dicionário com uma chave que não existe
dic = {'nome':'Dacio'}
print(dic['1'])

AttributeError -> Ocorre quando uma variável não tem um atributo/função
Não existe a função sort para tuplas
tupla = (1, 2, 3, 4)
print(tupla.sort())

IndentationError -> Ocorre quando há erro na identação do código
def nova():
print('Nova Função')

"""
