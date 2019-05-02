#include <stdio.h>

int main() {
	// There is not much to program here besides the actual number,
	// we leave it to reason how to come up with the actual value.

	// Start by understanding that this least number must have every 
	// prime less than 20 as a divisor:

	// Primes: 19*17*13*11*7*5*3*2

	// Now we start adding in composite numbers starting from 4, but 
	// doing so by multiplying the existing number by primes. So:

	// 19*17*13*11*7*5*3*2*(2)

	// so now 4 is included. The next number is six, but notice how it
	// is already included because (2)(3) = 6. Eight is the next number that 
	// actually needs to be added in.

	// 19*17*13*11*7*5*3*2*(2)*(2)
	
	// nine is next

	// 19*17*13*11*7*5*3*2*(2)*(2)*(3)

	// ten is included (5)(2), twelve is included (2)(2)(3), fourteen is 
	// included (7)(2). Fifteen is included (5)(3). sixteen needs to be 
	// added

	// 19*17*13*11*7*5*3*2*(2)*(2)*(3)*(2)
	
	// eighteen is included (3)(3)(2). twenty is included (2)(2)(5)

	int value = 19*17*13*11*7*5*3*2*2*2*3*2;

	printf("%d",value);
	return 0;
}

