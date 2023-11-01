import seaborn as sn
import math
import matplotlib.pylab as plt

x = plt.arange(-1.0, 1.0, 0.1)
y = [math.exp(-2 * math.sin(i)) for i in x]

# касательная к функции. d - уравнение касательной, где
# (-2 * math.exp(-2 * math.sin(x0)) * math.cos(x0) = f'(x0),
# math.exp(-2 * math.sin(x0) = f(x0)
dy = []
x0 = 0
for i in x:
    d = ((-2 * math.exp(-2 * math.sin(x0)) * math.cos(x0)) * (i - x0)) + math.exp(-2 * math.sin(x0))
    dy.append(d)

sn.lineplot(x=x, y=y)
g = sn.lineplot(x=x, y=dy)
g.set_title('Graph')
g.set(xlabel="x",
      ylabel="y")

plt.legend(labels=['y = e^(-2 * sin(x))', 'касательная к функции y'])
plt.annotate('точка касания', xy=(0, 1),  xycoords='data', xytext=(0, 2),
textcoords='data', arrowprops=dict(facecolor='y'))

plt.show()

