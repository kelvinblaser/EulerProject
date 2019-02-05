#include "Euler86.h"
#include "Utilities.h"
#include <iostream>
#include <cmath>
using namespace std;

Triple::Triple(int A, int B, int C)
{
	// Sort
	int temp;
	if (A > B)
	{
		temp = A;
		A = B; 
		B = temp;
	}

	if (A > C)
	{
		temp = A;
		A = C;
		B = temp;
	}

	if (B > C)
	{
		temp = B;
		B = C;
		C = temp;
	}
	
	// Assign
	a = A;
	b = B;
	c = C;
}

long Euler86(int limit)
{
	vector<Triple> trips;
	generateTriples(&trips, limit/100);
	
	int lowM = 1;
	int highM = 1;
	// Find Order of Magnitude
	while (lowM == highM)
	{
		if (countCuboids(&trips, 2*lowM) < limit)
			lowM *= 2;
		highM *= 2;
	}
	// Zero in
	while (highM - lowM > 1)
	{
		int nextM = (highM + lowM) / 2;
		if (countCuboids(&trips, nextM) < limit)
			lowM = nextM;
		else
			highM = nextM;
	}

	return highM;
}

void generateTriples(vector<Triple> *trips, int max)
{
	int mMax = int(sqrt(double(max)));
	for (int m = 2; m <= mMax; m++)
	{
		int nMax = int(sqrt(double(max-m*m)));
		if (nMax >= m)
			nMax = m-1;
		for (int n = 1-(m%2); n <= nMax; n+=2)
		{
			if (gcd(m,n)==1)
			{
				long a = m*m - n*n;
				long b = 2*m*n;
				long c = m*m + n*n;
				trips->push_back(Triple(a,b,c));
			}
		}
	}
}

long countCuboidsInTriple(Triple trip, int M)
{
	long count = 0;
	int mul = 1;
	while(trip.c * mul <= 3*M)
	{
		int a = trip.a * mul;
		int b = trip.b * mul;
		int c = trip.c * mul;

		if (b <= M)
			count += a/2;

		if ((a <= M) && (b/2-b+a >= 0))
			count += b/2 - b + a + 1;

		mul++;
	}
	return count;
}

long countCuboids(vector<Triple> *trips, int M)
{
	long count = 0;
	for (int i = 0; i < trips->size(); i++)
		if (trips[0][i].c < 3*M)
			count += countCuboidsInTriple(trips[0][i], M);

	return count;
}