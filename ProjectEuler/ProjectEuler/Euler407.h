#include <iostream>
#include <mpirxx.h>

using namespace std;

mpz_class Euler407(long long limit);
long long M(long long n);

mpz_class Euler407(long long limit)
{
	mpz_class sum = 0;
	for (int i = 1; i <= limit; i++)
	{
		sum += M(i);
		if (i%10000==0)
			cout << i << ", " << sum << endl;
	}
	return sum;
}