#include <stdio.h>
#include <stdlib.h>
#include <time.h>

int main(){
  
	srand((unsigned int)time(NULL));	

	int magicnumber = rand() % 100 + 1;

	int guess = 0;

	for (int try = 0; try < 10; try++){
		printf("Try %d: ", try + 1);
		scanf("%d", &guess);

		if (guess < magicnumber){
			printf("Too low!\n");
		} else if (guess > magicnumber){
			printf("Too high!\n");
		} else {
			printf("Congratulations! You found the number in %d tries!\n", try + 1);
			return 0;
		}
	}

	printf("Sorry, you've used all 10 tries. The number was %d.\n", magicnumber);
	return 0;
}

