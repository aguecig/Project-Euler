#include <stdio.h>

int main() {
	int a = 1;
	int b = 2;
	int count = 2;
	int sum;
	int temp;

	while(sum < 4000000) {
		temp = b;
		b = a + b;
		a = temp;
		count = count + 1;
		sum = b;
	}
	printf("%d",count);
	return 0;
		
}

// This program when run has told us that the number of terms in the 
// fibonacci sequence that are below 4,000,000 are the first 33 terms. 
// You can see this by running the program and observing the output.