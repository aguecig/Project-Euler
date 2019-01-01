#include <stdio.h>

int main() {
	int a = 1;
	int b = 2;
	int i;
	int sum = 2;
	int fib[33] = {a,b};
	for(i = 2; i < 34; i++) {
		fib[i] = fib[i-1] + fib[i-2];
		if(fib[i] % 2 == 0) {
			sum = sum + fib[i];
		}
	}
	printf("%d",sum);
	return 0;
}