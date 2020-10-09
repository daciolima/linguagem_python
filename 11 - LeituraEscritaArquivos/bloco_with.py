"""
O Bloco with

Passos para se trabalhar com arquivos
1 - Abrimos o arquivo
2 - Manipulamos o arquivo
3 - Fechamos o arquivo

O bloco with é utilizado para criar um contexto de trabalho onde os recursos
utilizados são fechados após o bloco with.

"""
# O bloco with
with open('file.txt') as arquivo:
    print(arquivo.readlines())
    