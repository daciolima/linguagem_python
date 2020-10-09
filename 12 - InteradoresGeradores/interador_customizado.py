"""

Escrevendo um interador customizado

Os mêtodos iter() e next() são responsáveis por criar qualquer interator

"""

class Contador:
    def __init__ (self, menor, maior):
        self.menor = menor
        self.maior = maior

    def __iter__(self):
        return self

    def __next__(self):
        if self.menor < self.maior:
            numero = self.menor
            self.menor = self.menor + 1
            return  numero
        raise StopIteration

con = Contador(1, 6)

it = iter(con)

print(next(it))
print(next(it))
print(next(it))
print(next(it))
print(next(it))


for n in Contador(1, 60):
    print(n)

for n in range(1, 60):
    print(n)
