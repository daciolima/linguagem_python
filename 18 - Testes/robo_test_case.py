import unittest

from .atividades_testes_robo import Robo


class RoboTest(unittest.TestCase):

    def setUp(self):
        self.megaman = Robo('Mega Man', bateria=50)

    def test_carregar(self):
        self.megaman.carregar()
        self.assertEqual(self.megaman.bateria, 100)

    def test_dizer_nome(self):
        self.assertEqual(self.megaman.dizer_nome(), 'BEEP BOOP BEEP BOOP. EU SOU O MEGA MAN')
        self.assertEqual(self.megaman.bateria, 49, 'Bateria deveria está em 49%.')

    def tearDown(self):
        print('Está sendo executado!')


if __name__ == "__main__":
    unittest.main()
