#include<stdio.h>

int main(){

    FILE* myfile = fopen("content.txt", "r");

    int a;
    double b;

    fread(&a, sizeof(int), 1, myfile);
    fread(&b, sizeof(double), 1, myfile);

    fclose(myfile);

    printf("We get integer value of: %d\n", a);
    printf("We get double value of: %lf\n", b);

    return 0;
}


