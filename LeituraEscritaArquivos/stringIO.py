"""
String IO

Atenção: Para ler ou escrever dados em arquivo de sistema operacional o software precisa ter permissão:
    - Permissão para ler o arquivo;
    - Permissão para escrever no arquivo.

StringIO -> Utilizado para ler e criar arquivo em memória
"""

# Primeiro fazemos o import
from io import StringIO
mensagem = 'Este é apenas uma string normal'

# Podemos criar um arquivo em memória já com uma string inserida ou mesmo vazio para inserirmos texto depois
arquivo = StringIO(mensagem)

# Agora qe temos o arquivo, podemos utilizar tudo o que já sabemos
print(arquivo.read())

# Escrevendo outros textos
arquivo.write('Outro texto')

# Podemos inclusive movimentar o cursor
arquivo.seek(0)

print(arquivo.read())
