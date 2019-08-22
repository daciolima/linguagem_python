"""
Try / Exception / Else / Finally

Dica de quando e onde tratar código

TODA ENTRADA DEVE SER TRATADA

"""

# Tente fazer isso
try:
    num = int(input('Informe um numero: '))

# Se houver erro no try lance isso
except ValueError:
    print('Você não digitou um valor válido')

# Se não houve saída do except é lancado o else
else:
    print(f'Você digitou o número {num}')

# Sempre é lançado havendo ou não erro
# O Finally, geralmente é utilizado para fechar ou desalocar recursos. Ex: conexão de banco
finally:
    print('Executando o finally')


############################################################################################

# OBS: Você é responsável pelas entradas das suas funções. Trate-as!!!
def dividir(a, b):
    try:
        return int(a) + int(b)
    except ValueError:
        print('Valor incorreto!')
    except ZeroDivisionError:
        print('Não é possível realizar uma divisão por zero')

num1 = input('Informe o primeiro número: ')
num2 = input('Informe o segundo número: ')

print(dividir(num1, num2))


##############################################################################################
# Tratamento semi-genérico
# OBS: Você é responsável pelas entradas das suas funções. Trate-as!!!
def dividir(a, b):
    try:
        return int(a) + int(b)
    # Usado tupla para lista em uma except quando ocorrer diferentes erros
    except (ValueError, ZeroDivisionError) as err:
        print(f'Ocorreu um erro {err}!')


num1 = input('Informe o primeiro número: ')
num2 = input('Informe o segundo número: ')

print(dividir(num1, num2))


