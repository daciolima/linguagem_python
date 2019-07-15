"""
Tipo float (real, decimal)

números com casas decimais

Obs: Numeros devem ser separados por ponto e não virgulas

"""

# Errado para float, porém gera uma tupla
valor = 1, 44
print(valor)
print(type(valor))


#Certo
valor = 1.44
print(valor)
print(type(valor))

# É possivel
valor1, valor2 = 1, 44
print(f'Valor {valor1} e {valor2}')
print(type(valor1))
print(type(valor2))

# Numero complexos
numero = 5j
print(type(numero))

# Int perde precisão com relação aos floats
salario = 2.56
salario2 = 3.67
total_float = salario + salario2
print(total_float)
total_int = int(salario) + int(salario2)
print(total_int)

diferenca = total_float - total_int
print('A diferença é de : ', diferenca)
