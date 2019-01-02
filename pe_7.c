#include <stdio.h>

int main() {
	int n = 10001;  //enter the nth prime you wish to find. Note the larger
	int count = 2;	// the value, the longer the program takes.
	int candidate = 5;
	int i;
	int primality;

	while (count < n) {  
		primality = 1;
		for(i = 3; i < candidate; i+= 2) {
			if(candidate%i == 0) {
				primality = 0;
				continue;
			}
		}
		if(primality == 1) {
			count = count + 1;
		}
		candidate = candidate + 2;
	}
	int last_prime = candidate - 2;
	printf("%d",last_prime);
	return 0;
}