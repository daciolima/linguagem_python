"""
Generators
Em aulas anteriores estudamos:
- List Comprehension
- Dictionary Comprehension
- Set Comprehension

Entenderemos o porque o Tuple Comprehension são chmados de Generators

"""
nomes = ['Carlos', 'Camila', 'Cida', 'Cicero', 'Vania']
print(any(nome[0] == 'C' for nome in nomes))

# List Comprehension
res = [nome[0] == 'C' for nome in nomes]
print(res)
print(type(res))

# Generators - Generators ocupa menos memória visto que ele gera um objeto e não uma lista
res2 = (nome[0] == 'C' for nome in nomes)
print(res2)
print(type(res2))

# getsizeof() -> Função que verifica tamanhoem byte em memória do elemento passado como parâmetro
from sys import getsizeof
print(getsizeof(res2))

# VERIFICAÇÃO
# List Comprehension
list_comp = getsizeof([x * 10 for x in range(1000)])

# Set Comprehension
set_comp = getsizeof({x * 10 for x in range(1000)})

# Dict Comprehension
dict_comp = getsizeof({x: x * 10 for x in range(1000)})

# Generators
gen_comp = getsizeof(x * 10 for x in range(1000))

# Visualizando de tamanhos com relação ao Generators Expression
print(f'Tamanho da list é {list_comp} bytes')
print(f'Tamanho da set é {set_comp} bytes')
print(f'Tamanho da dict é {dict_comp} bytes')
print(f'Tamanho da gen é {gen_comp} bytes')


gen_comp2 = (x * 10 for x in range(1000))

for num in gen_comp2:
    print(num)

