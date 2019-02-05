/*****************************************************************************
Solution to project Euler 111 - http://projecteuler.net/problem=111
Author: Kelvin Blaser
Date:  2013-06-29

Finding primes with large runs of digits
*****************************************************************************/
#include <vector>
#include "Primes.h"
#include <iostream>
#include <cmath>

using namespace std;

long long lpow(long long base, int exp)
{
	long long x;
	if (exp==1)
		return base;
	if (exp==0)
		return 1;
	
	x = lpow(base, exp/2);
	if (exp%2)
		return x*x*base;
	return x*x;
}

// Sets up the dig_vec.  This process depends on the number of digits to set 
// up as well as whether the digit is 0 or not.
void set_up_dig_vec(vector<int> &dig_vec, int num_dig, int m, int d)
{
	for (int i = 0; i < num_dig; i++)
		dig_vec.push_back(i);
	if (d==0)
		dig_vec[dig_vec.size()-1] = m-1;
	return;
}

// dig_index_combo changes dig_vec to the next combination of digits.
// Returns true if there is a next combo and false if there is not.
bool dig_index_combo(vector<int> &dig_vec, int m, int d)
{
	int zero_case; // Used if d==0
	if (d==0)
	{
		zero_case = dig_vec.back();
		dig_vec.pop_back();
		m--;
	}

	int ix = dig_vec.size()-1;
	while (ix >= 0 && dig_vec[ix] == m+ix - dig_vec.size())
		ix--;
	if (ix < 0)
		return false;
	dig_vec[ix]++;
	ix++;
	for (; ix < dig_vec.size(); ix++)
		dig_vec[ix] = dig_vec[ix-1]+1;

	if (d==0)
		dig_vec.push_back(zero_case);
	return true;
}

long long build_d_template(vector<int> &dig_vec, int m, int d)
{
	if (d==0)
		return 0;
	long long temp=0;
	for (int i=0; i < m; i++)
	{
		temp *= 10;
		temp += d;
	}
	for (int i=0; i < dig_vec.size(); i++)
		temp -= d * lpow(10,dig_vec[i]);
	return temp;
}

long long build_num(long long temp, vector<int> &dig_vec, int add_code)
{
	for (int i=0; i < dig_vec.size(); i++)
	{
		temp += (add_code % 10) * lpow(10,dig_vec[i]);
		add_code /= 10;
	}
	return temp;
}


long long sum_dig(int m, int d, Primes &primes)
{
	long long sum;					// The answer
	long long temp;					// A number which holds a sort of template (i.e. 2202220220 if d = 2)
	long long test_num;				// The number to test for primality (i.e. 2252228223 if d = 2)
	long long test_min = lpow(10,m-1);
	vector<int> dig_vec;			// Tells which digits are not d
	bool prime_found = false;		// Once a prime has been found, don't check numbers with fewer d's
	long long ix_max;
	int max_num_dig = m;

	if (d==0)
		max_num_dig--;

	for (int num_dig = 1; !prime_found && num_dig < max_num_dig; num_dig++)
	{
		dig_vec.clear();
		set_up_dig_vec(dig_vec, num_dig, m, d);
		sum = 0;
		ix_max = lpow(10, num_dig);
		
		do
		{
			temp = build_d_template(dig_vec, m, d);
			for (int i=0; i < ix_max; i++)
			{
				test_num = build_num(temp, dig_vec, i);
				if (primes.isPrime(test_num) && test_num >= test_min)
				{
					prime_found = true;
					sum += test_num;
					cout << test_num << ", \n";
				}
			}
		}while(dig_index_combo(dig_vec, m, d)); // While there are still combo's.
	}

	return sum;
}

/* The main proram.  m is the number of digits. */
long long Euler111(int m)
{
	long long ans = 0;

	// Build the appropriate limit for Primes
	long long lim = 1; 
	for (int i = 0; i < m/2; i++)
		lim *= 10;
	if (m <= 6)
		for (int i = m/2; i < m; i++)
			lim *= 10;

	Primes primes(lim);

	for (int d=0; d < 10; d++)
		ans += sum_dig(m, d, primes);
		
	return ans;
}