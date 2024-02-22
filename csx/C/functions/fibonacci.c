#include <stdio.h>

int fibonacci(int n){
    if (n == 1){
        return 1;
    }else if (n == 2){
        return 1;
    }else{
        return fibonacci(n-1) + fibonacci(n-2);
    }
}


int main(){

    /*
        Use for-loops to print out more results 
        with using a shorter line of codes.
    */

    printf("Fibonacci(%d) = %d\n", 1, fibonacci(1));
    printf("Fibonacci(%d) = %d\n", 2, fibonacci(2));
    printf("Fibonacci(%d) = %d\n", 3, fibonacci(3));
    printf("Fibonacci(%d) = %d\n", 4, fibonacci(4));
    printf("Fibonacci(%d) = %d\n", 5, fibonacci(5));
    printf("Fibonacci(%d) = %d\n", 6, fibonacci(6));

    return 0;
}