# Прог. Лабораторная работа №0
## Задача:
1. Создать репозиторий для дисциплины на [Github](https://github.com).
2. Склонировать его себе на ПК.
3. Написать свою первую программу
4. Скомпилировать и запустить ее
5. Получить по отдельности результаты каждого этапа компиляции.
6. Написать отчет в README.md, который должен содержать:
   - задание
   - описание проделанной работы
   - консольные команды
   - скриншоты результатов
   - ссылки на используемые материалы

## Описание проделанной работы:
1. На [ГитХаб](https://github.com) был создан [репозиторий](https://github.com/StefaniyaP/programming "programming") для дисциплины:
![image](https://github.com/StefaniyaP/programming/assets/144994975/88f70b3d-f3f8-42bb-9ac9-5a2aeef233a4)
2. После клонирования его на ПК была написана программа:


```C
#include <stdio.h>

int main()
{
    printf("Hello, World!\n");
    return 0;
}
```

Вывод в терминале после компиляции и запуска:
![image](https://github.com/StefaniyaP/programming/assets/144994975/99f122e3-c6c7-4ae8-a951-c822911173b0)

3. Результаты каждого этапа компиляции:
   1. Препроцессинг(предобработка)    
      Для того, чтобы увидеть результат препроцессинга, была вызвана команда `gcc.exe -E    newfile.c >newfile_preprocces.c`. Ее содержимое было отправленно в новый файл - "newfile_preprocess.c".    
      Начало файла:
      ![image](https://github.com/StefaniyaP/programming/assets/144994975/bade205a-134f-46bb-9158-bdaa019f08cb "начало файла")
      Конец файла:
      ![image](https://github.com/StefaniyaP/programming/assets/144994975/f5bd08e0-dd8d-478b-ab0c-1cda4c1ffa9c "конец файла")      
   3. Компиляция
      Чтобы получить результат компиляции, была вызвана команда `gcc.exe -c newfile.c`.
      При ее выполнении был создан файл "newfile.o", при попытке просмотреть который выходит следующее:
      ![image](https://github.com/StefaniyaP/programming/assets/144994975/709993dc-1f59-4e33-97ed-8f76be500f11)

   5. Линковка    
      Для этого этапа была вызванна команда `gcc.exe newfile.o -o newfile.exe`. В результате нее был создан исполняемый файл "newfile.exe", его содержимое:
      ![image](https://github.com/StefaniyaP/programming/assets/144994975/fd8d5d4a-f108-4ef6-872d-e8280899c575)
      Запустим исполняемый файл с помощью команды `.\newfile.exe` и получим: ![image](https://github.com/StefaniyaP/programming/assets/144994975/8ac8804f-d5c6-4dd5-a0f2-c93ce5fae84d)

### Используемый материал:
["Этапы компиляции на Си: предобработка, трансляция, компоновка", Тимофей Хирьянов](https://www.youtube.com/watch?v=UNJ1xTsH9ko)

## Шпаргалка по работе с git
![image](https://github.com/StefaniyaP/programming/assets/144994975/e670981f-d18e-4eee-9b73-a791e6bbb501)

   
