/*****************************************************************************
Euler 135 - Same Differences
http://projecteuler.net/problem=135

Also Solves 136 - Singleton Difference

------------------------------------------------------------------------------
First Attempt:  Brute Force Counting
				The following inequalities are satisfied:
				1.  y > d
				2.  y < 4d
				3.  y^2 - 4dy + n_max >= 0

	Result: Success   Solution: 4989		Time: 49.3 seconds
			Should be able to speed this up.  I know that y(4d - y) = n, so I 
			could just find all the factors of each n using a seive or 
			something.  But it's late.  Need to sleep.  No more programming.

			Ok speed up by getting rid of map and compiling in release mode.  
			(Alot of the bog down was probably debug related)
			Time:	27 ms
------------------------------------------------------------------------------
Euler 136:
	After optimizing by getting rid of map, this algorithm completes problem 
	136

	Solution:	2544559			Time:	2618 ms
------------------------------------------------------------------------------
Kelvin Blaser		2013-07-29
*****************************************************************************/
#include <iostream>
#include <iomanip>
#include <time.h>
#include <map>
using namespace std;

int main(){
	int begin = clock();

	const int MAX = 50000000;
	long long d = 1;
	int y, n;
	//map<long long, int> n_count;
	int* n_count = new int[MAX+1];
	for (int i = 0; i <= MAX; i++)
		n_count[i] = 0;

	// Before Parabolic Bifurcation
	while (4*d*d <= MAX)
	{
		for (y=d+1; y < 4*d; y++)
		{
			n = y*(4*d - y);
			n_count[n]++;
			//if (n_count.count(n))
			//	n_count[n]++;
			//else
			//	n_count[n] = 1;
		}
		d++;
	}

	// Parabolic Bifurcation to squeeze at d
	while ( (d-1)*(d-1) >= 4*d*d - MAX )
	{	
		for(y=d+1; (2*d - y)*(2*d-y) >= 4*d*d - MAX; y++)
		{
			n = y*(4*d - y);
			n_count[n]++;
			//if (n_count.count(n))
			//	n_count[n]++;
			//else
			//	n_count[n] = 1;
		}

		for(y=4*d-1; (y-2*d)*(y-2*d) >= 4*d*d - MAX; y--)
		{
			n = y*(4*d - y);
			n_count[n]++;
			//if (n_count.count(n))
			//	n_count[n]++;
			//else
			//	n_count[n] = 1;
		}
		d++;
	}

	// Squeeze at d to squeeze at 4d
	while ( 4*d <= MAX+1 )
	{	
		for(y=4*d-1; (y-2*d)*(y-2*d) >= 4*d*d - MAX; y--)
		{
			n = y*(4*d - y);
			n_count[n]++;
			//if (n_count.count(n))
			//	n_count[n]++;
			//else
			//	n_count[n] = 1;
		}
		d++;
	}

	//map<long long, int>::iterator it;
	int count10 = 0;
	for (int i = 1; i <= MAX; i++)
		if (n_count[i] == 1)
			count10++;
	//for (it = n_count.begin(); it != n_count.end(); it++)
	//	if (it->second==10)
	//		count10++;
		//cout << setw(10) << it->first << setw(5) << it->second << endl;
	cout << count10;

	int end = clock();
	cout << endl << end - begin << endl;
	system("pause");
	return 0;
}