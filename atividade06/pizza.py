from initialize import initialize
import matplotlib.pyplot as plt

x, y = initialize()

labels = ["A", "B", "C", "D",
             "E", "F", "G", "H", "I", "J"]

valores = x[0:10]

explode = [0,0.1,0,0,0,0.1,0,0,0.1,0]

plt.pie(valores, explode=explode, labels=labels, startangle=45)
plt.axis('equal')
plt.legend(title='Legenda')
plt.show()