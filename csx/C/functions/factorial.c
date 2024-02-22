#include <stdio.h>

int factorial(int n){
    if (n <= 0){
        return 1;
    }else{
        return n * factorial(n - 1);
    }
}



int main(){

    int x = 5;

    int result = factorial(x);

    printf("Factorial(%d) is %d.\n", x, result);

    return 0;
}