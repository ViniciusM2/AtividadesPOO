import unittest
from quadrilatero import Quadrilatero
from ponto import Ponto

class TesteQuadrilatero(unittest.TestCase):
    def testeContidoEmQ(self):
        p1 = Ponto(5, 6)

        p2 = Ponto(11, 4)

        q = Quadrilatero(p1, p2)

        a = Ponto(8, 5)

        # dentro
        self.assertTrue(q.contidoEmQ(a))

        b = Ponto(2, 2)

        #fora
        self.assertFalse(q.contidoEmQ(b))

        c = Ponto(7, 6)

        # na periferia do quadrilátero
        self.assertTrue(q.contidoEmQ(c))


if __name__ == '__main__':
    unittest.main()