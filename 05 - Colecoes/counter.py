"""
Módulo Collections - Counter

Collections -> High-performance Container Datetypes

https://docs.python.org/3.7/library/collections.html#counter-objects

Counter -> Recebe iterável como parâmetro e cria um objeto do tipo Collections Counter que é parecido
com um dicionário, contendo como chave o elemento da lista passada como parâmetro e como valor a quantidade de ocorrências desse elemento na lista
"""

# Utilizando Counter
# Exemplo 1
from collections import Counter
lista = [1, 3, 5, 6, 8, 9, 13, 16, 18, 22, 23, 26, 28, 39, 6, 13, 1, 3, 3, 9, 3]
res = Counter(lista)
print(type(res))
print(res)

# Exemplo 2 - Fatia por letra toda a string, cria chave e coloca como valor a quantidade de ocorrencia de cada letra
print(Counter('Dacio Lima'))

# Exemplo 3 -
texto = """
    Python é uma linguagem de programação de alto nível,[4] interpretada, de script, imperativa, orientada a objetos, 
    funcional, de tipagem dinâmica e forte. Foi lançada por Guido van Rossum em 1991.[1] Atualmente possui um modelo de 
    desenvolvimento comunitário, aberto e gerenciado pela organização sem fins lucrativos Python Software Foundation. 
    Apesar de várias partes da linguagem possuírem padrões e especificações formais, a linguagem como um todo não é 
    formalmente especificada. O padrão de facto é a implementação CPython.
"""

palavras = texto.split()
print(palavras)
res = Counter(palavras)
print(res)


# Encontrando as cinco palavra com mais ocorrencias no texto
print(f'As tres mais ocorrencias de paravras: {res.most_common(3)}')