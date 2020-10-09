"""
Levantando os próprios erros com raise

raise -> Lança exceçôes

Para simplificar, pense no raise como sendo últil para que possamos criar nossas
próprias excesÕes e mensagem de erros.

A forma geral de utulização é:

raise TipoDoErro('Mensagem de Erro')

Obs: Nada após a execução do raise será executado
"""



#Exemplo real
def colore(texto, cor):
    cores = ('verde', 'amarelo', 'azul', 'branco')
    if type(texto) is not str:
        raise TypeError('texto presica ser uma string')
    if type(cor) is not str:
        raise TypeError('Cor precisa ser uma string')
    if cor not in cores:
        raise ValueError(f'A cor precisa ser uma entre: {cores}')
    print(f'O texto {texto} será impresso na cor {cor}')


colore('Dacio', 'vermelho')