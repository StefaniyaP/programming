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
    int k, i, n, b;
    printf("k (size of an array) -> ");
    scanf("%d", &k);
    int A[k];

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
/*
    for (i = 0; i < k/2; i++)
    {
        b = A[i];
        if (b == n)
        {
            for (int j = 0; j < i/2; j++)
            {
                A[j] = A[i - j - 1];
                A[i - j - 1] = b;
            }
            //for (int j = k; j > i; j -= 1)
            //{
             //   A[j] = A[k - j - 1];
             //   A[k - j - 1] = b;
            //}
            break;
        }
        else
        {
            A[i] = A[k - i - 1];
            A[k - i - 1] = b;
        }
    }
 */   
    for (i = 0; i < k; i++)
        printf("%4d ", A[i]);

    printf("\n");
    return 0;
}