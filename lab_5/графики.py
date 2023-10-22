import matplotlib.pylab as plt
import numpy as np
# plt.plot([1, 2, 3, 4, 5], [4, 7, 3, 1, 5])
# plt.show()

# x = np.linspace(-2, 5, 50)
# y1 = [i ** 2 for i in x]
# y2 = [i + 2 for i in x]
#
# plt.title('Зависимости y1 = x^2, y2 = x + 2')
# plt.xlabel('x')
# plt.ylabel('y')
# plt.grid()
# plt.plot(x, y2, x, y1)
# plt.show()

# x = np.linspace(0, 10, 50)
# y1 = x * 2
#
# y2 = [i**2 for i in x]
#
# plt.figure(figsize=(9, 9))
# plt.subplot(2, 1, 1)
# plt.plot(x, y1)
# plt.title('Зависимости: y1 = x * 2, y2 = x^2')
# plt.ylabel('y1', fontsize=14)
# plt.grid(True)
# plt.subplot(2, 1, 2)
# plt.plot(x, y2)
# plt.xlabel('x', fontsize=14)
# plt.ylabel('y2', fontsize=14)
# plt.grid(True)


x = np.arange(0.0, 5, 0.01)
y = np.cos(x*np.pi)
plt.plot(x, y, c = 'r')
plt.fill_between(x, y)


plt.show()
