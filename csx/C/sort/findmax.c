#include<stdio.h>

int main(){
    int values[] = {9, 67, -1, 0, 10, 3};
    int len = 6;
    int max = values[0];
    for (int i = 1; i < len; i++){
        if (values[i] > max){
            max = values[i];
        }
    }
    printf("Max value: %d\n", max);
}