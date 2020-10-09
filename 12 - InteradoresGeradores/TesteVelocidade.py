"""
Teste de Velocidade com Expressões Geradoras

Expressões Geradoras são mais rápidas, vão gerando logo os números(next)
Enquando que a list comprehension espera que todos os números sejam gerados para depois somar.

Isso é bem visivel quando se trabalha ciência de dados e inteligencia artificial.

"""

# # Generators (Geradores)
# def nums():
#     for num in range(1, 10):
#         yield num
#
# gen1 = nums()
# print(gen1) # Generators
# print(next(gen1))
# print(next(gen1))
# print(next(gen1))
#
#
# # Generators Expression (Expressões Geradores)
# ge = (num for num in range(1, 10))
# print(ge) # Generators Expression
# print(next(ge))
# print(next(ge))
# print(next(ge))


# Realizando teste de Velocidade
import time

# Generator Expression
gen_inicio = time.time()
print(sum(num for num in range(1000000000))) # 100 milhões
gen_tempo = time.time() - gen_inicio

# List Comprehension
list_inicio = time.time()
print(sum([num for num in range(1000000000)])) # 100 milhões
list_tempo = time.time() - list_inicio

print(f'Generator Expression levou {gen_tempo}')
print(f'List Comprehension levou {list_tempo}')


