""""
Estruras lógicas: and, or, not e is

Operadores unários: Precisa apenas de um elemento para retornar
    -   not
Operadores binários: Precisa de dois elementos para comparar
    - and, or, is

# OR (ou)
True or True = True
True or False = True
False or True = True
False or False = False

# AND (e)
True and True = True
True and False = False
False and True = False
False and False = True

# NOT (Negação)

# IS (é)
Usado para comparar o estado do elemento e retorna booleano
"""

ativo = True
logado = False

if ativo and logado:
    print('bem-vindo usuário')
else:
    print('Você precisa realizar login.')

if not ativo:
    print('Você precisa realizar login.')
else:
    print('bem-vindo usuário')


# Ativo ou falso
print(ativo is False)


