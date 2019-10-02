"""
Len, Abs, Sum Round

len() -> Retorna o número de itens de um interável
abs() ->
sum() ->
round() ->
"""
# Exemplo - len():
print(len('Dacio Lima'))
print(len([1, 2, 3, 4, 5]))

# Por debaixo dos panos, quando utilizamos a função len() o python faz o seguinte:
# Dunder len
print('Dacio'.__len__())

# Exemplo abs() # Retorna o valor absoluto de um número inteiro ou real. De forma básica,
# seria o seu valor real sem o sinal.
print(abs(.5))
print(abs(5))
print(abs(3.14))
print(abs(-3.14))


# Exemplo sum() -> Recebe como parâmetro um interável, podendo receber um valor inicial, e retorna a soma total dos
# elementos, incluindo o valor inicial.
# O valor inicial default = 0
# Exemplo de sum()
print(sum([2, 4, 6, 8]))
print(sum([2, 4, 6, 8, 5]))
print(sum({'a': 0, 'b': 2, 'c': 4, 'd': 6, 'e': 8}.values()))


# round() -> Retorna um número arredondada para n digito de precisão após a casa decimal. Se a precisão não for
# informada retorna o inteiro mais próximo da entrada
print(round(10.5))
print(round(10.6))
print(round(10.34444, 2))




