import matplotlib.pylab as plt


def wallis_multiplier(i):
    i_squared_times_4 = 4 * i * i
    wm = i_squared_times_4 / (i_squared_times_4 - 1)
    return wm


x = plt.arange(1.6, 2001, 1)

y = wallis_multiplier(x)


plt.title('Pi Convergence plot')
plt.ylabel("Wallis Product value")
plt.xlabel("Iterations")
plt.plot(x, y, ".")

plt.show()

