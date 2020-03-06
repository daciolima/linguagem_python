"""
Mapas => Conhecidos em python como Dicionários

Dicionários em python são representados por chaves {}
"""

receita = {'jan': 100, 'fev': 230, 'mar': 300}

# Interar sobre dicionários
# for chave in receita:
#     print(chave)
#
# for chave in receita:
#     print(receita[chave])
#
# for chave in receita:
#     print(f'{chave} : {receita[chave]}')


# Acessando as chaves
print(receita.keys())
for chave in receita.keys():
    print(chave)

# Acessando os valores
print(receita.values())
for chave in receita.values():
    print(chave)

# Desempacotamento de dicionários
print(receita.items())
for chave, valor in receita.items():
    print(f'Chave={chave} e Valor={valor}')

# Soma, Valor Maximo, Valor Mínimo, Tamanho
# Obs: Só podemos obter retorno se os valores forem inteiros ou reais
print(sum(receita.values()))
print(max(receita.values()))
print(min(receita.values()))
print(len(receita))
