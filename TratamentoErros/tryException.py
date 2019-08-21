"""
O Block try/Exception

Utilizamos o bloco try/exceptio para tratar error que podem ocorrer no nosso código,
previnindo  assim que o programa pare de funcionar e o usuário recebar a mensagem de erro inesperado.

A forma geral mais simples é:

try:
    // Execusão
exception
    // O que deve ser feito em caso de problema


Exemplo 1 - Tratamento genérico
Tratar erro de forma genérica não é a melhor forma de tratamento de erros. O
Ideal é sempre tratar de forma ecpecífica conforme exemplo 2
try:
    len(3)
except:
    print('Deu algum problema')

# Exemplo 2 - Tratamento específico
try:
    len(5)
except TypeError as err:
    print(f'A aplicação gerou o seguinte erro: {err}')


# Podemos efetuar diversos tratamentos de erros de uma vez
try:
    #len(5)
    #dacio()

except NameError as erra:
    print(f'Deu NameError: {erra}')
except TypeError as errb:
    print(f'Deu TypeError: {errb}')
except TypeError as errc:
    print(f'Deu um erro diferente')

"""

def pegavalor(dicionario, chave):

    try:
        return dicionario[chave]
    except KeyError as kerror:
        print(f'Não existe essa chave: {kerror}')

dic = {'nome': 'Dácio'}
print(pegavalor(dic, 'nome1'))



