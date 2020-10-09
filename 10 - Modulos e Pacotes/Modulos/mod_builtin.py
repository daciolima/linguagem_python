"""
Trabalhando com módulos Builtin(Módulos integrados, que já vem instalados no Python)

QUando estalamos o Python algunas fnções são ativas e prontas para uso, porém a
Grande maioria das funções Built-In não são carregadas, precisam sem importadas, isso acontece
para não sobrecarregar a memória


# Utilizando apelidos para importes de funções
# Exemplo 1
import random as rdm
print(rdm.random())

# Exemplo 2
from random import randint as rdi
print(rdi.random(5, 89))

# Exemplo 3
from random import randint as rdi, random as rdm
print(rdi.random(5, 89))


"""
# Importando tudo - Forma 1
from random import *
print(random())

# Importando tudo - Forma 1
import random
print(random.random())

# Realizando vários import
from random import (
    random,
    randint,
    shuffle,
    choice
)

print(random())










