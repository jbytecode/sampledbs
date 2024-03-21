#include <stdio.h>

typedef struct {
    int x;
    int y;
} Coordinate;


void print_coordinate(Coordinate *c){
    printf("(%d, %d)\n", c->x, c->y);
}


int main(){
    Coordinate c = {5, 7};
    print_coordinate(&c);
    return 0;
}