#pragma once
#include <vector>
#include <iostream>
using namespace std;

class Primes
{
	static vector <bool> primes;
	static vector <long> primeNums;
	static long limit; // The largest number tested
	long localLimit;


public:
	Primes(void);
	Primes(long newLimit);
	~Primes(void);

	void runSieve(long newLimit);
	void setNewLimit(long newLimit);

	bool isPrime(long long num);

	void showPrimes(ostream& out = cout);
	long getPrime(long index);
	long getLimit(){ return localLimit; }
};
