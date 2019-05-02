#include <stdio.h>
#include <math.h>  // for pow function
#include <stdlib.h> // for abs function

int main() {
	int i;
	int j;
	int sum = 0;
	int square_of_sum = 0;
	int sum_of_squares = 0;
	int difference;

	for(j = 1; j < 101; j++) {
		sum = sum + j;
	}

	for(i = 1; i < 101; i++) {
		sum_of_squares = sum_of_squares + pow(i,2);
	}
	square_of_sum = pow(sum,2);
	difference = abs(sum_of_squares - square_of_sum);

	printf("%d",difference);
	return 0;
}