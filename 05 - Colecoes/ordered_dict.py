"""
Módulo Collections: Ordered Dict
https://docs.python.org/3.7/library/collections.html#ordereddict-objects

dicionario = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}
for chave, valor in dicionario.items():
    print(f'Chave: {chave}, Valor: {valor}')

Ordered Dict => É um dicionário que nos garante a ordem de inserção dos elementos.

"""
from collections import OrderedDict

dicionario = OrderedDict({'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5})
for chave, valor in dicionario.items():
    print(f'Chave: {chave}, Valor: {valor}')


