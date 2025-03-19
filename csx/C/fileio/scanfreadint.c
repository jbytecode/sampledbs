#include<stdio.h>

int main() {
    int age;

    printf("Enter your age: ");
    scanf("%d", &age);

    if(age < 18) {
        printf("You are a minor.\n");
    } else {
        printf("You are an adult.\n");
    }
}