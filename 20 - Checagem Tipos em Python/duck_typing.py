"""
O Tipo ou a classe dos objetos é menos importante do que o método que os definem
Ao invés de checar a classe ou tipos de dados... é checado é checada a presença ou
não de métodos ou atributos específicos.py
Quando vemos um objeto que é similar a outro, provavelmente os seus tipos de métodos, atributos e comportamentos
são iguais ou parecidos.

"""


class CisneNegro:
    def __len__(self):
        return 42


livro = CisneNegro()
nome = 'Dácio Lima'
idade = 41

print(len(livro))
print(len(nome))
print(len(idade))

