#include "Utilities.h"
using namespace std;

long gcd(long a, long b)
{
	long temp;
	while (b != 0)
	{
		temp = a % b;
		a = b;
		b = temp;
	}

	return a;
}

long long modExp(long a, unsigned long exp, long long modder)
{
	if (exp == 0)
		return 1;
	if (exp == 1)
		return a % modder;

	long long root = modExp(a, exp/2, modder);
	root *= root;
	root %= modder;

	if (exp % 2)
	{
		root *= a;
		root %= modder;
	}
	return root;
}