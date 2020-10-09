"""
Forçando tipos de dados com decoradores.

No Python as variáveis assumem o tipo de acordo com o tipo do conteúdo inserido, mas podemos forçar receber somente
um determinado tipo.

zip
a = (1, 3, 5)
b = (2, 4, 6)
c = zip(a, b)

Resultado: (1, 2), (3, 4), (5, 6)

"""

def forca_tipo(*tipos):
    def decorador(funcao):
        def converter(*args, **kwargs):
            novo_args = []
            for(valor, tipo) in zip(args, tipos):
                novo_args.append(tipo(valor))  # str('Geek'), int(3)
            return funcao(*novo_args, **kwargs)
        return converter
    return decorador

@forca_tipo(str, int)
def repete_tipo(msg, vezes):
    for vez in range(vezes):
        print(msg)

# Testando
repete_tipo('Geek', 3)


@forca_tipo(float, float)
def dividir(a, b):
    print(a / b)

# Testando
dividir('4', 2)