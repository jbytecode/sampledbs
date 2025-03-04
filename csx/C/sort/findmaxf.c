#include<stdio.h>

int findmax(int *vals, int len){
    int max = vals[0];
    for (int i = 1; i < len; i++){
        if (vals[i] > max){
            max = vals[i];
        }
    }
    return max;
}
int main(){
    int values[] = {9, 67, -1, 0, 10, 3, 99, 101};
    int len = sizeof(values) / sizeof(int);
    int max = findmax(values, len);
    printf("Max value: %d\n", max);
}
