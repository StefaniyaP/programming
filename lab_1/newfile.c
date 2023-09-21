#include <stdio.h>
#include <stdlib.h>

int main()
{
    int a, b, sum_a = 0, sum_b = 0;
    do
    {
        printf("Введите значение a > 0: ");
        scanf("%d", &a);
        printf("Введите значение b > 0: ");
        scanf("%d", &b);
    } while(a <= 0 || b <= 0);

    int quotient_a = a; 
    while(quotient_a > 0)
    {
        sum_a = sum_a + quotient_a % 10;
        quotient_a = quotient_a / 10;
    }
    printf("Сумма цифр числа а равна %d\n", sum_a);
   
     
    int quotient_b = b; 
    while(quotient_b > 0)
    {
        sum_b = sum_b + quotient_b % 10;
        quotient_b = quotient_b / 10;
    }
    printf("Сумма цифр числа b равна %d\n", sum_b);

    if (sum_a < sum_b)
      printf("Частное от деления суммы цифр а на число b равно %f\n", (float)sum_a / b);
    else
      printf("Частное от деления суммы цифр b на число a равно %f\n", (float)sum_b / a);    
    
    return 0;
}
