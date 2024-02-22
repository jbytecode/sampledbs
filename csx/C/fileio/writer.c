#include <stdio.h>

int main()
{
    FILE *myfile = fopen("content.txt", "w");

    int a = 1234;
    double b = 3.14159265;

    fwrite(&a, sizeof(a), 1, myfile);
    fwrite(&b, sizeof(b), 1, myfile);

    fclose(myfile);

    return 0;
}

