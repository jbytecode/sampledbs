#include <stdio.h>

void save(){
    FILE *f = fopen("test.txt", "w");
    int x[] = {1,2,3};
    fwrite(&x, sizeof(int), 3, f);
    fclose(f);
}

void load(){
    FILE *f = fopen("test.txt", "r");
    int a[3];
    fread(&a, sizeof(int), 3, f);
    for (int i = 0; i< 3; i++){
        printf("%d\n", a[i]);
    }
    fclose(f);
}

int main() {
    puts("Save");
    save();
    puts("Load");
    load();
    return 0;
}
