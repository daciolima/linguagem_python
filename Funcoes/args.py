""""
Entendendo os *args

    -   O *args é um parâmetro como outro qualquer. Isso significa que você
    poderá chamar de qualquer coisa, desde que comece com asterisco. porém a convenção
    adotou padronizar como *args
    -   O parâmetro *args utilizado em uma função, coloca os valores extras informados como
    entrada em uma tupla. Então desde já lembre-se que tuplas são imutáveis.

"""

#Entendendo o *args
# def soma_todos_valores(*args):
#     print(args)
#
# soma_todos_valores()
# soma_todos_valores(2)
# soma_todos_valores(3, 5)
# soma_todos_valores(5, 7, 8)
# soma_todos_valores(5, 3, 8, 9)

# #Entendendo o *args
# def soma_valores(*args):
#     total = 0
#     for numero in args:
#         total = total + numero
#     return total
#
# soma_valores()
# soma_valores(2)
# soma_valores(3, 5)
# soma_valores(5, 7, 8)
# soma_valores(5, 3, 8, 9)

#Entendendo o *args
def simplificando_soma_valores(*args):
    return sum(args)

print(simplificando_soma_valores())
print(simplificando_soma_valores(2))
print(simplificando_soma_valores(9, 5))
print(simplificando_soma_valores(5, 4, 8))
print(simplificando_soma_valores(5, 3, 8, 9))


# OBS: O asterisco serve para que informemos ao Python que estamos
# pasando como argumento uma coleção de dados. Desta forma, ele saberá
# o que precisará antes fazer antes de desempacotar estes dados.
# Exemplo 2
def somar(*args):
    return f'O resultado : {sum(args)}'

numeros = [1, 2, 3, 4, 5, 6, 7, 8]

#print(somar(numeros))
print(somar(*numeros)) # Asterisco informando que parâmetro é uma coleção

