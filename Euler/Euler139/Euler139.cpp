/*****************************************************************************
Euler 139 - Pythagorean Tiles
http://projecteuler.net/problem=139

------------------------------------------------------------------------------
First Attempt: A pythagorean triple (a,b,c) with a < b < c satisfies the 
			   property iff b-a|c.  Generate all primitive triples with 
			   perimeter < 100000000 by Euclid's formula.  If b-a|c, then 
			   divide 100000000 by the perimeter of the primitive triple to 
			   get the number of triangles similar to the primitive with 
			   perimeter less than 100000000.

	Result:	10057761		Time: 557 ms   
			   Could do better by noting that abs(a-b) = 1.  This means there 
			   are only one or two possible n values to try for a given m.  
			   Turns an O(p_max) algorithm into an O(sqrt(p_max)) algorithm.

	Result: 10057761		Time: 4 ms 
------------------------------------------------------------------------------
Kelvin Blaser		2013-08-13
*****************************************************************************/
#include <iostream>
#include <iomanip>
#include <time.h>
#include <cmath>
#include "../Euler/Utilities.h"

using namespace std;

int quad_algo(const int p_max);
int lin_algo(const int p_max);

int main(){
	int begin = clock();

	const int p_max = 100000000;
	cout << lin_algo(p_max) << " tilings\n";

	int end = clock();
	cout << endl << end - begin << endl;
	system("pause");
	return 0;
}

int quad_algo(int p_max) {
	const int m_max = int(sqrt(double((p_max-1)/2)));
	int n_max;
	int tilings = 0;

	for (int m = 2; m <= m_max; m++) {
		n_max = min(m-1, (p_max-1) / (2*m) - m);
		for (int n = (m%2)+1; n <= n_max; n+=2)
			if (gcd(m,n)==1)
				if ((m*m + n*n)%(abs(m*m-n*n-2*m*n))==0)
					tilings += (p_max-1) / (2*m*(m+n));
	}
	return tilings;
}

int lin_algo(int p_max) {
	const int m_max = int(sqrt(double((p_max-1)/2)));
	int tilings = 0;
	int n;

	const double root_two = sqrt(2.0) - 1.0;

	for (int m = 2; m <= m_max; m++) {
		n = int(root_two * m);
		if (n%2==m%2)
			n++;
		if (gcd(m,n)==1 && abs(m*m-n*n-2*m*n) == 1)
				tilings += (p_max-1) / (2*m*(m+n));
	}
	return tilings;
}