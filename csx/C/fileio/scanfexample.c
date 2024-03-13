#include <stdio.h>

int main() {
    char c[20];
    
    printf("Enter some text: ");
    scanf("%s", &c);
    
    printf("You entered: %s\n", c);
    printf("Length: %d\n", strlen(c));
    return 0;
}
