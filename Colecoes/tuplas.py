"""
Tuplas (tuple)

Tuplas são bastante parecidadas com as litas:
- As tuplas são imutáveis, ou seja, ao se criar uma tupla ela não muda;
- Tuplas tem parenteses, porém quem as definem são as vírgula;
- Métodos para adição e remoção de elementos nas tuplas não existes, visto que tuplas são imutáveis


# Exemplo de tuplas
tupla1 = (1, 2, 3, 4, 5)
print(tupla1)
print(type(tupla1))

tupla2 = 1, 2, 3, 4, 5
print(tupla2)
print(type(tupla2))

tupla3 = (1) # isso não é uma tupla
print(tupla3)
print(type(tupla3))

tupla4 = (12, ) # isso é uma tupla
print(tupla4)
print(type(tupla4))

tupla5 = 12, # isso é uma tupla
print(tupla5)
print(type(tupla5))

# São usados métodos de soma, valor máximo , valor mínino e Tamanho
tupla7 = (1, 2, 3, 4, 5, 6, 7)
print(sum(tupla7))
print(min(tupla7))
print(max(tupla7))
print(len(tupla7))
"""

# Podemos gerar tuplas usando o range
tupla6 = tuple(range(11))
print(tuple)
print(type(tupla6))

# Desempacotamento de tuplas
tuplas = ('Dacio Lima', 'Wal Lima')
nome1, nome2 = tuplas
print((nome1))
print((nome2))

# Concatenação de tuplas
tupla8 = (1, 2, 3)
print(tupla8)

tupla9 = (10, 22, 43)
print(tupla9)

print(tupla8 + tupla9)
print(tupla8)
print(tupla9)

# Subscrevendo tupla, ou seja, apagando o seu conteúdo e adicionando novos
tupla8 = tupla8 + tupla9
print(tupla8)

# Verificar se há determinado elemento na tupla e conta o seu elemento
tupla10 = (1, 2, 3)
print(3 in tupla10)
print(tupla10.count(3))


# Onde utilizar tupla?
# Devemos utilizar tuplas sempre que não precisamos modificar os dados contidos em uma coleção
meses = ('janeiro', 'fevereiro', 'marco', 'abril', 'maio', 'junho', 'julho', 'agosto', 'setembro', 'outubro', 'novembro', 'dezembro')

# Porque utilizar tuplas?
# - Tuplas são mais rápidas que lista/
# - Tuplas deixa código mais seguro;

