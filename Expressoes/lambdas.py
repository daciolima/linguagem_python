""""
Utilizando Lambdas

Conhecidas como expressões Lambdas, ou simplesmente Lambdas. São funções sem nome, ou seja, funções anônimas.

"""

# Exemplo
# FUnção normal
def funcao(x):
    return 3 * x + 1
print(funcao(4))

# Função Lambda
lambda x: 3 * x + 1

# COmo Utilizar Expressão lambda
calc = lambda x: 3 * x + 1
print(calc(4))

# Podemos ter expressoes lambdas com múltiplas entradas
nome_completo = lambda nome, sobrenome: nome.strip().title() + ' ' + sobrenome.strip().title()
print(nome_completo('Dacio', 'Lima'))

# Em funções Python podemos ter nenhuma ou várias entradas. Em lambdas também
amar = lambda: 'Como não amar Python'
uma = lambda x: 3 * x + 1
dois = lambda x, y: (x * y) ** 0.5
tres = lambda x, y, z: 3 / (1 / x + 1 / y + 1 / z)

print(amar())
print(uma(6))
print(dois(6, 7))
print(tres(6, 7, 8))

