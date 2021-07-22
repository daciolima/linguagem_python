"""
Biblioteca mypy
pip install mypy

Biblioteca mypy serve para verificar conforme anotações type_hinting e retornar erro caso exista
tipos diferentes nas variáveis com relação ao que foi colocado no type hinting.
"""


def cumprimentar(nome: str) -> str:
    return f'Olá! Tudo bem {nome}?'


def cabecalho(texto: str, alinhamento: bool = True) -> str:
    if alinhamento:
        return f'{texto.title()}\n{"-" * len(texto)}'
    else:
        return f' {texto.title()} '.center(50, '#')


print(cumprimentar('Dácio Lima'))
print(cabecalho('Dácio Lima', alinhamento=True))
print(cabecalho('Dácio Lima', alinhamento=False))
