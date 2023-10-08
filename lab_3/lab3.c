#include <stdio.h>
#include <stdlib.h>

int main()
{
    int n, i = -1, s;
    int* arr = (int*)malloc(sizeof(int));
    int size = 1;
    
    printf("Enter n < 100: ");
    scanf("%d", &n);
    printf("Enter s(start of a set) < 101: ");
    scanf("%d", &s);
    
    while (i < 101)
    {
        i += 1;
       
        if (i <= n && s <= n)
        {   
            for (int j = n - 1; j >= s; j -= 1)
            {
                arr[size - 1] = j;
                size++;
                arr = (int*)realloc(arr, size * sizeof(int));
            }

            for (int j = 100; j > n; j -= 1)
            {
                arr[size - 1] = j;
                size++;
                arr = (int*)realloc(arr, size * sizeof(int));
            }

            for (int j = 0; j < size - 1; j++)
            {   
                if (j == n - s)
                    printf("%d - n\n", n); 
                printf("%d\n", arr[j]);                      
            }
            free(arr);
            break;
        }

        else
        {   
            for (int j = 100; j >= s; j -= 1)
            {
                arr[size - 1] = j;
                size++;
                arr = (int*)realloc(arr, size * sizeof(int));
            }

            for (int j = 0; j < size - 1; j++)
            {   
                printf("%d\n", arr[j]);
            }
            free(arr);
            break;
        }
    }
    
    return 0;
}
