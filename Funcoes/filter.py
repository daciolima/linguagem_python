"""
Filter

felter() -> Serve para filtrar dados de uma determinada coleção


# Importando biblioteca para dados estatísticos
import statistics

# EXEMPLO 1
# dados coletados de algun sensor
dados = [1.3, 2.7, 0.8, 4.1, 4.3, -0.1]

# Calculando a média utilizando a função mean()
media = statistics.mean(dados)
print(media)

# OBS: Assim como a função map(), a filter() recebe dois parâmetros, sendo: filter(funcao, interável)
# A cada interação o lambda verifica X de forma que se dado for True ele carrega no filter.
res = filter(lambda x: x > media, dados)

# O retorno dos dados é um objeto, desta forma precisa ser listado
print(list(res))

# Assim como na função map() após ser utilizados os dados(print) os dados são apagados da memória.
print(f'Novamente: {list(res)}')


# EXEMPLO 2
paises = ['', 'Argentina', '', 'Brasil', 'Chile', '', 'Colombia', '', 'Equador', '', '', 'Venezuela']
res2 = filter(None, paises)   # None != '', logo o retorno disso é False
print(f'Ex2: {list(res2)}')


# EXEMPLO 3
res3 = filter(lambda x: len(x) > 0, paises)
print(f'Ex3: {list(res3)}')


# EXEMPLO 4
res4 = filter(lambda x: x != '', paises)
print(f'Ex4: {list(res4)}')


# A diferença entre map() e filter é:

map() -> Recebe função e interável e retorna um objeto mapeando a função para cada elemento do interável. No map()
a função retorna valores.

filter() -> Recebe dois paramâmetros, uma função e um interável e retorna um objeto filtrando apenas os elementos do interável
que tiverem retorno True na função. No filter() a função retorna True ou False


"""
# EXEMPLO 5 - Mais complexo
usuarios =[
    {'usename': 'samuel', 'tweets': ['Eu adoro bolos', 'Eu adoro pizzas']},
    {'usename': 'carla', 'tweets': ['Eu amo gato']},
    {'usename': 'jeff', 'tweets': []},
    {'usename': 'bob123', 'tweets': []},
    {'usename': 'doggo', 'tweets': ['Eu gosto de cachorro', 'Vou sair hoje']},
    {'usename': 'gal', 'tweets': []}
]
print(usuarios)

# Exercicio -> Filtrar os usuários que estão inativos no tweet.
inativos = list(filter(lambda u: len(u['tweets']) == 0, usuarios))
print(f'Usuários inativos: {inativos}')


# Refatorando EXEMPLO 5
inativos2 = list(filter(lambda x: not x['tweets'], usuarios))
print(inativos2)


# Combinando filter() e map()
nomes = ['Dacio', 'Lima', 'Waldilandia', 'gal', 'ana']

# Exercicio - > Devemos criar uma lista contendo 'Sua estrutura é: ' + nome, desde que cada nome tenha
# menos de 5 caracteres. No voando abaixo o filtro está sendo executado antes do map.
lista = list(map(lambda nome: f'Sua instrutora é {nome}', filter(lambda nome: len(nome) < 5, nomes)))
print(lista)




