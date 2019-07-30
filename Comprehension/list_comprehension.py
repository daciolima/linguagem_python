"""
Utilizando List Comprehension nós podemos gerar novas listas com dados processados a partir de outro interável
Podemos usar estruturas condicionais
"""

# Exemplo 1 - A cada numero da lista numeros multiplique por numero por 10
numeros = [1,2 ,3 ,4, 5, 6, 7]
res = [numero * 10 for numero in numeros]
print(res)

# Exemplo 2 - A cada numero da lista numeros use como parâmetro na funcao  e retorne
def funcao(valor):
    return valor * valor
res = [funcao(numero) for numero in numeros]
print(res)

# Exemplo - Loop vs List Comprehension
# Loop
numeros = [1, 2, 3, 4, 5]
numeros_dobrados = []
for numero in numeros:
    numero_dobrado = numero * 2
    numeros_dobrados.append(numero_dobrado)
print(numeros_dobrados)

# List Comprehension
print([numero * 2 for numero in [1, 2, 3, 4, 5]])

# Outros Exemplos
# Usando bitt in
nome = 'Dacio Lima'
print([letra.upper() for letra in nome])

# Usando função customizada
def caixa_alta(nome):
    nome = nome.replace(nome[0], nome[0].upper())
    return nome
amigos = ['maria','joao','marcos', 'wal', 'samuel', 'assis']
print([caixa_alta(nome) for nome in amigos])

# Retornando Booleanos
print([bool(valor) for valor in [0, [], '', True, 1, 3, 14]])

# Retornando string
print([str(alg) for alg in [1, 2, 3, 4, 5, 6]])

# ESTRUTURAS CONDICIONAIS
# Exemplo 1
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
pares = [numero for numero in numeros if numero % 2 == 0]
impares = [numero for numero in numeros if numero % 2 != 0]
print(pares)
print(impares)

# Refatorando
# Qualquer número par módulo de 2 é 0 e 0 em python é False. not False = True
print([numero for numero in numeros if not numero % 2])

# Qualquer número impar módulo de 2 é 1 e 1 em python é True
print([numero for numero in numeros if numero % 2])

# Exemplo 2
res = [numero * 2 if numero % 2 == 0 else numero / 2 for numero in numeros]
print(res)



