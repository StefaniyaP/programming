import matplotlib.pylab as plt
import math

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

plt.title('Graph')
plt.xlabel('x')
plt.ylabel('y')
plt.grid(True)
plt.plot(x, y, 'g-', lw=1, label='y = e^(-2 * sin(x))')
plt.plot(x, dy, 'r-', label='касательная к функции y')
plt.legend()
plt.annotate('точка касания', xy=(0, 1),  xycoords='data', xytext=(0, 2),
textcoords='data', arrowprops=dict(facecolor='y'))
plt.ylim([0, 5])
plt.show()
