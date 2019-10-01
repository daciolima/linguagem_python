"""
Any e ALl

all() -> Retorna True se todos os elementos de um interável são verdadeiros ou se o interável está vazio.

any() -> Retorna True se algum dos elementos do interável for verdadeiro. Se o interável estiver vazio, retorna False

"""

# Exemplo all()
print(all([1, 2, 3, 4]))
print(all([0, 1, 2, 3, 4]))
print(all([]))

# Exemplo All com list comprehension
# Exemplo 1
nomes = ['Dacio', 'Daniela', 'Daiana', 'Daniela']
nomes2 = ['Marcio', 'Carla', 'Mario', 'Maria']
print(all([nome[0] == 'D' for nome in nomes]))
print(all([nome[0] == 'M' for nome in nomes2]))

# Exemplo 2
# Obs: Um interável vazio convertido em boolean é False, mas o all() entende como True
print(all([letra for letra in 'eio' if letra in 'aeiou']))

print(all([num for num in [1, 2, 3, 4] if num % 2 == 0]))





# Exemplo any()
print(any([0, 1, 2, 3]))  # True

print(any([0, False, {}, []])) # False

print(any([num for num in [2, 4, 6, 8, 10] if num % 2 == 0]))

