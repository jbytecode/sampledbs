#include<stdio.h>
#include<stdlib.h>

double sum(double *x, int len){
    double sum = 0;
    for (int i = 0; i < len; i++){
        sum += x[i];
    }
    return sum;
}

double average(double *x, int len){
    double sumx = sum(x, len);
    return sumx / len;
}

int main(){
    double *values = malloc(8 * sizeof(double));
    values[0] = 9;
    values[1] = 67;
    values[2] = -1;
    values[3] = 0;
    values[4] = 10;
    values[5] = 3;
    values[6] = 99;
    values[7] = 101;
    int len = 8;
    double avg = average(values, len);
    printf("Average value: %f\n", avg);
    free(values);
}