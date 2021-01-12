from ponto import Ponto
A = Ponto(1, 2)
B = Ponto(-3, 4)
C = Ponto(-45, -6)
D = Ponto(34, -100)

qA = A.qualQuadrante()
print(f'O número obtido foi: {qA}')

qB = B.qualQuadrante()
print(f'O número obtido foi: {qB}')

qC = C.qualQuadrante()
print(f'O número obtido foi: {qC}')

qD = D.qualQuadrante()
print(f'O número obtido foi: {qD}')
