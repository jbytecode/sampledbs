/*
Heron's method for computing square roots
https://en.wikipedia.org/wiki/Methods_of_computing_square_roots
*/

#include <stdio.h>

double heronstep(double initial, double value){
    return 0.5 * (initial + value / initial);
}

double heron(double initial, double value){
    double next = heronstep(initial, value);
    while (next != initial){
        initial = next;
        next = heronstep(initial, value);
    }
    return next;
}

int main(){
    double value = 25.0;
    double initial = 1.0;
    double result = heron(initial, value);
    printf("The square root of %f is %f\n", value, result);
    return 0;
}
