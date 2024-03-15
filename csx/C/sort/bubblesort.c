#include <stdio.h>

int main(){
    int len = 6;

    int values[] = {9, 67, -1, 0, 10, 3};

    for (int i = 0; i < len; i++){
        for (int j = i + 1; j < len - 1; j++){
            if (values[i] > values[j]){
                double temp = values[i];
                values[i] = values[j];
                values[j] = temp;
            }
        }
    }

    for (int i = 0; i < len; i++){
        printf("%d\n", values[i]);
    }

}