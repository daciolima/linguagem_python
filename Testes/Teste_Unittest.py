"""
Introdução ao módulo Unittest

Unittest -> Testes Unitários

O que são testes unitários?
Teste unitário é a forma de se testar unidades individualmente de código fonte.
Unidades individuais podem ser: Funções, métodos, classe, módulos etc.

OBS: Teste unitário não é específico da linguagem Python, é uma forma de teste.

Para criar nossos testes, criamos classes que herdam de unitest.TestCase e a partir
de então ganhamos todos os 'assertions' presentes no módulo.

Para rodar os testes, utilizamos unittest.main()
Ex:
if __name__ == "__main__":
    unittest.main()

No Console para rodar os teste de forma verbose apresentando os DocStrings """ """, rode: # python arquivo.py -v

TestCase -> Casos de teste para sua unidade

# Conhecendo as assertions

Método                     Checa que
assertEqual(a, b)          a == b
assertNotEqual(a, b)       a != b
assertTrue(x)              bool(x) is True
assertFalse(x)             bool(x) is False
assertIs(a, b)             a is b
assertIsNot(a, b)          a is not b
assertIsNone(x)            x is None
assertIsNotNone(x)         x is not None
assertIn(a, b)             a in b
assertNotIn(a, b)          a not in b
assertIsInstance(a, b)     isinstance(a, b)
assertNotIsInstance(a, b)  not isinstance(a, b)

"""

# Prática - Utilizando a abordagem TDD nos arquivos atividades_unittest.py e testes.py

