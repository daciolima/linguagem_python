"""
Mödulo Collections - Deque

Podemos dizer que o deque é uma lista de alta performance onde também é
possivel adicionar elementos no inicio
"""

from collections import deque

# Criando Deque
deq = deque('Dacio')
print(deq)

#Adicionando elementos no Deque
deq.append(" Lima") # Adiciona no final da lista

print(deq)

deq.appendleft('Meu nome: ')
print(deq)

# Remover elementos
deq.pop() # Remove o último elemento da lista
print(deq)

deq.popleft()

print(deq)