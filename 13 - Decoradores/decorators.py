""""
Decoradores - (Decorators)

O que são decorators?
- Decorators são funções;
- Decorators envolvem outras funções e aprimoram seus comportamentos
- Decorators também são exemplos de Higher
"""

# Exemplo e função decorada(Aprimorada)
# Decorators como funções (Sintaxe não recomendada / Sem açucar sintático)
def seja_educado(funcao): # <= Decorators Function
    def sendo():
        print('Foi um prazer conhecer você!')
        funcao()
        print('Tenha um ótimo dia!')
    return sendo

def saudacao():
    print('Seja Bem-vindo(a) à Geek University!')

# Testando
teste = seja_educado(saudacao)  # <= Decorators
teste()



# Function Decorators
# Decorators com Syntax Sugar (Açúcar Sintático)
def seja_educado_mesmo(funcao):   # <= Decorators Function
    def sendo_mesmo():
        print('Foi um prazer conhecer você')
        funcao()
        print('Tenha um excelente dia!')
    return sendo_mesmo

@seja_educado_mesmo   # <= Decorators
def apresentando():
    print('Meu nome é Pedro!')

# Testando
apresentando()




