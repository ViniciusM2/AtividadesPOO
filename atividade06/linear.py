from initialize import initialize
import matplotlib.pyplot as plt

x, y = initialize()

x.sort()
y.sort()

plt.plot(x,y)
plt.show()