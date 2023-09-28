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