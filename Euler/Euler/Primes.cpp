#include "Primes.h"
#include <cmath>

vector <bool> Primes::primes;
number_t Primes::limit = 0;
vector <number_t> Primes::primeNums(1);

Primes::Primes(void)
{
	primeNums[0] = 2;
	if (!limit)
	{
		primes.resize(1, true);
		runSieve(1);
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
		runSieve(newLimit);
	}
	
	localLimit = newLimit;
}

Primes::~Primes(void)
{
}

void Primes::runSieve(number_t newLimit)
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
		runSieve(newLimit);
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
	
	return true;

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