












































"""
Módulos externos
Utilizamos o gerenciados de pacotes Python cjhamado Pip(Python Installer Package).
Você pode conhecer todos os pacotes externos oficiais em http://pypi.org

Ex:
módulo colorama -> É utilizado para permitir impressão de textos coloridos no terminal.

Instalando módulo

pip install colorama

from colorama import init, Fore

init()

print(Fore.MAGENTA + 'Dácio Lima')
print(Fore.GREEN + 'Dácio Lima')


"""
import pydf

pdf = pydf.generate_pdf("<h1>Dácio Lima</h1><br/><br/><strong>Programaçao</strong>")

with open('test_doc.pdf', 'wb') as f:
    f.write(pdf)






















