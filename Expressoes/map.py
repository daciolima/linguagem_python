"""
    Map
    map é uma função onde é passado dois valores, uma função e um interável a ser carregado na função.
    # Obs: Após exibir dados retornado de uma função map() os resultados retornados na variável são apagados
"""

import math

def area(r):
    # Calcular a área de um circulo
    return math.pi * (r ** 2)

print(area(4))
print(area(5.2))


# Forma comum
raios = [2, 5, 7.1, 6.3, 10, 44]
areas = []
for r in raios:
    areas.append(area(r))
print(areas)

# Forma 2 - Usando map
areas2 = map(area, raios)
print(areas2)
print(type(areas2))
print(list(areas2))

# Forma 3 - Usando lambda
print(list(map(lambda r: math.pi * (r ** 2), raios)))

# Mais um exemplo - Convertendo Celsius para Fahrenheit
cidades = [('Berlin', 29), ('Cairo', 36), ('Buenos Ayres', 19), ('Los Angeles', 26), ('Tokio', 27), ('Nova York', 28), ('Londres', 22)]
print(cidades)
c_para_f = lambda dado: (dado[0], (9/5) * dado[1] + 32)
print(list(map(c_para_f, cidades)))

