"""
Assertions ( Afirmações/Checagens/Questionamentos)

Em Python utilizamos a palavra reservada 'assert' para realizar simples
afirmações utilizadas nos testes.

Utilizamos o 'assert' em uma expressão que queremos chegar se é válida ou não.
Se a expressão for verdadeira, retorna None e caso seja falsa levanta um erro
do tipo AssertionError.

# OBS: Nós podemos especificar, opcionalmente, um segundo argumento ou mesmo uma
mensagem de erro personalizada.

# OBS: A palavra 'assert' pode ser utilizada em qualquer função ou código nosso...
não precisa ser exclusivamente nos testes.

# ATENÇÃO: Se usado a flag -o na execução do arquivo com testes usando assert o mesmo
é desabilitado. Ex. # python -O TesteAssertions.py

"""


def soma_de_positivos(a, b):
    assert a > 0 and b > 0, 'Ambos números precisão ser positivos!'
    return a + b


ret = soma_de_positivos(2, 3) # 6
# ret = soma_de_positivos(-2, 3) # AssertionError
print(ret)


def comer_fast_food(comida):
    assert comida in [
        'Pizza',
        'Pão',
        'Coxinha',
        'Carne',
        'Macarrão'
    ], 'Comida precisa está no cardápio'
    return f'Eu estou comendo {comida}'


ret2 = comer_fast_food('Pizza')
print(ret2)