from ponto import Ponto


class Quadrilatero:
    def __init__(self, p1, p2):
        self._p1 = p1
        self._p2 = p2

    def getP1(self):
        return self._p1

    def getP2(self):
        return self._p2

    def contidoEmQ(self, O):
        xP1 = self.getP1().getX()

        xO = O.getX()

        xP2 = self.getP2().getX()

        yP2 = self.getP2().getY()

        yO = O.getY()

        yP1 = self.getP1().getY()

        return (xP1 <= xO and xO <= xP2 and (yP2 <= yO and yO <= yP1))


p1 = Ponto(5, 6)

p2 = Ponto(11, 4)

q = Quadrilatero(p1, p2)

o = Ponto(8, 5)

res = q.contidoEmQ(o)

print(res)

a = Ponto(2, 2)

sol = q.contidoEmQ(a)

print(sol)

b = Ponto(7, 6)

s = q.contidoEmQ(b)

print(s)
