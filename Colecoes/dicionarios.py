""""

Dicionários

OBS: EM algumas liguagens de programação, os dicionários Python são chamados de mapas

Dicionário são coleções do tipo chave/valor

print(type({}))

OBS: Sobre Dicionários:
    -   Chave e valor são separados por dois pontos;
    -   Tanto chave quando valor pode ser qualquer tipo de dado
    -   Podemos misturar tipos de dados
    -   Dicionário não pode ter chave repetida

"""

# Criando Dicionário
# Forma 1
paises = {'br':'Brasil', 'eua':'Estados Unidos', 'py':'Paraguay'}
print(paises)
print(type(paises))


# Forma 2
paises2 = dict(Es='Espanha', UK='Reino Unido', It='Itália')
print(paises2)
print(type(paises2))

# Forma 3 - Cria dicionario com as chaves nomeadas na lista e atribui a cada uma delas o valor logo após a vírgula, nesse caso desconhecido
dicionario = {}.fromkeys(['nome', 'pontos', 'email', 'profile'], 'desconhecido')
print(dicionario)

# Forma 4 - cria dicionario com cada inteiração na string não repetindo letras.
dicionario = {}.fromkeys('teste', 'valor')
print(dicionario)

# Forma 5 - Criar dicionario com range - Corre de 1 a 10 colocando como valor a palavra Oi.
veja = {}.fromkeys(range(1, 11), 'Oi')
print(veja)

# Acessando Elementos
# Forma 1 - Via Chave
print(paises['br'])
print(paises2['It'])

# Forma 2 - Via get - Recomendado - Caso não encontrado retorna None == elemento sem tipo(Vazio)
print(paises.get('eua'))
print(paises2.get('UK'))

# Usando o get com retorno caso não encontre nada
pais = paises.get('NZ', 'Não foi encontrado o país')
print(pais)

# Forma 3 - in - Procura por chave caso não encontre retorna True ou False
print('br' in paises)
print('ag' in paises2)

# Podemos usar o Nome para colocar o valor em uma variável onde não sabemos ainda que tipo ela vai receber
# Exemplo None
numero = None
print(numero)
print(type(numero))

if numero == None:
    numero = 1
    print(numero)
    print(type(numero))

# Retorno None sempre é False
cafe = None
if cafe:
    print('Café encontrado')
else:
    print('Café não encontrado!')


# Podemos usar qualquer tipo de dado(int, string, boolean, floar), inclusive lista, tupla dicionário como
# chave de dicionário
# Exemplo de chaves com tuplas. Lembrando que tuplas são imutáveis
localidades = {
    (36.4588, 39.7888): 'Escritorio em Tókio',
    (20.4587, 21.7541): 'Escritorio em João Pessoa',
}
print(localidades)
print(type(localidades))

# Adicionando elementos em dicionário
receita_financeiro = {'jan':100, 'fev': 230, 'mar': 300}
print(receita_financeiro)
print(type(receita_financeiro))

# Forma 1 - Mais comum
receita_financeiro['abr'] = 410
print(receita_financeiro)

# Forma 2
novo_dado = {'mai': 210}
receita_financeiro.update(novo_dado)   # receita_financeiro.update({'mai': 210})
print(receita_financeiro)

# Atualizando dados em um dicionário
# Forma 1
receita_financeiro.update({'abr':500})
print(receita_financeiro)

# Removendo elementos
# Forma 1 - Remove o elemento e retorna o mesmo
saida = receita_financeiro.pop('mai')
print(saida)

# Forma 2 - Apenas remove o elemento, caso não encontrado a chave retornar um erro.
del receita_financeiro['abr']
print(receita_financeiro)

"""
Onde usar dicionário:
Imagine um carrinho de compras
Carrinho de compra
    Produto 1:
        -   nome;
        -   quantidade
        -   preco
    Produto 2:
        -   nome;
        -   quantidade
        -   Preco

Carrinho com lista

"""
# Forma com lista
carrinho = []
produto1 = ['Paystation', 1, 2300.00]
produto2 = ['Jogo Star', 1, 350.00]
carrinho.append(produto1)
carrinho.append(produto2)
print(carrinho)

carrinho = [['Paystation', 1, 2300.00], ['Jogo Star', 1, 350.00]]
print(carrinho)

# Forma com Tupla
produto1 = ('Paystation', 1, 2300.00)
produto2 = ('Jogo Star', 1, 350.00)
carrinho = (produto1, produto2)
print(carrinho)

# Forma com dicionário - Dessa forma facilmente adicionamos ou removemos produtos no
# carrinho e em cada produto podemos ter a certeza sobre cada informação
carrinho = []
produto1 = {'nome': 'Playstation', 'quantidade': 1, 'preco': 2300.00}
produto2 = {'nome': 'Game of War', 'quantidade': 1, 'preco': 250.00}

carrinho.append(produto1)
carrinho.append(produto2)
print(carrinho)

# Métodos de dicionários
# Copiando dicionarios
# Modo Deep Copy
d = dict(a=1, b=2, c=3)
novo = d.copy()
print(novo)

novo['d'] = 4
print(d)
print(novo)

# Modo Shallow Copy
novo = d
print(novo)
novo['d'] = 4
print(d)
print(novo)



