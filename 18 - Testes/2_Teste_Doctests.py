"""
Doctests

Para executar no console use o comando: python -m doctest -v arquivo.py

# OBS: A escrita abaixo relacionada ao TypeError deve ser exatamente igual a saída do console
# OBS: As duplas dentro de asplas triplas são reconhecidas como simples, dependendo do teste
retornará erro.
# No Docteste escrito nas asplas triplas os espaços são considerados, portanto, deve ser observado.
"""


def soma(a, b):
    """ Soma os números a e b

    >>> soma(1, 2)
    3
    """
    return a + b



# Outro exemplo aplicando TDD
def duplicar(valores):
    """ Duplicando lista

    >>> duplicar([1, 2, 3, 4])
    [2, 4, 6, 8]
    >>> duplicar([])
    []
    >>> duplicar([True, None])
    Traceback (most recent call last):
        ...
    TypeError: unsupported operand type(s) for *: 'int' and 'NoneType'
    """
    return [2 * elemento for elemento in valores]


if __name__ == "__main__":
    import doctest
    doctest.testmod(soma(1, 3))
    doctest.testmod(duplicar([True, None]))

