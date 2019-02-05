/*****************************************************************************
Euler 127 - abc-hits
http://projecteuler.net/problem=127

------------------------------------------------------------------------------
First Attempt:  Brute Force
	Result   :  Correct answer for MAX = 1000, but takes way too long for
				120000.
------------------------------------------------------------------------------
Second Attempt:	Precalculate the radicals.  Note that
			1. gcd(a,b)=gcd(b,c)=gcd(a,c)=1 ==> rad(abc) = rad(a)rad(b)rad(c)
			2. rad(abc) < c ==> rad(c) < c ==> c is squareful
			3. 1 and 2 ==> rad(a)rad(b) < c / rad(c)

	Result	:	Success.  Solution: 18407904	Time:  4655 ms
------------------------------------------------------------------------------
Kelvin Blaser		2013-07-28
*****************************************************************************/
#include <iostream>
#include <iomanip>
#include <time.h>
#include "../Euler/Utilities.h"
#include "../Euler/Primes.h"

using namespace std;
const int MAX = 120000;

long rad(int a, int b, int c, Primes& primes);
int rad(int n, Primes& primes);
long attempt1();
long attempt2();

int main(){
	int begin = clock();
	
	attempt2();

	int end = clock();
	cout << endl << end - begin << endl;
	system("pause");
	return 0;
}

// Not needed
long rad(int a, int b, int c, Primes& primes)
{
	long r = 1;
	int p;

	for (int i = 1; i <= primes.numPrimes() && primes.getPrime(i) <= c; i++)
	{
		p = primes.getPrime(i);
		if (a % p == 0 || b % p == 0 || c % p == 0)
			r *= primes.getPrime(i);
		if (r >= c)
			return r;
	}
	return r;
}

// Failed Attempt
long attempt1()
{
	int a, b, c;
	long sum  = 0;
	int count = 0;

	Primes primes(MAX);

	for (c = 3; c < MAX; c++)
	{
		for (a = 1; a < c/2; a++)
			if (gcd(a, c) == 1)
			{
				b = c - a;
				if (gcd(a, b) == 1 && gcd(b,c) == 1)
					if (rad(a,b,c, primes) < c)
					{
						sum += c;
						count++;
						cout << setw(10) << a
							<< setw(10) << b
							<< setw(10) << c << endl;
					}
			}
	}

	cout << sum << " " << count << endl;
	return sum;
}

int rad(int n, Primes& primes)
{
	int N = n;
	int r = 1;
	int p;

	for (int i = 1; (p = primes.getPrime(i)) <= N; i++)
	{
		if (N%p == 0)
		{
			r *= p;
			while (N%p == 0)
				N /= p;
		}
	}

	return r;
}

long attempt2()
{
	int rads[MAX+1];

	Primes primes(MAX);

	// Compute the radicals
	for (int i = 1; i <= MAX; i++)
		rads[i] = rad(i, primes);

	int a, b, c;
	long sum  = 0;
	int count = 0;
	for (c = 3; c <= MAX; c++)
		if (rads[c] < c)
		{
			int remain = c / rads[c];  // rad(a)rad(b) < remain		==>		rad(a) < remain
			for (a = 1; a < c/2; a++)
				if (rads[a] < remain && gcd(c,a) == 1)
				{
					b = c - a;
					if (rads[b]*rads[a] < remain)
					{
						sum += c;
						count ++;
					}
				}
		}

	cout << sum << " " << count << endl;
	return sum;
}