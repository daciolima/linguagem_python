"""
Decorators com diferentes assinaturas

# Para resolver problemas de envio de dois parametros em decorators, utilizamos um padrão chamado Decorators Pattern(**args, **kwargs)

# Assinatura de uma função é representada pelo tipo de seu retorno , nome da função e o parâmetro de entrada.

"""

# Relembrando
def gritar(funcao):
    def aumentar(nome):
        return funcao(nome).upper()
    return aumentar

@gritar
def saudacao(nome):
    return f'Olá, eu sou o/a {nome}!'

def ordenar(principal, acompanhamento):
    return f'Olá, eu gostaria de {principal}, acompanhamento de {acompanhamento}, por favor.'

# testando
print(saudacao('Catarina'))


# Decorators com envio de dois parametros
# Usando Padrão Decorators Pattern(*args, **kwargs) - Estudadas em funções
def gritar_mesmo(funcao):
    def aumentar_mesmo(*args, **kwargs):
        return funcao(*args, **kwargs).upper()
    return aumentar_mesmo

@gritar_mesmo
def comprimento(nome):
    return f'Olá, eu sou o/a {nome}!'

@gritar_mesmo
def solicitar(principal, acompanhamento):
    return f'Olá, eu gostaria de {principal} acompanhamento {acompanhamento}, por favor.'

# Testando
print(comprimento("Joana D'arc'"))
print(solicitar('Picanha', 'Batata Frita'))


@gritar_mesmo
def lol():
    return 'lol'

print(lol())

# OBS: Vale lembrar que podemos utilizar parâmetros nomeados
print(solicitar(acompanhamento='Batata Frita', principal='Picanha'))


# Decorators com argumentos
def verificar_primeiro_argumento(valor):
    def interna(funcao):
        def outra(*args, **kwargs):
            if args and args[0] != valor:
                return f'Valor incorreto! Primeiro argumento precisa ser {valor}.'
            return funcao(*args, **kwargs)
        return outra
    return interna

@verificar_primeiro_argumento('Pizza')
def comida_favorita(*args):
    print(args)

@verificar_primeiro_argumento(10)
def soma_dez(num1, num2):
    return num1 + num2

# Testando
print(soma_dez(10, 12)) # 22

print(comida_favorita('Pizza', 'Churrasco'))