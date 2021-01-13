import unittest
from ponto import Ponto

class TestePonto(unittest.TestCase):
    
    def testeGetX(self):
        ponto = Ponto(3,4)
        self.assertTrue(ponto.getX() == 3)
        self.assertFalse(ponto.getX() == 75)

    def testeGetY(self):
        ponto = Ponto(6,7)
        self.assertTrue(ponto.getY() == 7)
        self.assertFalse(ponto.getY() == 98)

    def testeSetX(self):
        ponto = Ponto(9999999,4)
        ponto.setX(3)
        self.assertTrue(ponto.getX() == 3)

    def testeSetY(self):
        ponto = Ponto(3,999999999)
        ponto.setY(4)
        self.assertTrue(ponto.getY() == 4)

    def qualQuadrante(self):
        A = Ponto(1, 2)
        B = Ponto(-3, 4)
        C = Ponto(-45, -6)
        D = Ponto(34, -100)
        self.assertTrue(A.qualQuadrante()==1)
        self.assertTrue(B.qualQuadrante()==2)
        self.assertTrue(C.qualQuadrante()==3)
        self.assertTrue(D.qualQuadrante()==4)


if __name__ == '__main__':
    unittest.main()