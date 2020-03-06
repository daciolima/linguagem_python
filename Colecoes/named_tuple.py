"""
Módulo Collections => Named Tuple (Tupla Nomeada)
https://docs.python.org/3/library/collections.html#collections.namedtuple

São tuplas diferenciadas onde especificamos um nome para a mesma e também para os parâmetros
no print podemos chamar por nome da variavel.parametro

"""

from collections import namedtuple

# Definindo nome e parâmetro
# Forma 1
cachorro = namedtuple('Cachorro', 'idade raca nome')

# Forma 2
cachorro2 = namedtuple('Cachorro', 'idade, raca, nome')

# Forma3
cachorro3 = namedtuple('cachorro', ['idade', 'raca', 'nome'])


#Aplicando
ray = cachorro(idade=2, raca='Chow-CHow', nome='ray')

print(ray)


# printando no modo named
print(ray.idade)
print(ray.raca)
print(ray.nome)

# Retornando um index de algum valor
print(ray.index('ray'))


