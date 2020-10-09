"""
Módulo -> É apenas um arquivo python que pode ter diversas funções para utilizarmos;

Pacote -> É um diretório contendo uma coleção de módulos

OBS: Nas versões python 2.x um pacote Python era necessário ter dentro dele um arquivo com nome __init__
Nas versões 3.x não há mais a necessidade, porém é usado por motivo de compatibilidade

"""

# Importando modulo de dentro de pacote
from Pacote import arq1, arq2

print(arq1.pi)
print(arq1.funcao1(4, 6))

print(arq2.curso)
print(arq2.funcao2())


# Importando módulo de dentro de subpacote
from Pacote.subpacote import arq3

print(arq3.funcao3())


# Importando uma funcao especifica de dentro de um submodulo
# Importando módulo de dentro de subpacote
from Pacote.subpacote.arq4 import funcao4

print(funcao4())