/*****************************************************************************
Solution to Project Euler 134 - http://projecteuler.net/problem=134
Author: Kelvin Blaser
Date: 12-25-2012 

Making some cubes yeah!
*****************************************************************************/
#include "Primes.h"
#include "Utilities.h"
typedef long long ll;

ll Euler134()
{
	Primes primes(1000040);
	int p1, p2;
	int temp;
	int d, d10, phi;
	ll x;
	ll sum = 0;

	for (int i = 3; primes.getPrime(i) <= 1000000; i++)
	{
		p1 = primes.getPrime(i);
		p2 = primes.getPrime(i+1);
		temp = p1;
		d10 = 1;
		d = 0;
		while (temp > 0)
		{
			d++;
			d10 *= 10;
			temp /= 10;
		}
		x = (p1*modExp(p2, (d10*2)/5-1, d10)) % d10;
		//cout << "p1 = " << p1 << "; p2 = " << p2 << ";  --  " << p2*x << endl; 
		sum += p2*x;
	}
	return sum;
}