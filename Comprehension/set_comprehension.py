"""
Set Comprehension

"""

# Exemplos 1
numeros = {num for num in range(1, 11)}
print(numeros)

# Exemplo 2
numeros2 = {x ** 2 for x in range(10)}
print(numeros2)

# Exemplo 3
letras = {letra for letra in 'Dacio Lima'}
print(letras)