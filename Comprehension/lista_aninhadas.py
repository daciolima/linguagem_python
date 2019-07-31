"""
Listas Aninhadas (Nested Lists)

    -   Algumas linguagens de programação(C/Java) possuem uma estrutura de dados chamada de arrays:
        -   Unidimencionais(Arrays/Vetores)
        -   Multidimencionais (Matrizes)

    Em Python chamamos arrays de listas
    numeros = [1, 2, 3, 4, 5]

"""
listas = [[1, 2, 3], [4, 5, 6], [7, 8, 9]] # Matriz de 3 x 3
print(listas, end='')
print(' ')
print(listas[0][2])
for lista in listas:
    for num in lista:
        print(num, end='')

# List Comprehension
#[[print(valor) for valor in lista] for lista in listas]

#Gerando tabuleiro para jogo da velha
velha = [['X' if numero % 2 == 0 else '0' for numero in range(1, 4) for valor in range(1, 4)]]
print(velha)

print([['*' for i in range(1, 4)] for j in range(1, 4)])



