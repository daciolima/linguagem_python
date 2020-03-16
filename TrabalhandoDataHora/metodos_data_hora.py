"""
Métodos de Data e Hora

"""

import datetime

# Com o now() podemos especificar o Timezone (Fuso Horário) onde no today() não temos como fazer isso.
agora = datetime.datetime.now()
print(agora)
print(type(agora))
print(repr(agora))


hoje = datetime.datetime.today()
print(hoje)
print(type(hoje))
print(repr(hoje))

print()
print('################### MÉTODO COMBINE() ######################')
# Mudança ocorrendo à meia-noite combine() # O Combine -> Combina o resultado o delta com o ultimo parametro, nesse
# caso o datetime.time() onde retorna 0 na h:m:s.
manutacao = datetime.datetime.combine((datetime.datetime.now() + datetime.timedelta(days=1)), datetime.time())

print(manutacao)
print(type(manutacao))
print(repr(manutacao))


print()
print('################### MÉTODO WEEKDAY() ######################')
# O método weekday retorna o dia da semana onde 0 é segunda-feira.
print(manutacao.weekday())


print()
print('################### SABER O DIA DA SEMANA QUE VOCÊ NASCEU ######################')
aniversario = "02/03/2020"
aniversario = aniversario.split('/')
aniversario = datetime.datetime(year=int(aniversario[2]), month=int(aniversario[1]), day=int(aniversario[0]))

if aniversario.weekday() == 0:
    print('Você nasceu em uma segunda-feira!')

print()
print('################### Formatando DATA ######################')
hoje = datetime.datetime.today()
print(hoje)

hoje_formatado = hoje.strftime('%d/%m/%Y')
print(hoje_formatado)


print()
print('################### Função Local Traduzir/Formatar extenso DATA ######################')


def formata_data(data):
    if data.month == 1:
        return f'{data.day} de Janeiro de {data.year}'
    elif data.month == 2:
        return f'{data.day} de Fevereiro de {data.year}'
    elif data.month == 3:
        return f'{data.day} de Março de {data.year}'
    elif data.month == 4:
        return f'{data.day} de Abril de {data.year}'
    elif data.month == 5:
        return f'{data.day} de Maio de {data.year}'
    elif data.month == 6:
        return f'{data.day} de Junho de {data.year}'
    elif data.month == 7:
        return f'{data.day} de Julho de {data.year}'
    elif data.month == 8:
        return f'{data.day} de Agosto de {data.year}'
    elif data.month == 9:
        return f'{data.day} de Setembro de {data.year}'
    elif data.month == 10:
        return f'{data.day} de Outubro de {data.year}'
    elif data.month == 11:
        return f'{data.day} de Novembro de {data.year}'
    elif data.month == 12:
        return f'{data.day} de Dezembro de {data.year}'


hoje = datetime.datetime.today()
print(formata_data(hoje))


print()
print('################### Traduzir/Formatar extenso DATA usando a Lib TextBlob ######################')
# Instalar a lib: pip install textblob
# OBS: Essa lib pega informações online, portanto, ela é lenta devido ao fato de ter que sempre está buscando informações
# online
from textblob import TextBlob


def formata_texto2(data):
    return f"{data.day} de {TextBlob(data.strftime('%B')).translate(to='pt-br')} de {data.year} "


hoje = datetime.datetime.today()
print(formata_texto2(hoje))


print()
print('################### Formatando DATA usando o método strptime ######################')
nascimento = '20/01/1980'
nascimento = datetime.datetime.strptime(nascimento, '%d/%m/%Y')
print(nascimento)


print()
print('################### Formatando SOMENTE HOJE ######################')
almoco = datetime.time(12, 30, 0)
print(almoco)  #  12:30:00


print()
print('################### Marcando tempo de execução de uma interação com método timeit() ######################')
# Deve-se haver a importação da lib timeit
import timeit

# Loop for
tempo = timeit.timeit('"-".join(str(n) for n in range(100))', number=10000)
print(tempo)

# List Comphension
tempo = timeit.timeit('"-".join(str(n) for n in range(100))', number=10000)
print(tempo)

# Map
tempo = timeit.timeit('"-".join(map(str, range(100)))', number=10000)
print(tempo)


print()
print('################### Marcando tempo de execução de uma função com método timeit() ######################')
# Para marcar tempo de execução de funções importaremos a lib: functools
import functools


def funcao_teste(n):
    soma = 0
    for num in range(n * 200):
        soma = soma + num ** num + 4
    return soma


# A função function.partial(função a ser testada, parâmetro da função a ser testada )
print(f' Função funcao_teste() levou: {timeit.timeit(functools.partial(funcao_teste, 2), number=10000)} '
      f'segundos para concluir.')





