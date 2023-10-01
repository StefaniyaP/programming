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
    fprintf(gp, "set terminal gif\n"); 
    fprintf(gp, "set output 'b.gif'\n");
    fclose(gp);
    fclose(output);
  
    return 0;
}