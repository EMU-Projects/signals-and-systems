#include <stdio.h>

#define M 4
#define L 5
#define MIN(X, Y) (((X) < (Y)) ? (X) : (Y))
#define MAX(X, Y) (((X) < (Y)) ? (Y) : (X))

void conv(int M_order, double h[], int L_len, double x[], double* y){
    for (int i=0; i<L_len+M_order-1; i++)
    {
        int x_start = MAX(0,i-M_order+1);
        int x_end   = MIN(i+1,L_len);
        int h_start = MIN(i,M_order-1);
        for(int j = x_start; j<x_end; j++)
        {
            y[i] += h[h_start--]*x[j];
        }
    }
}

void main(){
    double h[]={ 1, 2, 3, 2 };
    double x[]={ -1, 1, 0, 2, -2 };
    double *y;
    y = (double *) calloc(L+M, sizeof(double));
    conv (M,h,L,x,y);
    printf("y[n] = [");
    for (int i=0; i<M+L-1; i++)
    	printf(" %.2lf ", y[i]);
    printf("]\n");
}

