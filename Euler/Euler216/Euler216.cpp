/*****************************************************************************
Euler 216 - Investigating the Primality of Numbers of the Form 2n^2-1
http://projecteuler.net/problem=216

------------------------------------------------------------------------------
First Attempt:  Brute force primality testing with Miller-Rabin.  

	Result:		Failure:			Time:	20 min.
------------------------------------------------------------------------------
Second Attempt: Find all primes less than sqrt(2)*n_max.  For each prime, 
				solve the equation 2*x^2-1 = 0 mod p.  There will be 0, 1, or 
				2 solutions.  Suppose x = 2 mod 7.  Mark all numbers between 2
				and n_max that are congruent to 2 mod 7 as composite (unless
				2x^2 - 1 == 7).  Sieve through all primes.

	Result:		Success: 5437849	Time:	21.2 s
------------------------------------------------------------------------------
Kelvin Blaser		2013-09-03
*****************************************************************************/
#include <iostream>
#include <iomanip>
#include <time.h>
#include "Primes.h" // Defines number_t and test_t
#include <vector>

using namespace std;
const number_t N_MAX = 50000000;

number_t tonelli_shanks(number_t n, number_t p);

int main() {
	int begin = clock();

	double prime_max = sqrt(2.0) * N_MAX;
	Primes primes((number_t) (1.1 * prime_max));
	vector<bool> prime_form(N_MAX+1);
	number_t count = 0;
	
	// Start with all true except 0 and 1
	for (number_t i = 2; i <= N_MAX; i++)
		prime_form[i] = true;
	prime_form[0] = prime_form[1] = false;

	// For each prime p, solve 2x^2-1 = 0 mod p
	// Then sieve out the solutions.
	number_t p, root;
	for (number_t i = 2; (p=primes.getPrime(i)) <= prime_max; i++) 
		if (primes.modExp((p+1)/2, (p-1)/2, p) == 1) { 
			// There is a solution; solve it
			root = tonelli_shanks((p+1)/2, p);
			if (root > p / 2)
				root = p - root;
			// Sieve
			if (2*root*root - 1 != p)
				prime_form[root] = false;
			for (number_t i = root+p; i <= N_MAX; i += p)
				prime_form[i] = false;
			root = p - root;
			for (number_t i = root; i <= N_MAX; i += p)
				prime_form[i] = false;
		}

	// Count the primes.
	for (number_t i = 2; i <= N_MAX; i++)
		if (prime_form[i])
			count++;

	cout << count << endl;

	int end = clock();
	cout << endl << end - begin << endl;
	system("pause");
	return 0;
}

// Algorithm from http://en.wikipedia.org/wiki/Tonelli%E2%80%93Shanks_algorithm
number_t tonelli_shanks(number_t n, number_t p) {
	Primes primes;

	// 1. Write p-1 = q*2^s
	int s = 0;
	number_t q = p-1;
	while (q%2 == 0){
		s++;
		q /= 2;
	}

	// If s==1, then the solution is n^((p+1)/4)
	if (s == 1)
		return primes.modExp(n, (p+1)/4, p);

	// 2. Find z such that z^((p-1)/2) == -1 mod p  and set c = z^q
	number_t z = 1;
	while(primes.modExp(z, (p-1)/2, p) != p-1)
		z++;
	number_t c = primes.modExp(z, q, p);

	// 3. Set r = n^((Q+1)/2) and t = n^Q  mod p
	number_t r = primes.modExp(n, (q+1)/2, p);
	number_t t = primes.modExp(n, q, p);
	number_t m = s;

	// 4. Loop until t == 1
	number_t b, i, xx, temp;
	while (t != 1) {
		i = 0;
		xx = t;  // xx = t^(2^i)
		while (xx != 1) {
			xx *= xx;
			xx %= p;
			i++;
		}
		temp= i;
		i = m-i-1;
		m = temp;
		b = c;
		for (; i > 0; i--) {
			b *= b;
			b %= p;
		}
		r *= b;
		r %= p;
		t *= b;
		t %= p;
		t *= b;
		t %= p;
		c = b*b;
		c %= p;
	}
	return r;
}