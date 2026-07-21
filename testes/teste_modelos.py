"""Testes rápidos dos módulos usados no início do livro."""

import unittest

from codigo.cinematica import estado_mruv, posicao_mru
from codigo.incertezas import divisao_com_incerteza
from codigo.vetores import angulo_graus, modulo, produto_escalar


class TesteCinematica(unittest.TestCase):
    def test_mru(self):
        self.assertEqual(posicao_mru(5, x0=2, v=3), 17)

    def test_mruv(self):
        self.assertEqual(estado_mruv(2, x0=1, v0=3, a=2), (11, 7))


class TesteVetores(unittest.TestCase):
    def test_operacoes(self):
        self.assertEqual(modulo((3, 4)), 5)
        self.assertEqual(produto_escalar((1, 0), (0, 2)), 0)
        self.assertAlmostEqual(angulo_graus((1, 0), (0, 1)), 90)


class TesteIncertezas(unittest.TestCase):
    def test_divisao(self):
        valor, sigma = divisao_com_incerteza(12.0, 0.1, 3.0, 0.1)
        self.assertAlmostEqual(valor, 4.0)
        self.assertGreater(sigma, 0)


if __name__ == "__main__":
    unittest.main()
