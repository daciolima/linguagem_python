"""
Preservando Metadatas com wraps

Metadatas = São dados intrísecos em arquivos.
wraps = São funções que envolve elementos com diversas finalidades.

"""
# Importando o pacote para correção de proteção dos metadados
from functools import wraps

def ver_log(funcao):
    # Corrigindo problema especificado no final com a anotação @wraps()
    @wraps(funcao)
    def logar(*args, **kwargs):
        """Eu sou uma função (logar) dentro de outra."""
        print(f'Você está chamando {funcao.__name__}')
        print(f'Aqui a documentação: {funcao.__doc__}')
        return funcao(*args, **kwargs)
    return logar

@ver_log
def soma(a, b):
    """Soma dois números"""
    return a + b

# Testando
print(soma.__name__) # É esperado o retorno do nome da função porém o nome vem do decorators(Precisa correção usando a notação @wraps(<NomeDaFuncao>))
print(soma.__doc__) # É esperado o retorno do texto, porém a documentação vem do decorators(Precisa correção usando a notação @wraps(<NomeDaFuncao>))
