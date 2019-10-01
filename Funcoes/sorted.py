"""
Sorted

Não confunda apesar do nome, com a função sort() que já estudamos em Lista.
O sort() só funciona em listas

Podemos utilizar o sorted() com qualquer interável.

Como o próprio nome diz, sorted() serve para ordenar

sorted() -> Serve para ordenar qualquer interável retornando uma lista com os elementos ordenados.
Independente da origem do tipo do interável, o sorted() retorna sempre uma lista.

"""
numeros = [1, 2, 3, 4, 5, 6, 7, 7]
print(numeros)
print(sorted(numeros))
print(set(sorted(numeros)))
print(sorted(numeros, reverse=True))  # Ordena do maior para o menor


# Podemos utilizar o sorted() para coisas mais complexas.
usuarios =[
    {'username': 'samuel', 'tweets': ['Eu adoro bolos', 'Eu adoro pizzas']},
    {'username': 'carla', 'tweets': ['Eu amo gato']},
    {'username': 'jeff', 'tweets': []},
    {'username': 'bob123', 'tweets': [], 'cor': 'amarelo'},
    {'username': 'doggo', 'tweets': ['Eu gosto de cachorro', 'Vou sair hoje']},
    {'username': 'gal', 'tweets': [], 'cor': 'preto', 'musica': 'rock'}
 ]

print(usuarios)

# Listando um dicionário
print(sorted(usuarios, key=len))

# Listando um dicionário por username em ordem alfabética de Z - A
print(sorted(usuarios, key=lambda usuario: usuario['username'], reverse=True))

# Listando um dicionário por números de tweets
print(sorted(usuarios, key=lambda usuario: len(usuario['tweets'])))


# Outro exemplo
musicas = [
    {'titulo': 'Deus é fiel', 'tocou': 3},
    {'titulo': 'Alegria', 'tocou': 2},
    {'titulo': 'O poder de Deus', 'tocou': 20},
    {'titulo': 'sacrificio', 'tocou': 35}
]

# Ordenando da menos tocada para a mais tocada
print(sorted(musicas, key=lambda musica: musica['tocou']))

# Ordenando da mais tocada para a menos tocada
print(sorted(musicas, key=lambda musica: musica['tocou'], reverse=True))
