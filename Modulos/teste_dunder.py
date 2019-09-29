
def funcao():
    return 'arquivo sendo executado diretamente'


if __name__ == '__main__':

    funcao()
    print('arquivo sendo executado diretamente')
    print(f'Nome do arquivo internamente é esse: {__name__}')
else:
    print('Arquivo sendo executado por uma importação')
    print(f'Nome do arquivo internamente é esse: {__name__}')

