"""
Dictionary Comprehension

"""
# Exemplo 1
numeros = {'a':1, 'b':2, 'c':3, 'd':4, 'e':5, 'f':6, 'g':7}
dicionario = {chave:valor **2 for chave, valor in numeros.items()}
print(dicionario)

# Exemplo 2
lista = [1, 2, 3, 4, 5]
quadrado = {valor:valor **2 for valor in lista}
print(quadrado)

# Exemplo 3
chaves = 'chaves'
valores = [1, 2, 3, 4, 5, 6]
mistura = {chaves[i]: valores[i] for i in range(0, len(chaves))}
print(mistura)

# Exemplo 4
chaves = 'chaves'
valores = [1, 2, 3, 4, 5, 6]
res = {num: ('par' if num % 2 == 0 else 'impar') for num in valores }
print(res)