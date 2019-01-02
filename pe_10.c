    #include <stdio.h>  //long run time for 2 000 000, probably 10 minutes or so

    int main (void)
    {
        long long p, d;
        _Bool is_prime;
	long long sum = 5;
        for (p = 5; p <=2000000 ; p+=2)
        {
            is_prime = 1;

            for (d = 3; d < p; d+=2)
                if (p % d == 0){
                    is_prime = 0;
		    break;
		}   

                if (is_prime)          // or if (is_prime != 0); same
                    sum = sum + p;
        }

        printf ("%lld",sum);
        return 0;
    }