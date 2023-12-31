# Лабораторная работа №6
__Сложность:__ ___Rare___
1. Написать программу для решения задач своего варианта
2. Оформить отчет в ```readme.md```, который будет содержать:
   - условия задач
   - описание проделанной работы
   - скриншоты результатов
   - ссылки на используемые материалы
  
__Сложность:__ ___Medium___     
Написать для функций доктесты

## Требования и ограничения
Решения задач оформить в виде функций, возвращающих ответы. Для решения первой задачи использовать itertools.

## Мой вариант (вариант 7)
1) Иван составляет таблицу кодовых слов для передачи сообщений, каждому сообщению соответствует своё кодовое слово. 
  В качестве кодовых слов Иван использует все пятибуквенные слова в алфавите {A, B, C, D, E}, удовлетворяющие 
  такому условию: кодовое слово не может начинаться с буквы E и заканчиваться буквой A. Сколько различных кодовых слов 
  может использовать Иван?

2) Сколько единиц содержится в двоичной записи значения выражения: $4^{511} + 2^{511} − 511$?

3) Пусть $M(N)$  — произведение 5 наименьших различных натуральных делителей натурального числа $N$,
  не считая единицы. Если у числа $N$ меньше 5 таких делителей, то $M(N)$ считается равным нулю.
  Найдите 5 наименьших натуральных чисел, превышающих $200 000 000$, для которых 0 < $M(N)$ < $N$.
  В ответе запишите найденные значения $M(N)$ в порядке возрастания соответствующих им чисел $N$.

## Код
1) ```Python
    from itertools import *

    # Иван составляет таблицу кодовых слов для передачи сообщений, каждому сообщению соответствует 
    # своё кодовое слово. В качестве кодовых слов Иван использует все пятибуквенные слова в алфавите 
    # {A, B, C, D, E}, удовлетворяющие такому условию: кодовое слово не может начинаться с буквы E 
    # и заканчиваться буквой A. Сколько различных кодовых слов может использовать Иван?
    
    alphabet = {'A', 'B', 'C', 'D', 'E'}
    
    def iter(alphabet):
        b = []
        s = ''
        c = 0
        comb = permutations(alphabet, 5)
        for i in comb:
            if i[1] != 'E' and i[-1] != 'A':
                c += 1
                s = ''.join(i)
            b.append(s)
        # return c, b
        return c
    
    print(iter(alphabet))
   ```
    Вывод:
  
    ![image](https://github.com/StefaniyaP/programming/assets/144994975/6977b135-886a-40c4-b4a0-02d282d00a0f)

   ### Код с доктестом:
   ```Python
    import doctest
    from itertools import *
   
    alphabet = {'A', 'B', 'C', 'D', 'E'}
    def iter(alphabet):
        ''' 
        >>> iter(alphabet)
        91
        >>> iter({'N', 'V', 'K'})
        43
        >>> iter(12)
        3
        '''
        
        b = []
        s = ''
        c = 0
        comb = permutations(alphabet)
        for i in comb:
            if i[1] != 'E' and i[-1] != 'A':
                c += 1
                s = ''.join(i)
            b.append(s)
        # return c, b
        return c
    
    print(iter(alphabet))
    
    doctest.testmod(name='iter', verbose=True)
   ```

   Вывод:

    ![image](https://github.com/StefaniyaP/programming/assets/144994975/76f19d14-3b54-4a3d-8873-46b4852bf52a)

2) ```Python
    # Сколько единиц содержится в двоичной записи значения выражения: 4^511+2^511−511?

    x = 4 ** 511 + 2 ** 511 - 511

    def convert(x):
        b = ''
        while x > 0:
            a = x % 2
            b += str(a)
            x //= 2
        return b  

    b = convert(x)
    print(b.count('1'))  
   ```
    Вывод:
    
    ![image](https://github.com/StefaniyaP/programming/assets/144994975/51cb16c3-0cd0-4885-8bc4-7f9ee79370b2)

   ### Код с доктестом:
   ```Python
    import doctest

    x = 4 ** 511 + 2 ** 511 - 511
    
    
    def convert(x):
        '''
        >>> convert(x)
        504
    
        >>> convert(127)
        102
    
        >>> type(convert(127))
        <class 'str'>
        '''
    
        b = ''
        while x > 0:
            a = x % 2
            b += str(a)
            x //= 2
        return b.count('1')
    
    
    print(convert(x))
    
    doctest.testmod(name='convert', verbose=True)
   ```
   Вывод:
   
   ![image](https://github.com/StefaniyaP/programming/assets/144994975/f92aab7e-e79d-457f-bc8c-717e69dba63c)

4) ```Python
    # Пусть M(N) — произведение 5 наименьших различных натуральных делителей 
    # натурального числа N, не считая единицы. Если у числа N меньше 5 таких
    # делителей, то M(N) считается равным нулю.
    # Найдите 5 наименьших натуральных чисел, превышающих 200 000 000,
    # для которых 0 <M(N) < N. В ответе запишите найденные значения M(N)
    # в порядке возрастания соответствующих им чисел N.
    
    c = 0
    
    def m(n):
        s = []
        for d in range(2, int(n**0.5) + 1):
            if n % d == 0:
                s.append(d)
                s.append(n // d)
    
        if len(s) >= 5:
            s = sorted(s)
            return s[0] * s[1] * s[2] * s[3] *s[4]
        else:
            return 0
    
    n = 200000001
    def res(n):
        c = 0
        a = []
        while c < 5:
            if 0 < m(n) < n:
                a.append(str(m(n)) + ' - ' + str(n))
                c += 1
            n += 1  
        return a
  

    print(res(n))
    ```
    Вывод:         
  
    ![image](https://github.com/StefaniyaP/programming/assets/144994975/3d849268-03a0-4bb6-b207-a7afffb58539)

     ### Код с доктестом:
     ```Python
     import doctest
  
      def m(n):
          '''
          >>> type(m(n))
          <class 'int'>
          '''
          s = []
          for d in range(2, int(n**0.5) + 1):
              if n % d == 0:
                  s.append(d)
                  s.append(n // d)
      
          if len(s) >= 5:
              s = sorted(s)
              return s[0] * s[1] * s[2] * s[3] *s[4]
          else:
              return 0
      
      n = 200000001
      
      def res(n):
          '''
          >>> res(n)
          ['1728 - 200000004', '21632 - 200000008', '1260 - 200000010', '1152 - 200000016', '4127787 - 200000019']
      
          >>> res(128)
          3
      
          >>> type(res(n))
          <class 'int'>
          '''
          c = 0
          a = []
          while c < 5:
              if 0 < m(n) < n:
                  a.append(str(m(n)) + ' - ' + str(n))
                  c += 1
              n += 1  
          return a
          
      
      print(res(n))
      
      doctest.testmod(name='res', verbose=True)
     ```
  
     Вывод:

     ![image](https://github.com/StefaniyaP/programming/assets/144994975/f712c3fa-571d-49d8-ad72-77b0e97f0f59)
