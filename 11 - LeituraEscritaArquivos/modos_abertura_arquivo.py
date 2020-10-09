"""
Modos de abertura de arquivo

r - Abre para leitura - padrão
w - Abre para escrita - sobrescreve caso o arquivo exista
x - Abre para escrita somente se o arquivo não existir, caso exista
a - Abre para escrita, adicionando sempre no fim do arquivo caso exista.
+ - Abre para modo de atualização, leitura e escrita. (Temos o controle do cursor par atualização)

"""
# Modo usando x
try:
    with open('file3.txt', 'x') as arquivo:
        arquivo.write('Teste de escrita')
except FileExistsError:
    print('Arquivo já existe!')


# Modo usando a
with open('fruta.txt', 'a') as arquivo:
    while True:
        fruta = input('Informe um nome de fruta: ')
        if fruta != 'sair':
            arquivo.write(fruta)
            arquivo.write('\n')
        else:
            break

with open('file.txt', '+a') as arquivos_file:
    arquivos_file.write('testando 1, 2, 3')


