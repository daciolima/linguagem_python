"""
lendo arquivos CSV

CSV - Comma Separeted Values - Valores Separados por vírgula

# Separador por vírgula
1, 2, 3, 4, 5, 6
"profissional", "TI", "informática", "ciência", "dados"

# Separador por ponto e vírgula
1; 2; 3; 4; 5; 6
"profissional"; "TI"; "informática"; "ciência"; "dados"

# Separador por espaço
1 2 3 4 5 6
"profissional" "TI" "informática" "ciência" "dados"

"""

# Lendo com o Reader do CSV
print()
print('############## Lendo com o Reader do CSV ##############')
from csv import reader

with open('original.csv', encoding='UTF8') as arquivo:
    leitor_csv = reader(arquivo, delimiter=',')  # Padrão para o reader é o delimitador vírgula.
    next(leitor_csv)  # A função next pula uma linha em objetos interáveis, portanto, nesse caso, pula o cabeçalho.
    for linha in leitor_csv:
        print(f'{linha[0]} nasceu no(a) {linha[1]} e mede {linha[2]} centimetros.')



# Lendo com o DictReader do CSV
print()
print('############## Lendo com o DictReader do CSV ##############')
from csv import DictReader
with open('original.csv', encoding='UTF8') as arquivo:
    leitor_csv = DictReader(arquivo, delimiter=',')  # Padrão para o DictReader é o delimitador vírgula.
    for linha in leitor_csv:
        # Cada linha é um OrderedDict
        print(f'{linha["Nome"]} nasceu no(a) {linha["País"]} e mede {linha["Altura (em cm)"]} centimetros.')
