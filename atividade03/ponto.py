from sys import exit

class Ponto:

    def __init__(self, x, y):
        if isinstance(x, (int, float)) and isinstance(y, (int, float)):
            self._x = x
            self._y = y
        else:
            print('Dados Inválidos!')
            self._x = None
            self._y = None
            exit()


    def getX(self):
        return self._x

    def getY(self):
        return self._y

    def setX(self, x):
        if isinstance(x, (int, float)):
            self._x = x
        else:
            print("Você forneceu uma abcissa que não é um número!")

    def setY(self, y):
        if isinstance(y, (int, float)):
            self._y = y
        else:
            print("Você forneceu uma ordenada que não é um número!")

    def qualQuadrante(self):
        x = self.getX()
        y = self.getY()

        if x > 0:
            if y > 0:
                print('Primeiro Quadrante!')
                return 1
            if y < 0:
                print('Quarto Quadrante!')
                return 4
        if x < 0:
            if y > 0:
                print('Segundo Quadrante!')
                return 2
            if y < 0:
                print('Terceiro Quadrante!')
                return 3
