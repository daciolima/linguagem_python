"""
Reduce

Obs: A partir do Python3 a função reduce não é mais integrada(Built-in). Agora temos
que importar e utilizar esta função a partir do módulo 'functools'

A função reduce() só deve usar de realmente precisar dela. O mais indicado em 99% dos casos
usa-se o loop for por ser mais legível

Para entender o reduce:
Imagine que você tem uma coleção de dados:
dados = [a1, a2. a3... ]

E você tem uma funcção que recebe dois parâmetros:

def funcao(x, y):
    return x * y

assim como o map() e filter(), a funcao reduce recebe dois parâmetros: a funcao e o interável

reduce(funcao, interavel)

A funcao reduce(), funcioma da seguinte formar:

    Passo 1: res1 = f(a1, a2) # Aplica a funçao nos dois primeiros elementos da colecao e guarda o resultado
    Passo 2: res2 = f(res1, a3) # Aplica a funcao passando o resultado do passo 1 mais o terceiro elemento e isso é repetido
                                  até o final
    .
    .
    .
    Passo n: resn = f(resn, an)

Ou seja, a cada passo ela aplica a funcao passando como primeiro parâmetro o resultado da aplicação anterior.
No final reduce() irá retornar o resultado final.

Alternativamente poderíamos ver a funcao reduce() passando a
funcao(funcao(a1, a2), a3), a4), ...), an)

"""
# Como funciona na prática
# Multiplicando todos os numeros de uma lista
from functools import reduce

dados = [2, 3, 4, 5, 7, 11, 13, 17, 19, 23, 29]
multi = lambda x, y: x * y
res = reduce(multi, dados)
print(res)

# Utilizando o loop for ao invés do reduce
res2 = 1
for n in dados:
    res2 = res2 * n
print(res2)

