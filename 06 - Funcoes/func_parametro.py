"""
Funções com parâmetros (de entrada)
    -   Funções que recebem dados para serem processados dentro da mesma:

Temos funçoes que:
    -   Não possuem entrada;
    -   Não possuem saída;  # Ausencia de return
    -   Possuem entrada, mas não possuem saída;
    -   Não possuem entrada, mas possuem saída;
    -   Possuem entrada e saída.

Obs:
    -   Usar parametros com nomes que façam sentido

Atenção:
    -   Parâmetro: São varíaveis declaradas na definição de uma função;
    -   Argumentos são dados passados durante a execução de uma função
"""

# Função com entrada <- Entrada = Parâmetro
def quadrada(entrada):
    return entrada * entrada

print(f'A raiz quadrada é: {quadrada(7)}') # A string chamamos de argumentos


# Função com 2 entrada
def soma(num1, num2):
    return num1 + num2

print(soma(5, 4))


# Argumentos nomeados - Keyword Arguments
nome = 'Dácio'
sobrenome = 'Lima'

def nome_completo(nome, sobrenome):
    return f'Meu nome é {nome} {sobrenome}'

print(nome_completo(nome=nome, sobrenome=sobrenome))
print(nome_completo(nome=sobrenome, sobrenome=nome))  # Alterando as entradas
