"""
Reversed

Obs: Nâo confunda com a função reverse() que estudamos nas listas
A função reverse() só funciona nas listas.

Já a função reversed() funciona com qualquer interável.

Sua função é inverter o interável retornando uma List Reverse Interator

"""
# Exemplo
lista = [1, 2, 3, 4, 5]
res = reversed(lista)
print(type(res))

# Podemos converter o elemento retornando para uma lista, tupla ou Set
# Lista
print(list(reversed(lista)))

# Tupla
print(tuple(reversed(lista)))

# Set # No set não ha como inverter porque conjunto não obedece sequencia
print(set(reversed(lista)))

# Podemos interar sobre os reversed()
for letra in reversed('Dácio Lima'):
    print(letra, end='')

# Podemos fazer o mesmo sem o uso do for
print(''.join(list(reversed('Dácio Lima'))))

# join retira o fatiamento da string criada na lista e uni a uma só.
print(''.join(list(reversed('dacio'))))

# Vimos também como fazer inversão com o slice de string
print('Dacio Lima'[::-1])

# Podemo realizar o reversed() para fazer um loop reverso
for n in reversed(range(0,15)):
    print(n)

# Realizando reversed sem o uso da função reversed()
for n in range(10, -1, -1):
    print(f'Número: {n}')
