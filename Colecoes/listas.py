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


"""

# Exemplos
lista1 = [1, 2, 3, 4, 5, 6, 7, 8, 8, 9, 10, 1]
lista2 = ['d','a','c','i','o', ' ', 'l', 'i', 'm', 'a']
lista3 = []
lista4 = list(range(1, 11))
lista5 = list('Dacio Lima')
lista6 = ['Developer', 'Python', 'MongoDB', 'React']
lista7 = [1, 2, True, 'Dacio', 'd', [1, 2, 3], 3334455566]

carrinho = []
produto = ''
while produto != 'sair':
    print('Digite um produto na listaou digite sair para sair: ')
    produto = input()
    if produto != 'sair':
        carrinho.append(produto)
for produto in carrinho:
    print(produto)






