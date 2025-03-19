#include <stdio.h>

int main(){
    double a, b, c;

    printf("Enter three numbers: ");
    scanf("%lf %lf %lf", &a, &b, &c);

    double delta = b*b - 4*a*c;

    printf("Delta is %lf\n", delta);

    if (delta < 0) {
        printf("No real roots\n");
    } else if (delta == 0) {
        printf("One real root\n");
    } else {
        printf("Two real roots\n");
    }
}