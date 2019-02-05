#pragma once
#include <vector>
#include <iostream>
#include <cmath>
//#include <boost/multiprecision/cpp_int.hpp>

using namespace std;
//typedef boost::multiprecision::int128_t test_t;
typedef long long test_t;
typedef long long number_t;

class Primes
{
	void _runSieve(number_t newLimit);

	static vector <bool> primes;
	static vector <number_t> primeNums;
	static number_t limit; // The largest number tested
	long localLimit;

public:
	Primes(void);
	Primes(number_t newLimit);
	~Primes(void);

	void setNewLimit(number_t newLimit);
	bool isPrime(test_t num);
	bool millerRabin(test_t num);

	void showPrimes(ostream& out = cout);
	number_t getPrime(number_t index);  // index starts with 1
	number_t getLimit(){ return localLimit; }
	number_t numPrimes();
	number_t operator[](number_t ix); // No bounds checking

	static test_t modExp(test_t base, number_t exp, number_t mod);
};

vector <bool> Primes::primes;
number_t Primes::limit = 0;
vector <number_t> Primes::primeNums(1);

Primes::Primes(void)
{
	primeNums[0] = 2;
	if (!limit)
	{
		primes.resize(1, true);
		_runSieve(1);
		primes[0] = false;
	}
}

Primes::Primes(number_t newLimit)
{
	primeNums[0] = 2;
	if(newLimit > limit)
	{
		primes.resize( (newLimit+1) / 2, true);
		primes[0] = false;
		_runSieve(newLimit);
	}
	
	localLimit = newLimit;
}

Primes::~Primes(void)
{
}

void Primes::_runSieve(number_t newLimit)
{
	number_t size = primes.size();
	double rootLimit = (sqrt((double) newLimit) - 1) / 2.0;

	for (long i = 1; i <= rootLimit; i++)
	{
		if(primes[i])
		{
			number_t p = 2 * i + 1;
			if (p * p < limit)
			{
				number_t lowLim = limit / p + 1;
				if (!(lowLim % 2))
					lowLim++;
				lowLim *= p;
				lowLim = (lowLim - 1) / 2;
				for (long j = lowLim ; j < size; j += 2 * i + 1)
					primes[j] = false;
			}
			else
			{
				for (long j = 2 * i * (i + 1) ; j < size; j += 2 * i + 1)
					primes[j] = false;
			}
		}
	}

	primeNums.clear();
	primeNums.push_back(2);
	for (int i = 1; i < (newLimit + 1) / 2; i++)
		if (primes[i])
			primeNums.push_back(2*i+1);
	
	limit = newLimit;
	localLimit = newLimit;
}

void Primes::setNewLimit(number_t newLimit)
{
	if (limit < newLimit)
	{	
		primes.resize( (newLimit+1) / 2, true);
		_runSieve(newLimit);
	}
	
	localLimit = newLimit;
}

bool Primes::isPrime(test_t num)
{
	if (num <= 1)
		return false;
	if (num == 2)
		return true;
	
	if (!(num % 2))		// Even numbers
		return false;

	if (num < limit)
		return primes[(number_t)(num - 1) / 2];

	// Test up to square root
	 double rootNum = sqrt( (double) num);
	 while (rootNum > limit)
		setNewLimit( 2 * limit );

	for (number_t i = 0; (i < primeNums.size() && primeNums[i] < rootNum ); i++)
		if (num % primeNums[i] == 0 )
			return false;

	return true;
}

bool Primes::millerRabin(test_t num) 
{
	if (num <= 1)
		return false;
	if (num == 2)
		return true;
	if (num%2==0)
		return false;
	if (num < limit)
		return primes[(num-1)/2];

	int s = 0;
	test_t d = num-1;
	while (d%2==0) {
		s++;
		d /= 2;
	}
	
	int as[] = {2, 3, 5, 7, 11, 13, 17};
	for (int i = 0; i < 7; i++) {
		bool passed = false;
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

test_t Primes::modExp(test_t base, number_t exp, number_t mod) {
	if (exp == 0)
		return 1;
	if (exp == 1)
		return base % mod;
	test_t x = modExp(base, exp/2, mod);
	x *= x;
	x %= mod;
	if (exp % 2 == 1) {
		x *= base;
		x %= mod;
	}
	return x;
}

number_t Primes::getPrime(number_t index)
{
	while ( index > primeNums.size())
		setNewLimit( 2 * limit + 1 );

	return primeNums[index - 1];
}

number_t Primes::numPrimes()
{
	return primeNums.size();
}

number_t Primes::operator[](number_t ix) {
	return primeNums[ix];
}

void Primes::showPrimes(ostream& out)
{
	number_t length = primeNums.size();
	number_t i = 0;
	while (i < length && (primeNums[i] <= localLimit) )
	{
		out << primeNums[i] << " ";
		i++;
	}
	
}
