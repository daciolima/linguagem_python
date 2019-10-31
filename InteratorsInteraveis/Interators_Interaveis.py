"""
Entendo um interators e um Interables

Interator =>
    - Um objeto que pode ser interado
    - Um objeto que retorna um dado, sendo um elemento por ver quando a função next() é chamada

Iterable =>
    -   Um objeto que irá retornar um interator quando a função itar() for chamada.

"""

nome = 'Dacio'  # É um interável mas não um interator
numeros = [1, 2, 3, 4, 5]  # É um interável mas não um interator

it1 = iter(nome)
it2 = iter(numeros)

print(next(it1))
print(next(it1))
print(next(it1))
print(next(it1))
print(next(it1))

print(next(it2))
print(next(it2))
print(next(it2))
print(next(it2))
print(next(it2))


# Esse exemplo de loop tem rodando por baixo o next()
nome = 'DacioLima'
for letra in nome:
    print(f'{letra}')
