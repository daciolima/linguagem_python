"""
Sistema de Arquivo e Navegação

Para fazer uso de manipulação de arquivos de sistema operacional, precisamos importar e fazer uso do módulo OS;

OS -> Operating System - Sistema Operacional

"""

# Fazer o import
import os

# getcwd() -> Pega o current work directory - diretorio de trabalho corrente
# Retorna o path(caminho) absoluto
print(os.getcwd())

# Mudando para um diretório, podemos utilizar o chdir()
os.chdir('..')

# Exibindo o atual caminho
print(os.getcwd())

# Identificando o OS
print(os.name)  # posix(Mac ou Linux), nt(Windows)

# Mais detalhes
import sys
print(sys.platform)   # win32 -> Windows

# Checando se diretorio é absoluto ou relativo
# Retorna True se for absoluto, caso contrário o caminho é relativo
# WINDOWS
print(os.path.join(os.getcwd(), 'C:\\Users\\hepta.dacio.l\\Documents\\PROJETOS\\Python\\Exercicios\\LeituraEscritaArquivos'))

# Acrescentando diretorio
res = os.path.join(os.getcwd(), 'LeituraEscritaArquivos')

os.chdir(res) # Aplica a mudança
print(os.getcwd())

# Listando diretórios
print(os.listdir())
print(len(os.listdir()))

# Listando diretório de forma mais detalhada
print(list(os.scandir('C:\\Users\\hepta.dacio.l\\Documents\\PROJETOS\\Python\\Exercicios\\LeituraEscritaArquivos')))
arquivo = list(os.scandir('C:\\Users\\hepta.dacio.l\\Documents\\PROJETOS\\Python\\Exercicios\\LeituraEscritaArquivos'))
arquivo0 = os.scandir()
print(dir(arquivo[0]))
print(arquivo[0].inode()) # Retorna uma identificação do arquivo(Node)
print(arquivo[0].is_dir()) # É um diretório? False
print(arquivo[0].is_file()) # É um arquivo? True
print(arquivo[0].is_symlink()) # É um luink simbólico? True
print(arquivo[0].name) # Nome do arquivo
print(arquivo[0].path) # Caminho até o arquivo
print(arquivo[0].stat()) # Retorna dados sobre o arquivo, entre eles o tamanho do arquivo

# Quando usamos a função scadir() nós precisamos fechá-la, assim quando abrimos um arquivo

arquivo0.close()
