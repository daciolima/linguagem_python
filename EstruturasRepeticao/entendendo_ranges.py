"""
Ranges

    -   Precisamos conhecer melhor o loop for para usar o ranges
    -   Precisamos conhecer o range para trabalhar melhor com loops for

Ranges são utilizados para gerar sequencias numéricas, não
"""

# Forma 1 - Inicio não especificado, padrão 0.
for num in range(11):
    print(num)

# Forma 2 - Inicio especificado pelo usuário
for num in range(0, 11):
    print(num)

# Forma 3 - Valor de inicio, valor final, e o salto a cada laço
for num in range(0, 10, 2):
    print(num)

# Forma 4 - Inversa - Valor de inicio(final), valor final(Início), e o salto a cada laço - Decrementando
for num in range(10, 0, -1):
    print(num)