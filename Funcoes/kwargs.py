"""
**kwargs

Poderiamos chamar este parâmetro por **qualquer nome, porém por convenção foi adotado o **kwargs.

Este é só  mais um parâmetro, mas diferente dos *args que coloca os valores extras em uma tupla, o
**kwargs exige que utilizemos parâmetros nomeados, e transforma eses parâmetros extras em um dicionário
"""

# Exemplo 1
def cores(**kwargs):
    print(kwargs)

cores(marcos='Verde', dacio='verde', wal='roxo')

# Exemplo 2
def cores_favoridas(**kwargs):
    for pessoa, cor in kwargs.items():
        print(f'A cor favorita de {pessoa.title()} é {cor}')

cores_favoridas(marcos='amarelo', dacio='verde', wal='roxo')


# Exemplo 2
def cumprimento_especial(**kwargs):
    if 'dacio' in kwargs and kwargs['dacio'] == 'Python':
        return f'Você recebeu um cumprimento Pythonico!'
    elif 'dacio' in kwargs:
        return f"{kwargs['dacio']} rapaz"
    return 'Nâo tenho certeza quem você é!'

print(cumprimento_especial())
print(cumprimento_especial(dacio='Python'))
print(cumprimento_especial(dacio='Oi'))
print(cumprimento_especial(dacio='Especial'))

""" Nas funções se for usar todos os tipos de parâmetros podemos ter (NESTA ORDEM):
    -   Parâmetros obrigatórios;
    -   *args;
    -   Parâmetros default(Não obrigatórios)
    -   **kwargs
"""

# Exemplo de sequenciade parâmetros acima mencionados
def minha_funcao(idade, nome, *args, solteiro=False, **kwargs):
    print(f'{nome} tem {idade} anos')
    print(args)
    if solteiro:
        return print('Solteiro')
    else:
        print('Casado')
    print(kwargs)


minha_funcao(8, 'Julia')
minha_funcao(39, 'Dacio', 4, 5, 6, solteiro=True)
minha_funcao(20, 'Marcos', eu='não', voce='Vai')
minha_funcao(8, 'Carla', 9, 4, 3, java=False, python=True)

# Desenpacotando no kwargs
def mostra_nome(**kwargs):
    return f"{kwargs['nome']} {kwargs['sobrenome']}"

nomes = {'nome':'Dácio', 'sobrenome':'Lima'}
print(mostra_nome(**nomes))


def soma_multiplos_numeros(a, b, c, **kwargs):
    print(a + b + c)
    print(kwargs)

lista = [1, 2, 3]
tupla = (1, 2, 3)
set = {1, 2, 3}
# OBS: Os nomes da chave em um dicionário devem ser o mesmo dos parâmetos da função
dicionario = dict(a=1, b=2, c=3)
dicionario2 = dict(a=1, b=2, c=3, d=4)

soma_multiplos_numeros(*lista)
soma_multiplos_numeros(*tupla)
soma_multiplos_numeros(*set)
soma_multiplos_numeros(*dicionario)
soma_multiplos_numeros(**dicionario)
soma_multiplos_numeros(**dicionario2, linguagem='Python')




