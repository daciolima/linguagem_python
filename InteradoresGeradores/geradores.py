"""
Geradores

-   Geradores(Generators) são Interators (Interadores);

Obs: O contrário não é verdadeiro. Ou seja, nem todo interator é um generator

Outras informações:
-   Generators podem ser criadas com funções geradoras;
-   Funções geradoras usam a palavra reservada yield
-   Generators podem ser criados com expressões geradoras

Diferença entre Funções e Generator Functions (Funções Geradoras)

Funções:
1 - Utilizam return
2 - return só uma vez
3 - Quando executada retorna um valor

Generator Functions:
1 - Utilizam yield
2 - Pode utilizar yield várias vezes
3 - Quando executada retorna um generator

"""

# Exemplo de Generator Function(Função Geradora)
# OBS: Uma Generator Function não é um Generator, ela retorna um Generator.
def conta_ate(valor_maximo):
    contador = 1
    while contador <= valor_maximo:
        yield contador
        contador = contador + 1

# Teste da Generator Function
gen = conta_ate(10)
#print(type(gen))

print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))

print("continua...")

# Interando
for num in gen:
    print(num)

# Repare que a variável gen continuou imprimindo valor apesar de ser dois momentos diferentes.

# Imprimindo todos os elementos dentro de um generator de uma vez
gen2 = conta_ate(20)
print(list(gen2))

