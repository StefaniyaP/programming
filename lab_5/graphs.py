import matplotlib.pylab as plt
import numpy as np
import seaborn as sn

#1
#plt.plot([1, 2, 3, 4, 5], [1, 2, 3, 4, 5])
#plt.show()

#sn.lineplot([1, 2, 3, 4, 5], [1, 2, 3, 4, 5])

#2
# x = np.linspace(0, 10, 50)
# y1 = x

# y2 = [i**2 for i in x]

# sn.lineplot(x=x, y=y1)
# g = sn.lineplot(x=x, y=y2)
# g.set_title('Зависимости: y1 = x, y2 = x^2')
# g.set(xlabel="x", ylabel="y1, y2")
# plt.grid()

#3
# fruits = ['apple', 'peach', 'orange', 'bannana', 'melon']
# counts = [34, 25, 43, 31, 17]
# g = sn.barplot(x=fruits, y=counts)
# g.set_title('Fruits!')
# g.set(xlabel='Fruit', ylabel='Count')

#4
# x = [1, 5, 10, 15, 20]
# y = [1, 7, 3, 5, 11]
# g = sn.lineplot(x=x, y=y)
# g.set_title('Chart price', fontdict={'size': 15})

# g.set_xlabel('Day', fontdict={'size': 12, 'color': 'blue'})
# g.set_ylabel('Price', fontdict={'size': 12, 'color': 'blue'})

# plt.legend(labels=['steel price'])
# plt.grid(True)
# g.text(15, 4, 'grow up!')

#5
# x = [1, 5, 10, 15, 20]
# y1 = [1, 7, 3, 5, 11]
# y2 = [i*1.2 + 1 for i in y1]
# y3 = [i*1.2 + 1 for i in y2]
# y4 = [i*1.2 + 1 for i in y3]

# fig, axs = plt.subplots(2, 2, figsize=(12, 7))
# sn.lineplot(x=x, y=y1, ax=axs[0, 0], linestyle='-')
# sn.lineplot(x=x, y=y2, ax=axs[0, 1], linestyle='--')
# sn.lineplot(x=x, y=y3, ax=axs[1, 0], linestyle='-.')
# sn.lineplot(x=x, y=y4, ax=axs[1, 1], linestyle=':')

#6
# x = [1, 5, 10, 15, 20]
# y1 = [1, 7, 3, 5, 11]
# y2 = [4, 3, 1, 8, 12]

# sn.lineplot(x=x, y=y1, marker='o')
# sn.lineplot(x=x, y=y2, linestyle='dashdot', marker='o')
# plt.legend(labels=['L1', 'L2'])

x = [1, 5, 10, 15, 20]
y1 = [1, 7, 3, 5, 11]
y2 = [4, 3, 1, 8, 12]

line1, = plt.plot(x, y1, 'o-b')
line2, = plt.plot(x, y2, 'o-.m')
plt.legend((line2, line1), ['L2', 'L1'])

plt.show()