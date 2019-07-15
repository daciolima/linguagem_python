"""
Em python, um dado é considerado do tipo string sempre que:
- Estiver entre dessa forma = 'daciolima', "daciolima"
- Estiver entre aspas duplas triplas para blocos ou aspas simples triplas também para blocos
"""

nome = 'DacioLima'
print(nome)
print(type(nome))

nome2 = 'Dacio \n Lima'
print(nome2)
print(type(nome2))

nome3 = """Dacio 
Lima"""
print(nome3)
print(type(nome3))
print(nome3.upper())
print(nome3.lower())

# Transforma em uma lista de string
print(nome3.split())

titulo = 'Setor de Informatica'
print(titulo[0:4]) # Imprime do indexe 0 ao 3, essa operação é chamada de slice de string
print(titulo[5:20]) # Imprime os quatro últimos elementos da variável, essa operação é chamada de slice de string
print(titulo.split()) # Transforma o variável em uma lista
print(titulo.split()[0]) # Imprime o primeiro elemento da variável convertida em lista
print(titulo.split()[1]) # Imprime o segundo elemento da variável convertida em lista
print(titulo.split()[2]) # Imprime o terceiro elemento da variável convertida em lista

print(titulo[0]) # Imprime o elemento 0 da string

print(titulo[::-1]) # Leia o primeiro elemento até o ultimo e depois retorno invertido

print(titulo.replace('S', 'I')) # Substitui o S por I

# Exemplo de texto palíndromo
texto = 'socorram me subino onibus em marrocos'
print(texto[::-1])


print(texto.split()[::-1])