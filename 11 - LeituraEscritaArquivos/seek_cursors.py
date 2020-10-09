"""
Seek e Cursors

seek() -> É utilizada para movimentar o cursor pelo arquivos

"""

arquivo = open('file.txt', encoding='utf-8')
print(arquivo)
print(arquivo.read())


# SEEK()
# Movimento do cursor pelo arquivo com a função seek()
# A função seek() é utilizada para movimentação do cursor pelo arquivos.
# Ela recebe um parâmetro que indica onde queremos colocar o cursor.
arquivo.seek(0)
print(arquivo.read())
arquivo.seek(15)
print(arquivo.read())

# READ()
# read() -> ler conteúdo inteiro

# READLINE()
# readline() -> ler linha por linha
arquivo2 = open('file.txt', encoding='utf-8')
retorno = arquivo2.readline()
print(type(retorno))
print(retorno)
print(retorno.split(' '))

# READLINES
# readlines() Ler todas as linhas e transformandoas em elementos de uma lista
arquivo3 = open('file.txt', encoding='utf-8')
retorno3 = arquivo3.readlines()
print(type(retorno3))
print(retorno3)
print(len(retorno3))
print(retorno.split(' '))


# OBS: Abrimos um arquivo com a função open() é criada uma coneção entre o arquivo no disco do computador e o nosso programa
# Essa conexão é chamada de streaming. Ao finalizar o arquivo devemos fechar essa conexção e para isso usamos a função close()
# Passos para trabalhar com um arquivo
# 1 - Abrir arquivo
arquivo4 = open('file.txt', encoding='utf-8')
# 2 - Trabalhar no arquivos
print(arquivo4.read())
# 3 - Fechar o arquivo
arquivo4.close()

# Verificando se arquivo está aberto  ou não. Após arquivo fechado para ter acesso deve-se abrir novamente
print(arquivo4.closed)



