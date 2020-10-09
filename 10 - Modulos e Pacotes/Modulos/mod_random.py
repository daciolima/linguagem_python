"""

Módlo random e o que são módulos
- Módulos são arquivos que podem ser importados para uso.

- Módulo Rando possui várias funções de números pseudo-aleatório(aleatório onde pode haver repetição)



# Forma 1 para utilizar o módulo
# import de módulo completo(não recomendado)


import random
# a função random() -> Gera número real pseudo-aleatorio entre 0 e 1
print(random.random())


# Forma 2 para utilizar módulos
# import de módulo uma função específica
from random import random #(Forma recomendada)
for i in range(10):
    print(random())


# Gerando numeros reais pseudo-aleatorio entre os valores estabelecidos
from random import uniform
for i in range(10):
    print(uniform(3, 7)) # uniform() gerando número entre 3 e 6


# Gerando valores inteiros pseudo aleatório entre os valores estabelecidos
# Gerando números inteiros
# Gerando números da mega sena
from random import randint
for i in range(6):
    print(randint(1, 61), end=', ')


# choice() ->  Função que mostra um valor aleatório entre um interável
from random import choice
jogadas = ['Pedra', 'Papel', 'Tesoura']
print(choice(jogadas))

texto = 'Dácio Lima'
print(choice(texto))
"""

# Função shuffle() -> tem a função de embaralhar dados
from random import shuffle
cartas = ['K', 'Q', 'J', 'A', '2', '3', '5', '7']
print(cartas)
shuffle(cartas)
print(cartas)







