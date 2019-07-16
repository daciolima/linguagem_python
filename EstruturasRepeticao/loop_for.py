"""
Loop for

Loop => É uma estrutura de repetição
For = É uma estrutura

Usamos loop para inteirar sobre uma sequencia ou sobre valores interáveis

Exemplod e interável:
    -   String,
    -   Lista,
    -   Range
"""

# Iteração sobre String
nome = 'Dacio Lima'
for letra in nome:
    print(letra)

# Por padrão o end tem implicito o \n, para alterar basta subscrever adicionando o caracter necessário
nome = 'Dacio Lima'
for letra in nome:
    print(letra, end='')

# Iteração sobre lista
lista = [1, 2, 3, 4, 5]
for numero in lista:
    print(numero)

# Iteração sobre range
valores = range(1, 10)
for valor in range(1, 10):
    print(valor)

# Usando enumerate
# i = Indice, v = valor
for i, v in enumerate(nome):
    print(nome[i])

# Descatando o indice
for _, v in enumerate(nome):
    print(nome[i])

# Retorna o indice e seu respectivo valor
for letra in enumerate(nome):
    print(letra)

# Retorna o indice
for letra in enumerate(nome):
    print(letra[0])
# Retorna o valor
for letra in enumerate(nome):
    print(letra[1])

# Exemplo de for usando input
qtd = int(input('Quantas vezes deve-se realizar o loop? \n'))
soma = 0
for i in range(1, qtd+1):
    num = int(input(f'Informe o {i}/{qtd} valor: '))
    soma = soma + num
print(f'A soma é: {soma}')

# Elemento da tabela de Emoji: https://apps.timwhitlock.info/emoji/tables/unicode

for _ in range(3):
    for num in range(1, 15):
        print('\U0001F605' * num)


