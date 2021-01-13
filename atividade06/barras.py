from initialize import initialize
import matplotlib.pyplot as plt

x, y = initialize()

x = x[0:10]

divs = ["A", "B", "C", "D",
             "E", "F", "G", "H", "I", "J"]

valores = x

plt.bar(divs, valores, color='blue')
plt.title('Gráfico de Barras')
plt.xlabel('Divisões')
plt.ylabel("Valores")
plt.show()