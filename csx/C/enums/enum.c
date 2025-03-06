#include<stdio.h>

typedef enum {
    SUNDAY,
    MONDAY,
    TUESDAY,
    WEDNESDAY,
    THURSDAY,
    FRIDAY,
    SATURDAY
} Day;

int main(){
    Day today = WEDNESDAY;

    switch(today){
        case SUNDAY:
            printf("It's Sunday\n");
            break;
        case MONDAY:
            printf("It's Monday\n");
            break;
        case TUESDAY:
            printf("It's Tuesday\n");
            break;
        case WEDNESDAY:
            printf("What a week, huh?\n");
            break;
        case THURSDAY:
            printf("It's Thursday\n");
            break;
        case FRIDAY:
            printf("It's Friday\n");
            break;
        case SATURDAY:
            printf("It's Saturday\n");
            break;
        default:
            printf("Invalid day\n");
    }
    return(0);
}

