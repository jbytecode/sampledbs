#include <stdio.h>

int main(){

    int a = 5;

    float lowprecvalue = 3.14159265;

    double highprecvalue = 3.14159265;

    char c = 'C';

    const char *somestring = "Hello, world!";

    char name[] = "C Programming Language";

    printf("Here is the integer: %d\n", a);
    
    printf("Here is the float: %0.9f\n", lowprecvalue);

    printf("Here is the double: %0.9lf\n", highprecvalue);

    printf("Here is the character: %c\n", c);

    printf("Here is the constant character array: %s\n", somestring);

    printf("Other character array: %s\n", name);

    return 0;
}