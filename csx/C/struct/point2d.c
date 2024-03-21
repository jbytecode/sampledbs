#include <stdio.h>

typedef struct {
    int x;
    int y;
} Point2D;

void print_point2d(Point2D *p){
    printf("(%d, %d)\n", p->x, p->y);
}

void sum_point2d(Point2D *p1, Point2D *p2, Point2D *result){
    result->x = p1->x + p2->x;
    result->y = p1->y + p2->y;
}

int main(){
    Point2D p1 = {5, 7};
    Point2D p2 = {3, 2};
    Point2D result;
    sum_point2d(&p1, &p2, &result);
    print_point2d(&result);
    return 0;
}