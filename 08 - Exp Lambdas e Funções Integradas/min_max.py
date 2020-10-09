"""
Max e Min
max() -> retorna o maior valor de um interável ou o maior valor de dois ou mais elementos
min() -> retorna o menor valor de um interável ou o menor valor de dois ou mais elementos
"""

lista = [1, 4, 6, 89, 34, 67, 55]
print(max(lista))

dicionario = {'1': 1, '2': 4, '3': 6, '4': 89, '5': 34, '6': 67, '7': 55}
print(max(dicionario))
print(max(dicionario.values()))

lista2 = [78, 4, 6, 89, 34, 67, 55]
print(min(lista2))

# Verificando maior/menor baseado na entrada
#val1 = int(input('Informe o valor 1:'))
#val2 = int(input('Informe o valor 2:'))

#print(max(val1, val2))

# Verificando letras como maior
print(max('a', 'b', 'c'))
print(max('a', 'bc', 'abc'))

print(max('Dacio Lima'))

# o min() é o inverso de tudo que foi passado com o max
nomes = ['Dacio', 'Marcio', 'Tim', 'Wal', 'Samuel']
print(min(nomes))  # Pega como menor usando ordem alfabética

print(max(nomes, key=lambda nome: len(nome))) # Altera a forma de verificar quem o maior, nessa caso foi alterado para tamanho do nome

# Mais exemplo
musicas = [
    {'titulo': 'Deus é fiel', 'tocou': 3},
    {'titulo': 'Alegria', 'tocou': 2},
    {'titulo': 'O poder de Deus', 'tocou': 20},
    {'titulo': 'sacrificio', 'tocou': 35}
]

print(max(musicas, key=lambda musica: musica['tocou']))  # Cada música de musicas verificar a chave tocou-me e retorna a maior
print(min(musicas, key=lambda musica: musica['tocou']))  # Cada música de musicas verificar a chave tocou-me e retora a menor

# Forma 1 de imprimir o titulo
print(max(musicas, key=lambda musica: musica['tocou'])['titulo'])

# Forma 2 de imprimir o titulo
titulo2 = (min(musicas, key=lambda musica: musica['tocou']))
print(titulo2['titulo'])

# DESAFIO -> Como encontrar a música mais tocada e a menos tocada sem usar max(), min() e lambda?

# VERIFICANDO MAIOR
max = 0
for maior in musicas:
    if maior['tocou'] > max:
        max = maior['tocou']

for musica in musicas:
    if musica['tocou'] == max:
        print(musica['titulo'])


# VERIFICANDO MENOR
min = max
for menor in musicas:
    if menor['tocou'] < min:
        min = menor['tocou']

for musica2 in musicas:
    if musica2['tocou'] == min:
        print(musica2['titulo'])


