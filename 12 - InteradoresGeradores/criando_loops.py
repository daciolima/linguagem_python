"""
Criando sua própria versão de loop

"""

for num in [1, 2, 3, 4, 5]:  # iter([1, 2, 3, 4, 5])
    print(num)  # aplicação do next()

for letra in 'Dácio Lima':  # iter('Dácio Lima')
    print(letra)  # aplicação do next()


# Criando loops customizados
def meu_for(interavel):
    it = iter(interavel)
    while True:
        try:
            print(next(it))
        except StopIteration:
            break

meu_for('APRENDENDO PYTHON')