"""
Debugando com PDB

Podemos utilizar o python debugger em diferentes IDE usando python

A partir do python  3.7, não é mais necessário importar a biblioteca a bilbioteca pdb no início do arquivo
basta colocar na linha onde queremos iniciar o debugger a função breakpoint()
Não colocar nome das variáveis iguais aos atalhas pra evitar conflito de comando


Atalhos:
l -> retorna onde estamos no código
n -> próxima linha
p -> imprime variável
c -> continua a execução - finaliza execução
"""
# Exemplo de debugger
# Necessário importar a lib pdb

nome = 'Dácio'
sobrenome = 'Lima'
breakpoint()
nome_completo = nome + ' ' + sobrenome
curso = 'Programação em Python: Essencial'
final = nome_completo + ' faz curso '+ curso
print(final)
