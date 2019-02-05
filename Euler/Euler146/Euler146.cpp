/*****************************************************************************
Euler 146 -		Investigating a Prime Pattern
http://projecteuler.net/problem=146

------------------------------------------------------------------------------
First Attempt:  I know n must be even and divisible by 5, so only check n 
				which are divisible by 10.  The odd numbers have the following
				pattern:       p p c p p c p c c c c c c p
				divisible by:      3     3     3     3    
								   5         5         5
				I only need to check n^2+19 and n^2+12 for compositness.

				Brute Force 
	Result:     Failure.  After an hour it had only made it to 26,000,000
------------------------------------------------------------------------------
Second Attemp:	Most of the time was spent checking for primality.  Need to 
				find a faster primality test.  Implement a deterministic 
				Miller-Rabin test.

	Result:		Success:					Time:	2656ms (Better solutions out 
													there)
------------------------------------------------------------------------------
Kelvin Blaser		2013-08-17
*****************************************************************************/
#include <iostream>
#include <iomanip>
#include <time.h>
#include <cmath>
#include <Utilities.h>
using namespace std;

bool patternSat(unsigned long long n);
bool millerRabin(unsigned long long num);

int main(){
	int begin = clock();

	const long MAX = 150000000L;
	long long sum = 0;

	for (unsigned long long n = 10; n < MAX; n+=10) {
		if (n % 100000 == 0)
			cout << n << endl;
		if (patternSat(n)) {
			cout << setw(10) << n << setw(14) << sum << endl;
			sum += n;
		}
	}

	cout << patternSat(345410) << endl;

	cout << sum << endl;

	int end = clock();
	cout << endl << end - begin << endl;
	system("pause");
	return 0;
}

bool patternSat(unsigned long long n) {
	unsigned long long n2 = n * n;
	if (!millerRabin(n2+1))
		return false;
	if (!millerRabin(n2+3))
		return false;
	if (!millerRabin(n2+7))
		return false;
	if (!millerRabin(n2+9))
		return false;
	if (!millerRabin(n2+13))
		return false;
	if (millerRabin(n2+19))
		return false;
	if (millerRabin(n2+21))
		return false;
	if (!millerRabin(n2+27))
		return false;
	return true;
}

bool millerRabin(unsigned long long num) {
	if (num <= 1)
		return false;
	if (num == 2)
		return true;
	if (num % 2 == 0)
		return false;

	int s = 0;
	unsigned long long d = num-1;
	while (d%2==0) {
		s++;
		d /= 2;
	}

	int as[] = {2, 3, 5, 7, 11, 13, 17};
	bool passed = false;
	for (int i = 0; i < 7; i++) {
		if (as[i] <= num-1) {
			if (modExp(as[i], d, num) == 1)
				passed = true;
			unsigned long long two_to_r = 1;
			for (int r = 0; r < s; r++)
			{
				if (modExp(as[i], two_to_r * d, num) == num-1)
					passed = true;
				two_to_r *= 2;
			}
			if (!passed)
				return false;
		}
	}
		
	return true;
}