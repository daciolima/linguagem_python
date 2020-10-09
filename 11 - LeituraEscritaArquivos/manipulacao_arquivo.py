"""
Sistema de Arquivos - Manipulação

Mais informações: http://docs.python.org/3/library/os.html?highlight=os#module-os

"""
import os

# Descobrindo se um arquivo existe ou não
print(os.path.exists('file20.txt')) # False
print(os.path.exists('file2.txt')) # True

# Descobrindo se um diretório existe ou não
# Path relativo
print(os.path.exists('diretorio')) # True
print(os.path.exists('diretorio/subdiretorio')) # True
print(os.path.exists('outro')) # False

# Criando arquivo
# Forma 1
open('arquivo.txt', 'w').close()

# Forma 2
open('arquivo1.txt', 'a').close()

# Forma 3
with open('arquivo2.txt', 'w') as arquivoteste:
    pass

# Forma 4
# Se arquivo já existir retornará tela de erro
#os.mknod('arquivo3.txt')

# Se você estiver utilizando no MAC, pode haver erro de PermissionError

# Criando diretorio um a um.
os.mkdir('templates')
# OBS: A função mkdir() cria diretório se este não existir, Caso exista, teremos FileExistsError

# Criando diretório e subdiretóriode uma vez
os.makedirs('dacio/teste')
open('dacio/teste/file.txt', 'w').close()
open('dacio/teste/file2.txt', 'w').close()
open('dacio/teste/file3.txt', 'w').close()
# Ignorando erro caso arquivo já exista
os.makedirs('dacio/teste', exist_ok=True)

# Renomeando diretórios
os.rename('templates', 'templates2')

# Renomeando arquivos
os.rename('dacio/teste/file.txt', 'dacio/teste/file-teste.txt')

# Deletando diretórios e arquivos
# Arquivo
os.remove('dacio/teste/file2.txt')
# Diretorio
os.rmdir('templates2')
# Se o diretorio não existir teremos um FileNotFoundError

# Removendo vários arquivos dentro de um diretório
for arquivo in os.scandir('dacio/teste'):
    print(f'- {arquivo.name}')
    if arquivo.is_file():
        os.remove(arquivo.path)

# Removendo arvore de diretórios vazias
# Atenção. Arquivos uma vez removidos não passam pela lixeira
os.removedirs('dacio/teste')

# Removendo arquivos e enviando para lixeira. Há a necessidade de uma library de terceiros
# Deve-se instalar a library send2trash. # pip install send2trash
# Após instalar a library send2trash arquivo pode ser enviado para lixeira dessa forma:
from send2trash import send2trash
# Deletando aquivo e enviando para lixeira
open('send2trash.txt', 'w').close()
send2trash('send2trash.txt')
# Deletando diretório e enviando para lixeira
os.mkdir('Send2Trash')
send2trash('Send2Trash')

# Trabalhando com diretórios temporários
import tempfile
with tempfile.TemporaryDirectory() as tmp:
    print(f'Criei o diret´orio temporário em {tmp}')
    with open(os.path.join(tmp, 'arquivo_temporário.txt', 'w')) as arquivo:
        arquivo.write('Teste Dácio 1234\n')
    input()
# OBS: Estamos criando um diretório temporário, abrindo o mesmo e dentro dele criando
# um arquivo para escrevermos um texto. No final, usamos um input() só para mantermos
# os arquivos temporários 'vivos' dentro dos blocos with.
# Possivelmente o código acima não irá funcionar se você estiver usando o OS Windows
# O SO trabalha de forma diferente com arquivos temporários.

# Trabalhando com arquivo temporário
# EM arquivo temporário só conseguimos escrever em bits, por isso usamos b na linha 96
with tempfile.TemporaryFile() as tmp:
    tmp.write(b'Dacio Lima\n')
    tmp.seek(0)
    print(tmp.read())
input()












