#include <stdio.h>

/*
    The recursive implementation is not that efficient (why?).
    Try to write a non-recursive version of the 
    same function.
*/
int factorial(int n){
    if (n == 0){
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
