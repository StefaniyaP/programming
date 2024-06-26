# Прог. Лабораторная работа №3
## Задание:
__сложность:__ Rare
1. Написать программу по своему варианту (7 вариант)
   _Найти в массиве первое вхождение искомого элемента, а все элементы в частях массива до и после него “перевернуть”, то есть поменять порядок их следования на обратный. Если такого элемента нет, “перевернуть” весь массив._
2. Оформить отчет в ```readme.md```, который должен содержать:
   - Задание
   - описание проделанной работы
   - скриншоты результатов
   - ссылки на используемые материалы
                   
__сложность:__ Medium
   - Использовать динамическое выделение памяти для хранения данных программы

## Ход работы:
### Сложность Rare
Код:
```C
#include <stdio.h>
#include <stdlib.h>
#include <time.h>

void random_fill(int k, int a[])
{
    int i;
    for (i = 0; i < k; i++)
        a[i] = rand() % 31;
}

int main()
{
    srand(time(NULL));
    int k, i, n;
    printf("k (array length) -> ");
    scanf("%d", &k);
    int A[k];

    random_fill(k, A);

    for (i = 0; i < k; i++)
        printf("%4d ", A[i]);

    printf("\n");

    printf("n (unknown number) -> ");
    scanf("%d", &n);

    int index = -1;
    int tmp;
    for (i = 0; i < k; i++)
      if (A[i] == n) {
        index = i;
        break;
    }
         
     if(index != -1) {
        int m = index;
        for (i = 0; i < m/2; i++)
        {
            tmp = A[i];
            A[i] = A[m - i - 1];
            A[m - i - 1] = tmp;
        }
        m = index + 1;
        int l = k - m;
        for (i = m; i < m + l / 2; i++)
        {
            tmp = A[i];
            A[i] = A[k + m - i - 1];
            A[k + m - i - 1] = tmp;
        }  

     } else {
        for (i = 0; i < k/2; i++)
        {
            tmp = A[i];
            A[i] = A[k - i - 1];
            A[k - i - 1] = tmp;
        } 

     }
 
    for (i = 0; i < k; i++)
        printf("%4d ", A[i]);

    printf("\n");
    return 0;
}
```
Программа получает от пользователя такое количество элементов ```k```, которое необходимо поместить в массив, причем числа, помещаемые в массив, генерируются рандомно. Генерируется массив с помощью функции ```random_fill```, печатается массив, после этого пользователь вводит число ```n``` которое необходимо найти в массиве. Вводится флаг ```index = - 1```, с помощью которого проверяется, существует ли ```n``` в сгенерированном массиве. Если существует, то ```index``` становится равен индексу числа ```n``` в полученном массиве, причем только одному, так как после этого в цикле ```for```, который отвечает за это переназначение, выполняется оператор ```break```. Далее проверяется условие: если ```index``` не равен -1, то все числа до и после числа ```n``` в массиве "переворачиваются". Пример:  
       
![image](https://github.com/StefaniyaP/programming/assets/144994975/285442c9-f239-4ae9-96ef-666d4e91b4f9)   
     
В примере видно, что элементы до найденного числа ```n```, которое равно 13 в данном случае, печатаются в результате в обратном порядке. То же самое происходит и с числами, идущими после числа ```n```.   
Это же и работает, если количество элементов массива нечетно:    
    
![image](https://github.com/StefaniyaP/programming/assets/144994975/dde565aa-ac1e-489b-b066-146bf591a6fe)      
     
Итак, если же условие, описанное выше, не выполняется, то есть ```index``` по-прежнему равен -1 и числа ```n``` в списке нет, список переворачивается полностью. Пример:     
      
![image](https://github.com/StefaniyaP/programming/assets/144994975/828d07e2-6d9b-414c-a1d8-1d4c17254ee0)     
      
И при нечетном количестве элементов:     
     
![image](https://github.com/StefaniyaP/programming/assets/144994975/ae681c87-568d-4098-8b3c-6921c3dd2426)   

### Сложность Medium
Динамическое выделение памяти под массив:   
```С
    int* arr;
    arr = (int*)malloc(k * sizeof(int));
```
Проверка, действительно ли выделяется память:
```С
    if (arr == NULL)
        printf("Memory allocation error");
    else
        printf("ok\n");
```
Освобождение выделенной памяти:   
```С
    free(arr);
```
Вывод:   
![img.png](img.png)

Полный код:   
```C
#include <stdio.h>
#include <stdlib.h>
#include <time.h>

void fill(int k, int a[])
{
    int i;
    for (i = 0; i < k; i++)
        a[i] = rand() % 31;
}

int main()
{
    srand(time(NULL));
    int k, i, n;
    int* arr;
    printf("k (array length) -> ");
    scanf("%d", &k);
    int A[k];

    arr = (int*)malloc(k * sizeof(int));
    if (arr == NULL)
        printf("Memory allocation error");
    else
        printf("ok\n");

    fill(k, A);

    for (i = 0; i < k; i++)
        printf("%4d ", A[i]);

    printf("\n");

    printf("n (unknown number) -> ");
    scanf("%d", &n);

    int index = -1;
    int tmp;
    for (i = 0; i < k; i++)
      if (A[i] == n) {
        index = i;
        break;
    }

     if(index != -1) {
        int m = index;
        for (i = 0; i < m/2; i++)
        {
            tmp = A[i];
            A[i] = A[m - i - 1];
            A[m - i - 1] = tmp;
        }
        m = index + 1;
        int l = k - m;
        for (i = m; i < m + l / 2; i++)
        {
            tmp = A[i];
            A[i] = A[k + m - i - 1];
            A[k + m - i - 1] = tmp;
        }

     } else {
        for (i = 0; i < k/2; i++)
        {
            tmp = A[i];
            A[i] = A[k - i - 1];
            A[k - i - 1] = tmp;
        }

     }

    for (i = 0; i < k; i++)
        printf("%4d ", A[i]);

    printf("\n");


    free(arr);
    return 0;
}
```
      
### Блок-схема:

![image](https://github.com/StefaniyaP/programming/assets/144994975/61c901bf-7e39-44ed-8c14-d2d562753fcd)      

## Ссылки на используемые материалы:
[Stack Overflow](https://stackoverflow.com)


