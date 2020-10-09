"""
    Recebendo dados de usuário
"""

# Entrada de dados através do builtins input()
#print('Qual o seu nome?')
#nome = input()
nome = input('Qual o seu nome? \n')

# Saída de dados com somente uma variável não precisa parenteses, ex: print basea-se no python 2.0
# print('Seja bem vindo(a) %s' % nome)

# Saida de dados em python 3.7
#print('Seja Bem-vindo {0}'.format(nome))
print(f'Seja bem-vindo {nome}')

#print('Qual a sua idade: ')
#idade = input()
idade = input('Qual a sua idade? \n')


# Saída de dados com duas ou mais variáveis precisa de parenteses,  ex: print basea-se no python 2.0
#print('O %s tem %s ' % (nome, idade))

# Saida de dados em python 3.7
#print('O {0} tem {1}'.format(nome, idade))
print(f'O {nome} tem {idade}')

# Cast é a conversão de um tipo de dado para outro, estamos usando um cast int
print(f'O {nome} nasceu {2019 - int(idade)}')



