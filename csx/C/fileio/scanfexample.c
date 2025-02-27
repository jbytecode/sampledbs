#include <stdio.h>
#include <string.h>

int main() {
    char c[20];
    
    printf("Enter some text: ");
    scanf("%s", c);
    
    printf("You entered: %s\n", c);
    printf("Length: %ld\n", strlen(c));
    return 0;
}
