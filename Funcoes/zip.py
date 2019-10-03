"""
Zip

zip() -> Cria um interável (Zip Object) que agrega em tupla elemento de cada um dos interável passando como entrada em pares.

"""

lista1 = [1, 2, 3, 4, 5]
lista2 = [6, 7, 8, 9, 10]
lista3 = [11, 12, 13, 14, 15, 16]

zip1 = zip(lista1, lista2)
print(zip1)
print(type(zip1))

# Sempre podemos gerar uma lista, Tupla ou Dicionário
# Obs: Lembre que uma vez descarregada a informação os dados tem que ser gerados novamente. Veja que
# eles aparecem na list porém nao aparece nas demais.
print(list(zip1))
print(tuple(zip1))
print(dict(zip1))

# Repare que os dados são gerados sempre casada de acordo com a quantidade de interável. Observe o retorno
# incluindo a lista3, sendo essa maior que as anteriores
zip2 = (zip(lista1, lista2, lista3))
print(list(zip2))

# Podemos usar diferentes interáveis com zip
tupla = 1, 2, 3, 4, 5
lista = [6, 7, 8, 9, 10]
dicionario = {'a': 11, 'b': 12, 'c': 13, 'd': 14, 'e': 15}

zt = zip(tupla, lista, dicionario.values())
print(list(zt))

# Lista de tuplas
dados = [(0, 1), (2, 3), (4, 5), (6, 7), (8, 9), (10, 11), (12, 13)]
# o * desempacota os elementos da variável dados
print(list(zip(*dados)))

# Exemplo mais completo
prova1 = [80, 91, 78]
prova2 = [98, 89, 53]
alunos = ['Dacio', 'Wal', 'Isaac']

# Imprimir nome dos alunos com sua maior nota
final = {dado[0]: max(dado[1], dado[2]) for dado in zip(alunos, prova1, prova2)}
print(final)

# Poderiamos usar o map
final2 = zip(alunos, map(lambda nota: max(nota), zip(prova1, prova2)))
print(dict(final2))

