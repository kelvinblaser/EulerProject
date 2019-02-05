//#include <mpirxx.h>
#include <iostream>
#include <cmath>
using namespace std;

long Euler94(double perimeterLimit)
{
	long perimeterSum = 0;
	long mMax = sqrt(perimeterLimit / 3.);
	double root3 = sqrt(3.0);
	
	for (long m = 2; m <= mMax; m++)
	{
		long n = long(m / root3);
		if (3*n*n == m*m-1)
		{
			long x = m*m + n*n;
			perimeterSum += 3*x + 1;
		}
		long z = long(m * root3 + 0.5);
		if (3*m*m + 1 == z*z)
		{
			n = 2*m - z;
			long x = m*m + n*n;
			perimeterSum += 3*x - 1;
		}
	}

	return perimeterSum;
}