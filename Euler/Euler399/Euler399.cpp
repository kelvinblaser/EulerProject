/*****************************************************************************
Euler 399 - Square-Free Fibonacci Numbers
http://projecteuler.net/problem=399

------------------------------------------------------------------------------
First Attempt:  
	Most of the time is spent finding the last 16 digits.  If I had a 128 bit
	integer type, I could find the nth fibonacci number in O[log(n)] time 
	rather than O[n] and it would only take about 2 seconds for the sieve.
	As it is, I can't multiply two 16 digit numbers and guarantee that it will
	fit in a 64 bit integer.

	Result:	1508395636674243,6.5e27330467		Time:	9s

Second Attempt:  2014-11-29
	Used Boost's 128 bit integer type.  Gets the answer in under 2 seconds 
	now.  w00t!!  I should also report that I am now an ultimate decimator.
------------------------------------------------------------------------------
Kelvin Blaser		2014-11-28
*****************************************************************************/
#include <iostream>
#include <iomanip>
#include <time.h>
#include <vector>
#include <cmath>
#include <stdint.h>
#include "Primes.h"
#include <boost/multiprecision/cpp_int.hpp>
#include <utility> // For pair
using namespace std;
typedef boost::multiprecision::int128_t int128_t;
typedef pair<int128_t, int128_t> fibPair;

const double RT5 = sqrt(5.0);
const double PHI = (1. + RT5)/2.;
const double LOGPHI = log(PHI);

class Euler399 {
	int calcPMax();
	int fibPeriod(int p);
	void sieveSqrFree();
	int countNthIx();
	int128_t fibLast16(int ix);
	fibPair _fibMod(int n, long long MOD);

	int N, pMax;
	int128_t last16;
	double nthSqrFree;
	vector<bool> sqrFreeFib;
	Primes primes;

public:
	Euler399(int NN);
};

Euler399::Euler399(int NN) {
	N = NN;
	pMax = calcPMax();
	primes.setNewLimit(pMax);
	cout << "Primes up to " << pMax << " calculated.\n";
	sieveSqrFree();
	cout << "Square-free Fibonacci numbers sieved.\n";
	int ix = countNthIx();
	cout << ix << endl;
	last16 = fibLast16(ix);
	//nthSqrFree = pow(PHI,N/2) / RT5;
	double logf = ix * log10(PHI) - log10(RT5);
	int exponent = int(logf);
	double mantissa = pow(10.,logf - exponent);
	cout << last16 << ',' << setprecision(2) << 
		mantissa << 'e' << exponent << "\n\n";
}

int Euler399::calcPMax() {
	double plast = 0.;
	double p = 3*N/2;
	double diff = p;
	double log5p;
	const double NLOGPHI = 3*N*LOGPHI/2;

	while (diff > 0.05 || diff < -0.05) {
		log5p = log(RT5*p);
		diff = (p*log5p - NLOGPHI)*RT5/(1+RT5*log5p);
		p = p - diff;
	}

	return int(p);
}

int Euler399::fibPeriod(int p) {
	int fLast = 1;
	int fNow = 1;
	int T = 2;
	int temp;
	int NN = 3*N/2;
	long long p2 = long long (p) * long long (p);

	while (fNow != 0 && T <= NN/p && T <= p2) {
		T++;
		temp = fNow;
		fNow = (fLast + fNow) % p;
		fLast = temp;
	}

	if (T >= NN/p || T > p2) 
		return 0;

	return T;
}

void Euler399::sieveSqrFree() {
	int p,p2Period; 
	int NN = 3*N/2;

	sqrFreeFib.resize(NN, true);
	for (int i = 0; i < primes.numPrimes(); i++) {
		p = primes[i];
		p2Period = p * fibPeriod(p);
		if (p2Period && p2Period < NN)
			for (int j=p2Period; j < NN; j+=p2Period)
				sqrFreeFib[j] = false;
	}
	return;
}

int Euler399::countNthIx() {
	int count = 0;
	int ix = 1;
	while (count < N) {
		if (sqrFreeFib[ix])
			count += 1;
		ix++;
	}
	return ix-1;
}

int128_t Euler399::fibLast16(int ix) {
	// Slower method with O[n] time complexity
	/*long long fLast = 1;
	long long fNow = 1;
	long long temp;
	const long long MOD = 10000000000000000LL;
	for (int jx = 2; jx < ix; jx++) {
		temp = fNow;
		fNow = (fLast + fNow)%MOD;
		fLast = temp;
	}
	return fNow;*/  

	// Faster method with O[log n] time complexity.  Requires 128 bit int type
	const long long MOD = 10000000000000000LL;
	int128_t f = _fibMod(ix,MOD).first;
	while (f < 0)
		f += MOD; // % operator returns negative values for negative input
	return f;
}

fibPair Euler399::_fibMod(int n, long long MOD) {
	if (n==0) 
		return fibPair(0,1);
	fibPair next = _fibMod(n/2, MOD);
	int128_t a = next.first;
	int128_t b = next.second;
	int128_t c = (a*(2*b-a))%MOD;
	int128_t d = (b*b + a*a)%MOD;
	if (n%2 == 0)
		return fibPair(c,d);
	return fibPair(d,(c+d)%MOD);
}

int main() {
	int begin = clock();

	Euler399(200);
	Euler399(100000000);

	int end = clock();
	cout << endl << end - begin << endl;
	system("pause");
	return 0;
}