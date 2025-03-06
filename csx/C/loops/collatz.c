#include <stdio.h>

int main(){
    int n = 26;
    while(1){
        printf("%d\n", n);
        if (n == 1){
            break;
        }
        if (n % 2 == 0){
            n = n / 2;
        } else {
            n = 3 * n + 1;
        }
    }
}