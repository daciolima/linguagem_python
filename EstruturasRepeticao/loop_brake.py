"""
Saindo do loop com brake

Utilizasse o brake para sair do loop de maneira projetada.

"""

# Exemplo 1
for numero in range(1,11):
    if numero == 6:
        break
    else:
        print(f'Numero é: {numero}')
print('Sair do Loop')

# Exemplo 2
while True:
    comando = input("Digite 'sair' para sair: \n")
    if comando == 'sair':
        break