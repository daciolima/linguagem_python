"""
Manipulando Data e Hora

Python tem um módulo built-in(integrado) para se trabalhar com data e hora
chamado de datetime

"""

import datetime


print(datetime.MAXYEAR)
print(datetime.MINYEAR)

# Retorna data e hora corrente
print(datetime.datetime.now())

# Retornar a representação do datetime
print(repr(datetime.datetime.now()))

# replace() para fazer ajustes na data/hora
inicio = datetime.datetime.now()
print(inicio)
# Alterando o horário para 16 horas, 0 minuto, 0 segundo, 0 microsegundo
inicio = inicio.replace(year=2023, hour=16, minute=0, second=0, microsecond=0)

print(inicio)

print()


print('################################################################')

evento2 = datetime.datetime(2019, 1, 1, 0)
print(type(evento2))
print(evento2)

nascimento = input('Informe sua data de nascimento ( dd/mm/yyyy): ')
nascimento = nascimento.split('/')
nascimento = datetime.datetime(int(nascimento[2]), int(nascimento[1]), int(nascimento[0]))
print(nascimento)
print(type(nascimento))

print()
print('################################################################')

# Acessando individualmente partes da data e hora
evento = datetime.datetime.now()

print(evento.year)  # Só o ano
print(evento.month)  # Só o mês
print(evento.day)  # Só o dia
print(evento.minute)  # Só o minuto
print(evento.second)  # Só o segundo
print(evento.microsecond)  # Só o milésimo segundo

print(dir(evento))
