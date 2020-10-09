"""
Escopo de variáveis

Dois casos de escopo:
1 - Variáveis globais: São reconhecidas em todo o programa.
2 - Variável local: São reconhecidas apenas no bloco onde foram declaradas

nome_da_variavel = valor_da_variavel

Python é uma liguagem de tipagem dinâmica. Isso significa que o tipo de variavel é inferido no momento que o valor dela for atribuído
"""

# Exemplo variável global(Disponível em todo o arquivo(Programa))
numero = 40
print(numero)

# Exemplo de variável local(Disponível apenas no bloco)
if numero > 10:
    novo = numero + 10
    print(novo)






