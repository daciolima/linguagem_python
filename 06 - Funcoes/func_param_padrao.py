"""
Funçoes com parâmetro padrão(Default Parameter)
    -   Funções onde a passagem de parâmetro seja opcional.
    -   Valores default DEVEM sempre está no ultimo parâmetro caso seja usado.
    -   É aceito qualquer valor nos parametros padrão.
Motivos para usar parâmetro padrão:
    -   Nos permite ser mais flexível nas funções;
    -   Evita erros com parâmetros incorretos.


"""

# Exemplo 1 - A função print se não por algum argumento ou parâmetro não retorna nada(Não dá erro)
print()

# Exemplo 2 - Na potencia foi colocar um valor padrão e assumirá caso nao seja colocada valores no parâmetro na
# Chamada da função
def exponencial(numero, potencia=2):
    return numero ** potencia

print(exponencial(3))


# Exemplo 2
def mostrar_informacao(nome='Dacio', instrutor=False):
    if nome == 'Dacio' and instrutor:
        print(f'Bem vindo instrutor {nome}')
    elif nome == 'Lima':
        print(f'Pensei que você era o instrutor')
    return f'Olá {nome}'

print(mostrar_informacao())
print(mostrar_informacao(instrutor=True))
print(mostrar_informacao(True))
print(mostrar_informacao('Barros'))
print(mostrar_informacao(nome='Wal'))

# Exemplo 3 - Usando uma outra função como parametro padrão
def soma(num1, num2):
    return num1 + num2

def subtracao(num1, num2):
    return num1 - num2

def mat(num1, num2, fun=soma):
    return fun(num1, num2)

print(mat(2, 2))
print(mat(10, 4, subtracao))

# Escopo de variáveis - Se tiver uma variável local com o mesmo nome de uma global, a variável local tem preferencia
# Variáveis Globais
instrutor = 'Dacio'

# Variáveis locais
def professor():
    instrutor = 'Python'
    return f'Oi {instrutor}'

print(professor())


# Utilização de uma variável global
total = 0  # Variável global

def incremento():
    global total  # Chama variável Global
    total = total + 1
    return total

print(incremento())


# Usando função dentro de função tratando escopo de variáveis
def fora():
    contador = 0
    def dentro():
        nonlocal contador # Informa que não é local e que tabém não e global, mas de uma função logo acima

        contador = contador + 1
        return contador
    return dentro()

print(fora())
