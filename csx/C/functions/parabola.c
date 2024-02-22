#include <stdio.h>
#include <math.h>

double calculate_delta(double a, double b, double c){
    return b * b - 4.0 * a * c;
}

double get_first_root(double a, double b, double c){
    double mydelta = calculate_delta(a, b, c);
    return (-b + sqrt(mydelta)) / (2 * a);
}

double get_second_root(double a, double b, double c){
    double mydelta = calculate_delta(a, b, c);
    return (-b - sqrt(mydelta)) / (2 * a);
}

int get_number_of_roots(double delta){
    if (delta < 0.0){
        return 0;
    }else if (delta == 0.0){
        return 1;
    }else{
        return 2;
    }
}


int main(){
    double par1 = 1.0;
    double par2 = 5.0;
    double par3 = -10;

    double delta = calculate_delta(par1, par2, par3);

    int numroots = get_number_of_roots(delta);

    printf("Number of roots: %d\n", numroots);

    if (numroots < 0){
        puts("Sorry, no real roots!");
    }else if (numroots == 1){
        puts("We have two reel roots but they are not distinct!");
        double x1 = get_first_root(par1, par2, par3);
        double x2 = x1;
        printf("x1 = %lf, x2 = %lf\n", x1, x2);
    }else{
        puts("We have two reel distinct roots!");
        double x1 = get_first_root(par1, par2, par3);
        double x2 = get_second_root(par1, par2, par3);
        printf("x1 = %lf, x2 = %lf\n", x1, x2);
    }
    return 0;
}