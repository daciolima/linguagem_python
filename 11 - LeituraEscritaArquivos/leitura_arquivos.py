"""
Leitura de Arquivos

Para o conteúdo de um arquivo em Python, utilizamos a função integrada open(),
que literalmente significa abrir.

open() -> Na forma mais simples de utilização nós passamos apenas um parâmetro de entrada,
que neste caso é o caminho para o arquivo a ser lido. Essa função retorna um _io.TextIOWrapper e é com ele que trabalhamos então.

# OBS: Por padrão, a função open() abre o arquivo para leitura. Este arquivo deve existir, ou então teremos um erro FileNotFoundError

Objeto: <_io.TextIOWrapper name='file.txt' mode='r' encoding='cp1252'>

name:  Nome do objeto
mode: 'r'  -> Modo de leitura
encoding: 
"""

arquivo = open('file.txt', encoding='utf-8')

print(arquivo)

print(type(arquivo))

# Primeira vez
# Função read() - Ler o conteudo inteiro de arquivo
arquivo_lido = arquivo.read()
print(type(arquivo_lido))
print(arquivo_lido)
lista_arquivo = arquivo_lido.split('\n')
print(lista_arquivo)

# Limitando o read a leitura dos 50 primeiros caracteres
arquivo2 = open('file.txt', encoding='utf-8')
arquivo_lido2 = arquivo2.read(13)
print(arquivo_lido2)

# Obs: O python, utiliza um recurso para trabalhar com arquivos chamado cursor. Esse cursor
# funciona como o cursor quando estamos escrevendo.





