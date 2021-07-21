"""
Type Hinting = Especificar dicas de tipo de retorno.
Qualquer valor em uma variável str entra como True, salvo se está tiver valor None
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
