"""
Annotation são as informações que colocamos referente ao tipo de variável e que pode ser visto
através da builtin .__annotation__
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

print(cumprimentar.__annotations__)
print(cabecalho.__annotations__)
