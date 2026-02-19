#include<stdio.h>

int main(){
	double a, b, c, delta;
	printf("Enter a: ");
	scanf("%lf", &a);
	printf("Enter b: ");
	scanf("%lf", &b);
	printf("Enter c: ");
	scanf("%lf", &c);
	delta = b*b - 4*a*c;
	printf("Delta: %lf\n", delta);
	return 0;
}
