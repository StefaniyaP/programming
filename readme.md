# Прог. Лабораторная работа №5
## Задание:
     
## Ход работы:
Было создано виртуальное окружение, в которые были установлены библиотеки ```matplotlib``` и ```numpy```    
    
![image](https://github.com/StefaniyaP/programming/assets/144994975/a826326e-9ba2-4cac-a57f-aecbed528174)     
      
![image](https://github.com/StefaniyaP/programming/assets/144994975/75087e5f-38d8-49a7-b0e8-cdd181177a6f)    
    
В книге [Devpractice Team. Библиотека Matplotlib](https://evil-teacher.on.fleek.co/books/prog_pm/matplotlib.pdf) 1 - 3 уроки:    
### Урок 1
Установлен ```matplotlib```, проверка установки и версии библиотеки:    
```Python
import matplotlib
print(matplotlib.__version__)
```

Вывод:     

![image](https://github.com/StefaniyaP/programming/assets/144994975/e917dc67-d0b5-408e-883d-949a1a1a9ef7)    
    
```Python
import matplotlib.pyplot as plt

plt.plot([1, 2, 3, 4, 5], [1, 2, 3, 4, 5])
plt.show()
```

