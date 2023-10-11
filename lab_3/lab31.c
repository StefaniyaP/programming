#include <stdio.h>
#include <stdlib.h>
#include <time.h>

void fill(int k, int a[])
{
    int i;
    for (i = 0; i < k; i++)
        a[i] = rand () % 31;
}



int main()
{
    srand(time(NULL));
    int k, i, n, m, A[k];
    printf("k (size of an array) -> ");
    scanf("%d", &k);

    fill(k, A);

    printf("n (unknown number) -> ");
    scanf("%d", &n);
    for (i = 0; i < k; i++)
    {
        printf("%d ", A[i]);

        if (A[i] == n) 
        {
            for (int j = i; j >= 0; j -= 1)
                printf("%d ", A[j]);

            for (int j = i + 1; j < k; j++)
                printf("%d ", A[-j]);
        }
       // else
       // {
      //      for (int j = k; j < k; j -= 1)
       //         printf("%d ", A[j]);
      //  }        
    }
    printf("\n");
    
    return 0;
}
