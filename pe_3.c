#include <stdio.h>

int main() {
	long long int n = 600851475143; //enter integer to be factored here
	long long int factor;
	long long int lastfactor;

	if(n%2 == 0) {
		n = n/2;
		lastfactor = 2;
		while(n%2 == 0) {
			n = n/2;
		}
	}
	else {
		lastfactor = 1;
	}
	factor = 3;
	while(n > 1) {
		if(n%factor == 0) {
			n = n/factor;
			lastfactor = factor;
			while(n%factor == 0) {
				n = n/factor;
			}
		}
		factor = factor + 2;
	}
	printf("%d",lastfactor);
	return 0;
	}