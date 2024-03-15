#include <stdio.h>
#include <string.h>

typedef struct Person {
    char name[50];
    int age;
    float salary;
} Person;


void person_print(Person *person){
    printf("Name: %s\n", person->name);
    printf("Age: %d\n", person->age);
    printf("Salary: %.2f\n", person->salary);
}

void person_set_name(Person *person, char *name){
    strcpy(person->name, name);
}

void person_set_age(Person *person, int age){
    person->age = age;
}

void person_set_salary(Person *person, float salary){
    person->salary = salary;
}

int main() {
    Person person = {"John", 25, 1000.0};
    person_print(&person);

    person_set_age(&person, 30);
    person_print(&person);

    person_set_age(&person, 35);
    person_print(&person);          

    return 0;
}
