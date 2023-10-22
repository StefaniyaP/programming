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
     
## Ход работы:
Было создано виртуальное окружение и установлены библиотеки ```matplotlib``` и ```numpy```    
    
![image](https://github.com/StefaniyaP/programming/assets/144994975/a826326e-9ba2-4cac-a57f-aecbed528174)     
      
![image](https://github.com/StefaniyaP/programming/assets/144994975/75087e5f-38d8-49a7-b0e8-cdd181177a6f)    
    
В книге [Devpractice Team. Библиотека Matplotlib](https://evil-teacher.on.fleek.co/books/prog_pm/matplotlib.pdf) изучены 1-3 уроки

Мой вариант:   

![image](https://github.com/StefaniyaP/programming/assets/144994975/2934e009-92a1-4fcd-93d8-a16ae915a916)

### Графики, построенные во время выполнения уроков 1-3:
![image](https://github.com/StefaniyaP/programming/assets/144994975/1f0a7f4e-9454-47eb-8263-3172dc6067b6)

![image](https://github.com/StefaniyaP/programming/assets/144994975/c8972f81-7c17-49f3-bfd0-2788c5521521)

![image](https://github.com/StefaniyaP/programming/assets/144994975/e956241b-f532-4697-992a-849539f1bbc0)

![image](https://github.com/StefaniyaP/programming/assets/144994975/66590eba-27e7-421d-8383-f2d8dab29d7a)

![image](https://github.com/StefaniyaP/programming/assets/144994975/7048a56f-ebfc-4e97-ac3c-58c62cef12c1)

![image](https://github.com/StefaniyaP/programming/assets/144994975/659ec4dd-ef51-43cb-9357-6571278c9131)

![image](https://github.com/StefaniyaP/programming/assets/144994975/c5b62bcc-8cab-47b6-a561-3e8fa7af6b2f)

![image](https://github.com/StefaniyaP/programming/assets/144994975/8aa7b57a-ffa4-46a1-84c1-b88ae0e48e5d)

![image](https://github.com/StefaniyaP/programming/assets/144994975/147773c0-db0e-4c8c-b052-f7921f2fdc4a)

![image](https://github.com/StefaniyaP/programming/assets/144994975/33c8e0c9-e316-4422-9378-e6a77143d7b3)

![image](https://github.com/StefaniyaP/programming/assets/144994975/878c4d8c-31e8-4bc8-965d-73fb349b28f7)

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

### График по заданию 4:


