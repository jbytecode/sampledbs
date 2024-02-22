#include <stdio.h>

int main(){

    double a = 1.0;
    double b = -5.0;
    
    double mysum      = a + b;
    double mydiff     = a - b;
    double myproduct  = a * b;
    double mydivision = a / b;

    int equality            = (a == b);
    int lessthan            = (a < b);
    int greaterthan         = (a > b);
    int lessorequalthan     = (a <= b);
    int greaterorequalthan  = (a >= b);
    int notequal            = (a != b);

    printf("a + b    = %lf\n", mysum);
    printf("a - b    = %lf\n", mydiff);
    printf("a * b    = %lf\n", myproduct);
    printf("a / b    = %lf\n", mydivision);

    printf("a == b   => %d\n", equality);
    printf("a < b    => %d\n", lessorequalthan);
    printf("a > b    => %d\n", greaterthan);
    printf("a <= b   => %d\n", lessorequalthan);
    printf("a >= b   => %d\n", greaterorequalthan);
    printf("a != b   => %d\n", notequal);

    return 0;
}