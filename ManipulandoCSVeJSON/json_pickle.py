"""

JSON e Pickle

JSON - Javascript Object Notation

API => São meios de comonunicação entre os serviços oferecidos por empresas (Twitter, Facebook, Youtube...) e
terceiros (nós desenvolvedores)


"""

import json
import jsonpickle


class Gato:

    def __init__(self, nome, raca):
        self.__nome = nome
        self.__raca = raca

    @property
    def nome(self):
        return self.__nome

    @property
    def raca(self):
        return self.__raca


felix = Gato('Felix', 'Cianes')
print(felix.__dict__)
ret = json.dumps(felix.__dict__)
print(ret)

# Integrando Json com Pickle  # pip install jsonpickle
# Imprimindo
ret_json_pickle = jsonpickle.encode(felix)
print(ret_json_pickle)

# Criando arquivo jsonpickle
with open('felix.json', 'w') as arquivo:
    arquivo.write(ret_json_pickle)

# Lendo arquivo jsonpickle
with open('felix.json', 'r') as arquivo:
    conteudo = arquivo.read()
    ret = jsonpickle.decode(conteudo)
    print(ret)
    print(type(ret))
    print(ret.nome)
    print(ret.raca)