"""
    Loop while

while expressao_booleana
    // Execução do loop

O bloco do while será repetida enquanto a expressão booleana for verdadeira ou falsa

"""

# Exemplo
numero = 1
while numero < 10:
    print(numero)
    numero += 1

resposta = ''
while resposta != 'sim':
    resposta = input('Já acabou Dácio? \n')