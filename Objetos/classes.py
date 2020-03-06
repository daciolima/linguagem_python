"""
POO - Classe

Em POO, Classe nada nada mais são do que modelos do mundo real sendo representado computacionalmentente.

Imagine que você queira fazer um sistema para automatizar o controle das lâmpadas da sua casa.

Classe podem conter:
    - Atributos -> Representam as características do objetos, ou seja, pelos atributos conseguidos
        representar computacionamente os estados de um objeto. No caso da lâmpada, possivelmente
        iríamos querer saber se a lâmpada é 110 ou 220 volts, se ela é branca, amarela, vermelha 
        ou outra cor, qual a luminosidade dela e etc.

    - Métodos(Funções) -> representam os comportamentos do objetos, ou seja, as ações que estes
    objetos podem realizar no seu sistema. No caso da lâmpada, por exemplo, um comportamento 
    comum que muito provavelmente iríamos querer representar no nosso sistema é o de ligar e 
    desligar a mesma.

Em Python, para definir uma classe usamos a palavra reservada class. 

OBS: Utilizamos a palavra 'pass'(passe) em python quando temos um bloco de código que ainda não está
    implementado.

OBS2: Os dois ponto(:) indica inicio de um bloco de código.

OBS3: Quando nomeamos nossas classes em Python utilizamos por convenção o nome com inicial em maipusculo. 
Se o nome for composto, utiliza-se as iniciais de ambas as palavras em maiúsculas, todas juntas. 

Dica: Em computação não utilizamos: Acentuação, caracteres especiais, espaços ou similares para nomes de 
classes, atributos, métodos, arquivos, diretórios e etc.

OBS: Quando estamos planejando um software e definimos quais classes teremos que ter no sistema, chamamos 
estes objetos que serão mapeados para classes de entidades.
"""

class Lampada:
    pass

class ContaCorrente:
    pass

lamp = Lampada()

print(type(lamp))

valor = int('42') # Operação de Cast
print(type(valor))