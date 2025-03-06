#include <stdio.h>

int main(){
    int a;
    printf("Enter a number: ");
    scanf("%d", &a);
    
    switch(a){
        case 1:
            printf("a is equal to 1\n");
            break;
        case 2:
            printf("a is equal to 2\n");
            break;
        default:
            printf("a is not equal to 1 or 2\n");
    }
    return 0;
}