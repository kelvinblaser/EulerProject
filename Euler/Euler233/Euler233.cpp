/*****************************************************************************
Euler 233 - Almost Right-Angled Triangles I
http://projecteuler.net/problem=233

------------------------------------------------------------------------------
First Attempt:  
	
------------------------------------------------------------------------------
Kelvin Blaser		2015-02-08
*****************************************************************************/
#include <iostream>
#include <iomanip>
#include <time.h>
#include <cmath> // For sqrt
#include <stdint.h>
#include "Primes.h"
//#include <boost/multiprecision/cpp_int.hpp>
#include <utility> // For pair
#include <vector>
#include <set>
#include <unordered_set>
using namespace std;
//typedef boost::multiprecision::int128_t int128_t;
//typedef pair<int128_t, int128_t> fibPair;
typedef int64_t int_t;
typedef pair<int_t, int_t> IntPair;
typedef vector<vector<IntPair>> PrimeFactorization;

int_t Euler223(const int_t N);
int_t Euler223a(const int_t N);
vector<IntPair> calcPrimeFact(const int_t n, Primes& primes);
void primeFactorizations(int_t n, PrimeFactorization& primeFactors);
set<int_t> cartProduct(const set<int_t> s1, const set<int_t> s2);
set<int_t> divisorsFromPrimes( vector<IntPair> primeFact);

int main() {
	int begin = clock();

	cout << Euler223a(100) << " almost right-angled triangles less than " 
		<< 100 << endl;
	cout << Euler223(2500000) << " almost right-angled triangles less than " 
		<< 2500000 << endl;
	//cout << (IntPair(3,0) < IntPair(3,1)) << endl;

	int end = clock();
	cout << endl << end - begin << endl;
	system("pause");
	return 0;
}

int_t Euler223(const int_t N) {
	PrimeFactorization primeFact(N/3+2);
	primeFactorizations(N/3+1, primeFact);

	//unordered_set<IntPair> triangles;
	//set<IntPair> triangles;
	//vector<set<int_t>> triangles(N/3+1);
	set<int_t> divs;
	set<int_t>::iterator it;
	int_t x,y,b,aa,bb;
	int_t ans = 0;
	//vector<IntPair> pf_minus;// = primeFact[a-1];
	//vector<IntPair> pf_plus; // = primeFact[a+1];
	vector<IntPair> pf_twos(1);
	pf_twos[0] = IntPair(2,0);
	for (int_t a = 2; a <= N/3; a++) {
		if (a % 10000 == 0)
			cout << setw(9) << a << "/" << N/3 << setw(12) 
			<< ans << endl; //triangles.size() << endl;
		vector<IntPair> pf_minus(primeFact[a-1]);
		vector<IntPair> pf_plus(primeFact[a+1]);
		pf_twos[0].second = 0;
		if (a%2) {
			pf_twos[0].second += pf_minus[0].second + pf_plus[0].second;
			pf_minus[0].second = 0;
			pf_plus[0].second = 0;
		}
		//else 
		//	pf_twos[0] = IntPair(2,0);
		divs = divisorsFromPrimes(pf_twos);
		divs = cartProduct(divs, divisorsFromPrimes(pf_minus));
		divs = cartProduct(divs, divisorsFromPrimes(pf_plus));
		for (it = divs.begin(); it != divs.end(); it++) {
			x = *it;
			y = (a*a-1) / x;
			b = (y-x)/2;
			if (a > b)
				break;
			if (x%2 != y%2)
				continue;
			if (a+y <= N) {
				//if (a < b) {
				//	aa = a; bb = b;
				//}
				//else {
				//	aa = b; bb = a;
				//}
				//triangles.insert(IntPair(aa,bb));
				//triangles[aa].insert(bb);
				ans++;
			}
		}
	}

	//for (int i = 0; i < primeFact.size(); i++)
	//	set<int> divs = divisorsFromPrimes(primeFact[i]);

	//return triangles.size() + (N-1)/2;
	//int_t ans = 0;
	//for (int_t a = 0; a <= N/3; a++)
	//	ans += triangles[a].size();
	//return ans + (N-1)/2;

	return ans + (N-1)/2;
}

int_t Euler223a(const int_t N) {
	Primes primes(N/3+1);
	int_t triangles = 0;
	int_t x,y,b;
	set<int_t> divs;
	set<int_t>::iterator it;
	vector<IntPair> pf;
	for (int_t a = 2; a <= N/3; a++) {
		if (a % 10000 == 0)
			cout << setw(9) << a << "/" << N/3 << setw(12) 
			<< triangles << endl; //triangles.size() << endl;
		pf = calcPrimeFact(a*a-1, primes);
		divs.clear();
		divs = divisorsFromPrimes(pf);
		for (it = divs.begin(); it != divs.end(); it++) {
			x = *it;
			y = (a*a-1) / x;
			b = (y-x)/2;
			if (a > b)
				break;
			if (x%2 != y%2)
				continue;
			if (a+y <= N) {
				//if (a < b) {
				//	aa = a; bb = b;
				//}
				//else {
				//	aa = b; bb = a;
				//}
				//triangles.insert(IntPair(aa,bb));
				//triangles[aa].insert(bb);
				triangles++;
			}
		}
	}
	return triangles + (N-1)/2;
}
//
vector<IntPair> calcPrimeFact(int_t n, Primes& primes) {
	vector<IntPair> pf;
	int_t p,e;
	for (int px=0; px < primes.numPrimes();  px++) {
		p = primes[px];
		if (n < p*p) {
			pf.push_back(IntPair(n,1));
			break;
		}
		if (n%p)
			continue;
		e = 0;
		while (n%p == 0) {
			e++;
			n/=p;
		}
		pf.push_back(IntPair(p,e));
		if (n == 1)
			break;
	}
	return pf;
}

void primeFactorizations(const int_t n, PrimeFactorization& primeFactors) {
	int_t y,e,p;
	Primes primes(n);
	if (primeFactors.size() <= n)
		primeFactors.resize(n+1);
	primeFactors[0].push_back(IntPair(0,1));
	primeFactors[1].push_back(IntPair(1,1));

	for (int px = 0; px < primes.numPrimes(); px++) {
		p = primes[px];
		for (int_t x = p; x <= n; x+=p) {
			y = x; e = 0;
			while (!(y%p)) {
				e++;
				y /= p;
			}
			primeFactors[x].push_back(IntPair(p,e));
		}
	}

	return;
}

set<int_t> cartProduct(set<int_t> s1, set<int_t> s2) {
	set<int_t> res;
	set<int_t>::iterator it, jt;
	for (it = s1.begin(); it != s1.end(); it++) 
		for (jt = s2.begin(); jt != s2.end(); jt++) 
			res.insert((*it)*(*jt));
	return res;
}

set<int_t> divisorsFromPrimes( vector<IntPair> primeFact) {
	int start[] = {1};
	int_t p,e,pp;
	set<int_t> divs(start, start+1);
	set<int_t> s2;
	for (vector<IntPair>::iterator it = primeFact.begin(); 
		it != primeFact.end(); it++) {
		p = it->first; e = it->second;
		pp = 1;
		s2.clear();
		for (int i=0; i <= e; i++) {
			s2.insert(pp);
			pp *= p;
		}
		divs = cartProduct(divs, s2);
	}	
	return divs;
}