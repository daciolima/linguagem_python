""""
Funções de retorno

São funções que retornam alguma coisa que é diferente de funções que imprime alguma coisa.

OBS:
 - Funções de retorno apenas retorna, mas não imprime.
 - Vantagem de função de retorno é porque você pode adicionar mais alguma informação antes de imprimi-la

Sobre return:
 1 - Ela finaliza a função, ou seja, ela sai de execução da função;
 2 - Podemos ter, em uma função diferentes returns,
 3 - Podemos, em uma função, retornar qualquer tipo de dado e até mesmo múltiplos valores
"""

numeros = [1, 2, 3]

# Função de retorno
num_excluido = numeros.pop()

# Função que imprime alguma coisa
print(numeros)


# Função de retorno
def quadrado(numero):
    return numero * numero

print(quadrado(7))


# Exemplo de vantagem
def dizer_oi():
    return 'Oi'

nome = 'Dacio'
print(f'{dizer_oi()}, {nome}! Bem-vindo!!!')


# Diferentes return
def nova_funcao():
    variavel = True
    if variavel:
        return True
    else:
        return False

print(nova_funcao())


# Retornando multiplos valores
def varios():
    return 1, 2, 3, 4

num1, num2, num3, num4 = varios()

print(num1, num2, num3, num4)

# Gerar um numero pseudo(peseudo pode haver repetição) rondômico(numeros aleatórios) entre 0 e 1.
from random import random
def jogar_moeda():
    valor = random() # Numeros randômicos cai float quando menor que 1
    if valor > 0.5:
        return 'Cara'
    return 'Coroa'

print(jogar_moeda())


