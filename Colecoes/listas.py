"""
Listas

Listas em python funcionam com vetores/matrizes, ()arrays em outras linguagens, com a diferença de que serem
Dinânmicos e também de podermos colocar QUALQUER tipo de dados.

Linguagens C/JAVA esses arrays devem ser de tamanho fixo e somente um tipo de dado

Lista em Python é dinâmica e tamanho ilimitado, ou seja, aceita qualquer tipo de dado e o limite vai de acordo com a memória do computador



# Podemos checar se determinado valor está na lista
num = 18
if num in lista4:
    print(f'Encontrei o número: {num}')
else:
    print(f'Não encontrei o : {num}')

if 'c' in lista5:
    print(f'Encontrei o número: c')
else:
    print(f'Não encontrei a letra c')


# MÉTODOS AGREGADOS A DADOS DO TIPO LIST
# Método .sort() => Ordena a lista
lista2.sort()
print(lista2)

# Método retorna o número de ocorrências de um valor informado no parametro do método dentro de uma lista
# Método .count(valor)
print(lista1.count(1))
print(lista2.count('a'))

# Método .append(valor) adicionar no final da lista apenas um valor por vez
print(lista1)
lista1.append(3)
print(lista1)

# Append de lista dentro de lista
lista1.append([1,3,5])  # Coloca a lista como elemento único(sublista)
print(lista1)

if [1, 3, 5] in lista1:
    print('Encontrei a lista')
else:
    print('Não encontrei a lista')

# Adiciona individualmente todos os elementos da lista passada como parâmetro. Só aceita dados do tipo interáveis. Ex: Lista, String
lista1.extend([123, 44, 67])
print(lista1)

# Adicionar valores em uma determinada ordem deslocando os demais os demais pra frente
lista1.insert(2, 'NovoValor')
print(lista1)

# Juntar listas
lista3 = lista1 + lista2
print(lista3)

# Inprime valores no modo inverso
lista1.reverse()  # Mesmo resultado => print(lista1[::-1]). Isso se chama Slice
print(lista1)

# Contar os elementos da uma lista
print(len(lista1))

# Removendo ultimo elemento da lista retornando o mesmo na tela
print(lista1)
lista1.pop()
print(lista1)

# Podemos remover um elemento pelo indice deslocando todos os demais para esquerda
lista5.pop(2)
print(lista5)

# Remover todos os elementos da lista
print(lista5)
lista5.clear()
print(lista5)

# Converter uma string para uma lista
curso = 'Sou desenvolvedor de sistemas'
print(curso)
curso = curso.split()
print(curso)

# Separa elementos de uma lista por caracter desejado
curso = 'Linguagem Python'
print(curso)
curso = curso.split(', ')
print(curso)

# Convertendo uma lista em uma string. Pega cada elemento atribui o caracter desejado uni.
curso = ' '.join(lista6)
print(curso)

# Iteirando sobre uma lista utilizando for
for el in lista1:
    print(el)
    soma = soma + el
print(soma)


carrinho = []
produto = ''
while produto != 'sair':
    print('Digite um produto na listaou digite sair para sair: ')
    produto = input()
    if produto != 'sair':
        carrinho.append(produto)
for produto in carrinho:
    print(produto)

# Utilizando variáveis em lista
numeros = [1, 2, 3, 4, 5]
print(numeros)
num = 0
num1 = 1
num2 = 2
num3 = 3
num4 = 4
num5 = 5

numeros = [num, num1, num2, num3, num4, num5]
print(numeros)

# Acessando cores da lista, pense sempre como uma roda
cores = ['vermelho', 'azul', 'Amarelo']
print(cores[0])
print(cores[1])
print(cores[2])
print(cores[3])
print(cores[-1])

# Iterar usando for
cores = ['vermelho', 'azul', 'Amarelo']
for cor in cores:
    print(cor)

# Iterar usando o while
indice = 0
while indice < len(cores):
    print(cores[indice])
    indice = indice + 1


# Gerar indice em um for
for ind, cor in enumerate(cores):
    print(ind, cor)

# Lista aceitam repetição
lista = []
lista.append(42)
lista.append(42)
lista.append(36)
print(lista)

# Encontrar o index baseado no valor passado por parametro, retorna o index do primeiro valor encontrado
numeros = [1, 5, 7, 8, 9, 45, 67]
print(numeros.index(9))

# Busca index dos valores a partir do index informado, no exemplo: procurar o 45 a partir do index 3
numeros = [1, 5, 7, 8, 9, 45, 67]
print(numeros.index(45, 3))

# Busca index dos valores entre os index informados, no exemplo: procurar o 45 entre os index 3 e 6
numeros = [1, 5, 7, 8, 9, 45, 67]
print(numeros.index(45, 3, 6))

# Realiza troca de valores nos index
lista6 = ['Developer', 'Python', 'MongoDB', 'React']
lista6[0], lista6[1] = lista6[2], lista6[3]
print(lista6)



# Revisão de slicing
# lista[inicio:fim:passo]
# range[inicio:fim:passo]

# Exemplo
lista1 = [1, 2, 3, 4, 5, 6, 7, 8, 8, 9, 10, 1]
print(lista1[::])  # Pega todos os elementos
print(lista1[1:])  # Pega todos os elementos a partir do index 1
print(lista1[:2])  # Pega todos os elementos até o index 2
print(lista1[1:3])  # Pega todos os elementos do index 1 até o 3
print(lista1[1:-1])  # Pega todos os elementos do index 1 até o último
print(lista1[1::2])  # Pega todos os elementos do index 1 até o último pegando de 2 em 2
print(lista1[::2])  # Pega todos os elementos do index 0 até o último pegando de 2 em 2
print(lista1[::-1])  # Pega todos os elementos do index 0 até o último pegando do último até o primeiro
lista5 = list('Dacio Lima')
print(lista5[::-1])

# Buscas
print(sum(lista1))# Soma os valores - Somente numeros reais
print(min(lista1))# Menor valores - Somente numeros reais
print(max(lista1))# Maior valores - Somente numeros reais
print(len(lista1))# Tamanho da lista - Todos so tipos de dados


# Transformação de lista em tupla
print(lista1)
print(type(lista1))

tupla = tuple(lista1)
print(tupla)
print(type(tupla))

# Desempacotamento de lista, O numero de variáveis deve ser igual ao número de elementos a serem desempacotados
num1, num2, num3 = lista1
print(num1)
print(num2)
print(num3)

# Copiando uma lista para outra(Deep Copy e Shallow Copy)
# Forma 1 - (Deep Copy) - Realiza copia sem afetar a lista anterior
print(lista1)
nova = lista1.copy()  #  <- Deep Copy
print(nova)
nova.append(50)
print(lista1)
print(nova)

# Forma 2 - (Shallow Copy) - Realiza copia afetando lista anterior
print(lista1)
nova = lista1   #  <- Shallow Copy
print(nova)
nova.append(50)
print(lista1)
print(nova)
"""

# Exemplos
lista1 = [1, 2, 3, 4, 5, 6, 7, 8, 8, 9, 10, 1]
lista2 = ['d','a','c','i','o', ' ', 'l', 'i', 'm', 'a']
lista3 = []
lista4 = list(range(1, 11))
lista5 = list('Dacio Lima')
lista6 = ['Developer', 'Python', 'MongoDB', 'React']
lista7 = [1, 2, True, 'Dacio', 'd', [1, 2, 3], 3334455566]












