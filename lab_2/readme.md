# Прог. Лабораторная работа №2
## Задание:
___сложность: Rare___     
1. Написать программу по вариантуб используя оператор цикла ```while``` (так как вариант нечетный).
2. Построить график с использованием ```gnuplot```.
3. Составить блок-схемы.
4. Оформить отчет в README.md, который должен содержать:
   - задание
   - описание проделанной работы
   - скриншоты результатов
   - блок-схемы
   - график функции
   - ссылки на используемые материалы     
     
___сложность: Medium___
1. использовать ```gnuplot``` напрямую из программы. минуя файлы и перенаправление вывода.
2. реалтзовать анимацию построения графика.
3. сохранить анимированный график в формате gif.

## Ход работы:
### Написание программы через операторы циклов ```while``` и ```for```
7 вариант:   
![](https://github.com/StefaniyaP/programming/assets/144994975/ed52db9a-bb7b-43cd-83d8-c48afc965304)   
#### С оператором цикла ```while```
Программа:    
``` C
#include <stdio.h>
#include <math.h>

int main()
{
    double x = -1.0, h, y, eps;
    printf("Enter h:\n");
    scanf("%lf", &h);
    eps = h / 2.0;
    printf("    x        y\n");

    while (x >= -1.0 - eps && x <= 2.0 + eps)
    {
        if (x <= 1.0 + eps)
          y = exp(-2.0 * sin(x));
        else
          y = pow(x, 2) - (cos(x) / sin(x));
        printf("%f %f\n", x, y);
        x = x + h;
    }   
    return 0;
}
```
Был создан файл "plot.gpi", который мы сделали исполняемым с помощью команды ```chmod +x plot.gpi```:
```C
#!/usr/bin/env -S gnuplot -persist
# set terminal png enhanced
# set output "my_graph.png"
set xlabel "x" 
set ylabel "f(x)"
set grid
set title "График функции f(x)"
plot "my_graph.txt" with lines title "f(x)"
```

Также был создан файл "my_graph.txt", в который программа будет осуществлять вывод вместо терминала. Для этого мы воспользовались командой  ```./prog > my_graph.txt```.     
Вот что получилось:    
![image](https://github.com/StefaniyaP/programming/assets/144994975/9e2b73e5-ab17-46ca-b827-9444200ef5d0)    

Далее был построен график при помощи команды ```./plot.gpi``` и сохранен в формате png:    
![image](https://github.com/StefaniyaP/programming/assets/144994975/1bf705f3-7a3b-4426-b90f-a2e053a6243f)

И построена блок-схема для данной программы:   
![image](https://github.com/StefaniyaP/programming/assets/144994975/2d697a3b-090b-4055-aae6-54f6faf43f59)   

#### С оператором цикла ```for```
Программа: 
```C
#include <stdio.h>
#include <math.h>
#include <unistd.h>

FILE *output;
FILE *gp;

int main()
{
    gp = popen("gnuplot -p", "w");
    output = fopen("sistema.dat", "w");

    double x = -1.0, h, y, eps;
    printf("Enter h:\n");
    scanf("%lf", &h);
    eps = h / 2.0;

    fprintf(gp, "plot './sistema.dat' with lines\n");

    for(; x >= -1.0 - eps && x <= 2.0 + eps; x += h)
    {
        if (x <= 1.0 + eps)
          y = exp(-2.0 * sin(x));
        else
          y = pow(x, 2) - (cos(x) / sin(x));
        fprintf(output,"%f %f\n", x, y);
        fflush(output); 
        usleep(1000000);
        fprintf(gp, "replot \n");
        fflush(gp);
    }
    fclose(gp);
    fclose(output);
  
    return 0;
}
```    
В данной программе было реализовано задание сложности Medium: ```gnuplot``` использовался напрямую из программы, благодаря чему при запуске кода можно увидеть процесс построения графика в реальном времени. 
     
Блок-схема для данной программы:     
![image](https://github.com/StefaniyaP/programming/assets/144994975/43e8e10f-8e96-41f4-9b8a-c0a13ee925ba)

## Используемые материалы:   
![Статья на Хабре "Gnuplot и с чем его едят"](https://habr.com/ru/companies/ruvds/articles/517450/)


