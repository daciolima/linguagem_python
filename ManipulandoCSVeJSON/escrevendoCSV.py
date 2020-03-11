"""
Escrevendo em arquivos CSV

reader(leitor) - writer(escritor)

"""

# writer() -> Gera um objeto para possamos escrever em um arquivo CSV.
# Utilizamos o método writerow() para escrever cada linha. Este método recebe uma lista.
from csv import writer

with open('filme.csv', 'w', encoding='UTF8') as arquivo:  # 'w' subscreve o conteudo, 'a' append dados
    escritor_csv = writer(arquivo)
    filme = None
    escritor_csv.writerow(['Título', 'Gênero', 'Duração'])
    while filme != 'sair':
        filme = input('Informe um nome de um filme: ')
        if filme != 'sair':
            genero = input('Informe o gênero: ')
            duracao = input('Informe a duração: ')
            # No writer() é inserido com uma lista
            escritor_csv.writerow([filme, genero, duracao])


# DictWriter
# Utilizamos o método writerow() para escrever cada linha. Este método recebe uma lista.
from csv import DictWriter
with open('filme2.csv', 'w', encoding='UTF8') as arquivo:  # 'w' subscreve o conteudo, 'a' append dados
    cabecalho = ['Título', 'Gênero', 'Duração']
    escritor_csv = DictWriter(arquivo, fieldnames=cabecalho)
    escritor_csv.writeheader()
    filme = None
    while filme != 'sair':
        filme = input('Informe um nome de um filme: ')
        if filme != 'sair':
            genero = input('Informe o gênero: ')
            duracao = input('Informe a duração: ')
            # DictWriter é inserido como dicionário.
            escritor_csv.writerow({"Título": filme, "Gênero": genero, "Duração": duracao})


