"""
Conjuntos em qualquer linguagem de programação, estamos fazendo referência a Teoria dos conjuntos da matemática.

Em python os conjuntos são chamados de Sets.

Sets:
    -   Não possui valores repetidos(se houve ele descarta sem erros);
    -   não possuem valores ordenados;
    -   Não possuem indice;
Conjuntos são usados quando precisamos armazenar algum que não precisar ordenar e não haver necessidade de indexar.

Diferença de maps e sets:
Maps: Tem chave e valor;
Sets: Tem apenas valor.

# Definido conjunto
s = set({1, 2, 3, 4, 5, 6, 7 ,8 , 3})
print(s)
print(type(s))

#Iteirar
for valor in s:
    print(valor)

# Verificar existencia de elemento
if 3 in s:
    print(f'Tem 3')
else:
    print('Não tem o 3')

lista = [45, 69, 32 , 15, 9, 9, 'Dacio']
print(set(lista))


# Exemplo de comportamento entre lista, tuplas, dicionários e conjuntos
lista = [1, 3, 5, 6, 3, 8, 6, 12]
print(f'Lista: {lista}')
tupla = 1, 3, 5, 6, 3, 8, 6, 12
print(f'Tupla: {tupla}')
dicionario = {}.fromkeys([45, 69, 32 , 15, 9, 9, 'Dacio'], 'dict') # Dicionário não repete chaves
print(f'Dicionário: {dicionario}')
conjunto = {45, 69, 32 , 15, 9, 9, 'Dacio'} # Conjuntos não repete valores e faz ordenação própria
print(f'Conjunto: {conjunto}')

# Adicionando e removendo elementos de um conjunto
s = {1, 4, 7}
print(type(s))
s.add(3)
s.add(9)
s.add(5)
print(s)
s.remove(3)
s.remove(7)
s.discard(11)
print(s)

# removendo todos os elementos
s.clear()
print(s)

Obs: Se usar o método remove com um elemento que não existe é retornado um KeyError
     Se usar o método discard com um elemento inexistente não retornará erro.
"""

# Método Matemáticos de Conjuntos
estudante_python = {'Marcos', 'André', 'Geraldo', 'Vânio', 'Kathia', 'Samuel', 'Júnior', 'Oziel'}
estudante_java = {'Fernando', 'Wal', 'Júlia', 'Kathia',' Gustavo', 'Oziel'}

# Veja que alguns alunos de python também estudam Java
# Precisamos gerar um conjunto de nomes únicos
# Forma 1 - Utilizando Union
unicos = estudante_python.union(estudante_java)
print(unicos)

# Forma 2 - Utilizando Pipe |
unicos2 = estudante_python | estudante_java
print(unicos2)


# Precisamos gerar um conjunto de estudantes que estão nos dois conjuntos
# Forma 1 - Utilizando o intersection (Interseção)
ambos = estudante_python.intersection(estudante_java)
print(ambos)

# Forma 2 - Utilizando o & (E comercial)
ambos2 = estudante_python & estudante_java
print(ambos2)

# Precisamos gerar um conjunto dos estudantes que não estão no outro conjunto
so_python = estudante_python.difference(estudante_java)
print(so_python)

so_java = estudante_java.difference(estudante_python)
print(so_java)





