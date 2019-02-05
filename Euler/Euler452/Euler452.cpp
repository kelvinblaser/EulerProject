/*****************************************************************************
Euler 452 - Long Products
http://projecteuler.net/problem=452

------------------------------------------------------------------------------
First Attempt:  Sieve Method
    It works but I need more memory.
	Tweaked the vector a bit.  I only need to store odd numbers less than half
	of m. The odd numbers above m/2 are taken care of by a boolean vector.
	Result:	345558983				Time:	40 s
------------------------------------------------------------------------------
Kelvin Blaser		2013-12-28
*****************************************************************************/
#include <iostream>
#include <iomanip>
#include <time.h>
#include <vector>
using namespace std;

const long long MOD = 1234567891;
const long long MAX = 1000000000;

long long gcd(long long a, long long b);

int main() {
	int begin = clock();

	// Create binomial coefficients
	int num_coeffs = 0;
	int n = MAX;
	while (n > 0) {
		n /= 2;
		num_coeffs++;
	}
	vector<long long> nums(num_coeffs + 1);
	vector<long long> dens(num_coeffs + 1);
	vector<long long> c(num_coeffs + 1, 1);
	for (int i = 0; i <= num_coeffs; i++) {
		nums[i] = MAX + i - 1;
		dens[i] = i;
	}
	long long g; // gcd
	for (int i = 1; i <= num_coeffs; i++) {
		for (int j = 1; j <= i; j++) {
			g = gcd(nums[j], dens[i]);
			nums[j] /= g;
			dens[i] /= g;
		}
		for (int j = 1; j <= i; j++) {
			c[i] *= nums[j];
			c[i] %= MOD;
		}
	}

	// Debug - Seems to be working
	//for (int i = 0; i <= num_coeffs; i++) 
	//	cout << setw(2) << i << "  " << c[i] << endl;

	// Sieve
	//vector<int> sieve(MAX+1,1);]
	//cout << sizeof(num_coeffs) << endl;
	vector<int> sieve((MAX/2+1)/2, 1);
	vector<bool> visited((MAX+1)/2 - (MAX/2+1)/2, false);
	int bool_ix_offset = (MAX/2+1)/2;
	//int* sieve = new int[(MAX/2+1)/2];
	//int sieve[(MAX)+1/2];
	//vector<int> sieve((MAX+1)/2);
	long long temp;

	// Visit all of the even numbers (Not included in vectors)
	int nn = 1;
	for (int pow2 = 2; pow2 <= MAX; pow2*=2) {
		for (int i = 0; i < (MAX/pow2 + 1)/2; i++) {
			temp = sieve[i];
			temp += c[nn];
			temp %= MOD;
			sieve[i] = temp;
		}
		nn++;
	}
	

	// Go through each prime and sieve
	for (int n = 3; n <= MAX/2; n+=2) {
		int ix = (n-1)/2;
		if (sieve[ix] < 0)
			continue;
		for (int jx = ix; jx <= (MAX-1)/2; jx += n) {
			if (jx < (MAX/2+1)/2) {
				if (sieve[jx] < 0)
					continue;
				temp = sieve[jx];
				sieve[jx] = -1;
			}
			else {
				if (visited[jx-bool_ix_offset])
					continue;
				temp = 1;
				visited[jx-bool_ix_offset] = true;
			}
			int m = 2*jx+1;
			int num_factors = 0;				
			while (m%n == 0) {
				m /= n;
				num_factors++;
			}
			temp *= c[num_factors];
			temp += sieve[(m-1)/2];
			temp %= MOD;
			sieve[(m-1)/2] = temp;
		}
	}
	// Go through the final primes in the bool vector
	long long tuples = sieve[0];
	for (int i = 0; i < visited.size(); i++)
		if (!visited[i]) {
			tuples += c[1];
			tuples %= MOD;
		}
	cout << "Tuples: " << tuples;

	int end = clock();
	cout << endl << end - begin << endl;
	system("pause");
	return 0;
}

long long gcd(long long a, long long b) {
	long long temp;
	while (b > 0) {
		temp = b;
		b = a % b;
		a = temp;
	}
	return a;
}