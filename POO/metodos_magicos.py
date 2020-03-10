"""
POO - Métodos Mágicos

OBS: Todos os métodos dunder(double underline) vem da classe object.  dir(object)

Métodos mágicos são todos os métodos que utilizam o dunder(duplo underline).
ex:
__init__  => Construtor de uma classe

__repr__ => Representação de um objeto, ou seja, mostra todos os elementos de um objeto.

__str__ => Representação de um objeto, ou seja, mostra todos os elementos de um objeto. (Método __str__ é prioritário
 se usado com o print)

"""


class Livro:

    def __init__(self, titulo, autor, paginas):
        self.titulo = titulo
        self.autor = autor
        self.paginas = paginas

    # Sobrescrita(ato de polimorfismo) do método dunder __repr__
    # Uma vez existente esse método na classe todo objeto printado exibirá o que for retornado nesse método
    def __repr__(self):
        return f'{self.titulo} escrito por {self.autor}'

    # Retornará como prioridade a representação do objeto se usado com o comando print.
    def __str__(self):
        return self.titulo

    # Esse método retornara o len de página caso seja chamado um len do objeto instanciado da classe Livro.
    def __len__(self):
        return self.paginas

    # Método deleta objeto em memória
    def __del__(self):
        print('Um objeto do tipo livro foi deletado da memória')

    # Sobrescrevendo o método de add para saber trabalhar com junção de objetos, ou seja,
    # No caso de dois objetos ele retornará o __str__ dos dois objetos.
    def __add__(self, outro):
        return f'{self} unido ao {outro}'

    # Altera o comportamento do método de multiplicação permitindo o * multiplicar(printar) string quantas vezes for
    # passado pelo multiplicador
    def __mul__(self, outro):
        if isinstance(outro, int):
            msg = ''
            for n in range(outro):
                msg += ' ' + str(self)
            return msg
        return 'Não posso multiplicar!'


# Testando
livros1 = Livro('Python Rocks', 'Geek', 800)
livros2 = Livro('Python Django', 'Dacio', 450)


print(livros1)
print(livros2)
print(len(livros1))

print(livros1 + livros2)
print(livros1 * 3)
