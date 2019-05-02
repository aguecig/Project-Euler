#include <stdio.h>

main() {
	int i = 1;
	int sum = 0;
	while(i < 1000) {
		if(i % 15 == 0) {
			sum = sum + i;
			i++;
		}
		else if(i % 5 == 0) {
			sum = sum + i;
			i++;
		}
		else if(i % 3 == 0) {
			sum = sum + i;
			i++;
		}
		else {
		i++;
		continue;
		}
	}
	printf("%d",sum);
	return 0;
}