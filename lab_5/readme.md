# Прог. Лабораторная работа №5
## Задание:
_Сложность:_ Rare
1. Создать в каталоге для данной ЛР в своем репозитории виртуальное окружение и установить в него ```matplotlib``` и ```numpy```.
Создать файл ```requirements.txt```.
2. Открыть книгу [Devpractice Team. Библиотека Matplotlib](https://evil-teacher.on.fleek.co/books/prog_pm/matplotlib.pdf)
и выполнить уроки 1-3.
3. Выбрать одну из неразрывных функций своего варианта из ЛР№2, построить
график этой функции и касательную к ней. Добавить на график
заголовок, подписи осей, легенду, сетку, а также аннотацию
к точке касания.
4. Оформить отчет в ```readme.md```, который должен содержать:
- графики, построенные во время выполнения уроков из книги
- объяснения процесса решения и график по заданию 4
5. Склонировать [репозиторий](https://github.com/still-coding/report_tool.git) рядом
со своим репозиторием. Изучить использование этого инструмента и создать pdf-версию
отчета из ```readme.md```. Добавить ее в репозиторий

_Сложность:_ Medium
- построить все графики с использованием seaborn
     
## Ход работы:
Было создано виртуальное окружение и установлены библиотеки ```matplotlib``` и ```numpy```    
    
![image](https://github.com/StefaniyaP/programming/assets/144994975/a826326e-9ba2-4cac-a57f-aecbed528174)     
      
![image](https://github.com/StefaniyaP/programming/assets/144994975/75087e5f-38d8-49a7-b0e8-cdd181177a6f)    
    
В книге [Devpractice Team. Библиотека Matplotlib](https://evil-teacher.on.fleek.co/books/prog_pm/matplotlib.pdf) изучены 1-3 уроки

Мой вариант:   

![image](https://github.com/StefaniyaP/programming/assets/144994975/2934e009-92a1-4fcd-93d8-a16ae915a916)

### Графики, построенные во время выполнения уроков 1-3:
#### Matplotlib
1) ![image](https://github.com/StefaniyaP/programming/assets/144994975/2f4cdb81-65f0-4269-b2c1-913843904bf7)
2) ![image](https://github.com/StefaniyaP/programming/assets/144994975/06a64184-4f69-4463-8655-d1e31930e076)
3) ![image](https://github.com/StefaniyaP/programming/assets/144994975/b182c72c-b4b0-400e-8749-4bdf24ec8653)
4) ![image](https://github.com/StefaniyaP/programming/assets/144994975/70591f8f-88a8-459f-aeb2-d26ed95c658b)
5) ![image](https://github.com/StefaniyaP/programming/assets/144994975/5ca43390-3540-4d01-a04b-f32b64863475)
6) ![image](https://github.com/StefaniyaP/programming/assets/144994975/2f4ac36e-c8b3-4ca7-b075-8114fb1a436c)

#### Seaborn
1) ![image](https://github.com/StefaniyaP/programming/assets/144994975/27187d7f-ca84-4197-8480-22dfa8366fe0)
2) ![image](https://github.com/StefaniyaP/programming/assets/144994975/b84ded69-3b4c-4164-9851-547bb7f3ed21)
3) ![image](https://github.com/StefaniyaP/programming/assets/144994975/618d46e5-32d1-403f-bdc8-62f3c5d9c33f)
4) ![image](https://github.com/StefaniyaP/programming/assets/144994975/9a40ad07-4ca6-4de9-8e9b-15561703012f)
5) ![image](https://github.com/StefaniyaP/programming/assets/144994975/7211e3ca-1b9d-44ee-bc1d-5ccaa714e3f2)
6) ![image](https://github.com/StefaniyaP/programming/assets/144994975/d022c897-30b4-4f39-be14-4a4ea4a90004)

### График по варианту:
```Python
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
```
![image](https://github.com/StefaniyaP/programming/assets/144994975/18213b76-02aa-4f16-a4b4-c260b357da54)

### Сложность Medium

График по варианту:   
```Python
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
g.set(xlabel="x", ylabel="y")

plt.legend(labels=['y = e^(-2 * sin(x))', 'касательная к функции y'])

g.text(0, 1, "точка касания")

plt.show()
```

![image](https://github.com/StefaniyaP/programming/assets/144994975/769ff78f-c2ad-4ea4-8ddf-df405edd3d44)





