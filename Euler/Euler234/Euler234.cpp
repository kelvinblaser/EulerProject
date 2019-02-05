/*****************************************************************************
Euler 234 - Semidivisible Numbers
http://projecteuler.net/problem=234

------------------------------------------------------------------------------
First Attempt:  The interval of integers between primes[i]^2 and primes[i+1]^2
				have primes[i] as lps and primes[i+1] as ups.  One formula to 
				add all the numbers in an interval divisible by some other 
				number.  Add all numbers divisible by primes[i] and then all
				numbers divisible by primes[i+1] and then subtract two times
				all numbers divisibl by primes[i]*primes[i+1]

	Result:		Success:	1259187438574927161			Time:	52 ms
------------------------------------------------------------------------------
Kelvin Blaser		2013-10-27
*****************************************************************************/
#include <iostream>
#include <iomanip>
#include <time.h>
#include "Primes.h" // Defines number_t and test_t
using namespace std;

const number_t LIMIT = 999966663333L;
//const number_t LIMIT = 1000L;
number_t sum_between(number_t a, number_t b, number_t p);

int main() {
	int begin = clock();

	Primes primes(4000000L);
	number_t sum = 0;
	number_t p = 2;
	number_t p1, top;

	for (number_t i = 1; p*p <= LIMIT; i++) {
		p1 = primes.getPrime(i+1);
		top = ((p1*p1-1 < LIMIT) ? p1*p1-1 : LIMIT);
		sum += sum_between(p*p+1, top, p);
		sum += sum_between(p*p+1, top, p1);
		sum -= 2*sum_between(p*p+1, top, p*p1);
		p = p1;
	}

	cout << sum << endl;

	int end = clock();
	cout << endl << end - begin << endl;
	system("pause");
	return 0;
}

number_t sum_between(number_t a, number_t b, number_t p) {
	number_t x, y;
	x = a / p;
	if (x * p != a)
		x++;
	y = b / p - x;
	return p*(x*(y+1) + (y*(y+1))/2);
}