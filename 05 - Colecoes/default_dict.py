"""
Modulo Collections - Default Dict
https://docs.python.org/3.7/library/collections.html#defaultdict-objects

Default Dict => Ao criar um dicionário utilizando-o, nós informamos um valor default,
podemos usar um lambda para isso. Este valor serpa utilizado sempre que não houver um valor definido.
Caso tentemos acessar uma chave que não existe, essa chave será criada e o valor default será atribuído.


dicionario = {'aluno': 'Sou desenvolvedor de sistemas'}
print(dicionario)
print(dicionario['aluno'])

"""

# Exemplo do Default Dict
from collections import defaultdict

variavel = defaultdict(lambda: 0)
variavel['nome'] = 'Dácio Lima'
print(variavel)

print(variavel['sobrenome']) # No dicionário do tipo defaultdict não existe erro no retorno caso não encontra a chave

