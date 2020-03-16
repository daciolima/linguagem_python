def comer(comida, eh_saudavel):
    if eh_saudavel:
        final = 'quero manter a forma'
    else:
        final = 'a gente só vive uma vez'
    return f'Estou comendo {comida} porque {final}'


def dormir(num_horas):
    if num_horas > 8:
        return f'Ptz! Dormi muito! Estou atrasado para o trabalho!'
    else:
        return f'Continuo cansado após dormir por {num_horas} horas. :('


def eh_engracada(pessoa):
    comediantes = ['Jim Carrey', 'Bozo']
    if pessoa in comediantes:
        return True
    return False


# Classe usada para teste de hooks
class Robo:

    def __init__(self, nome, bateria=100, habilidades=[]):
        self.__nome = nome
        self.__bateria = bateria
        self.__habilidades = habilidades

    @property
    def nome(self):
        return self.__nome

    @property
    def bateria(self):
        return self.__bateria

    @property
    def habilidades(self):
        return self.__habilidades

    def carregar(self):
        self.__bateria = 100

    def dizer_nome(self):
        if self.__nome > 0:
            self.__bateria = -1
            return f'BEEP BOOP BEEP BOOP. EU SOU O {self.__nome.upper()}'
        return 'Bateria fraca. Favor recarregar e tentar novamente.'

