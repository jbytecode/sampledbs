#include <stdio.h>
#include <stdlib.h>

int main(){
    // Allocation dynamic memory
    int *values = (int *)malloc(8 * sizeof(int));
    values[0] = 9;
    values[1] = 67;
    values[2] = -1;
    values[3] = 0;
    values[4] = 10;
    values[5] = 3;
    values[6] = 99;
    values[7] = 101;
    int len = 8;
    for (int i = 0; i < len; i++){
        printf("%d\n", values[i]);
    }
    // Freeing dynamic memory
    free(values);
}