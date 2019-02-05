/*****************************************************************************
Euler 128 - Hexagonal Tile Differences
http://projecteuler.net/problem=127

------------------------------------------------------------------------------
First Attempt:  Convert from n to radius and index coords. Then go through n 
				to find the numbers which have 3 prime differences.

				Note.  Only numbers on the corners [ (r,i) = (r, mr) for 
				m in {0,1,2,3,4,5} ] or the last number in a ring [ (r,i) = 
				(r, 6r-1) can have 3 prime differences. ]  This greatly 
				reduces the search space.

				The points have the following neighbors.  Let j = i/r.
				  Corner									Side
			1.	(r, (i+1))		- Don't need to test	(r, 0)
			2.	(r, (i-1)%6r)   - Only test j=0			(r, (i-1))	- DNT
			3.	(r-1, j(r-1))							(r-1, 0)
			4.	(r+1, j(r-1)%6(r+1))					(r-1, 6*r-1)- DNT
			5.	(r+1, jr)								(r+1, 6(r+1)-1) - DNT
			6.	(r+1, j(r+1))							(r+1, 6(r+1)-2)

	Result   :  Success But takes a while
				Solution:  1631922332		Time:  4min 30sec
				I noticed that every point is either j = 0 or one of the Side
				points.  I have been able to convince myself that this must be
				so.  Cutting out those other points should speed things up by
				more than a factor of 4

				Much faster.   28 ms
------------------------------------------------------------------------------
Kelvin Blaser		2013-07-28
*****************************************************************************/
#include <iostream>
#include <iomanip>
#include <time.h>
#include "../Euler/Utilities.h"
#include "../Euler/Primes.h"

using namespace std;

int main(){
	int begin = clock();

	const int END = 2000;
	int count     = 2;	// Not testing 1 and 2, but they work
	int r         = 2;
	bool done     = false;
	Primes primes(END*400);

	long p_count;

	while (!done)
	{
		// Check the top
		p_count = 0; // No prime differences found yet

		// Top
		if (primes.isPrime(6*r-1))	// Need to test the (r, 6r-1) point (2)
			p_count++;				// This point is usually not tested since 
										// the difference is 1 for the other corners

		if (primes.isPrime(12*r+5)) // (r+1, 6(r+1)-1) point is different for the top corner
			p_count++;				// Point (4)

		if (primes.isPrime(6*r+1))
			p_count++;

		if (p_count==3)
		{
			count++;
			//cout << setw(14) << 3*r*(r-1)+2+j*r << setw(8) << count 
				//<< setw(8) << j << endl;
			if (count == END)
			{
				long long ans = r-1;
				ans *= 3*r;
				ans += 2;
				cout << "----------------\n";
				cout << "|" << setw(13) << ans << " |" << endl;
				cout << "----------------\n";
				cout << r << endl;
				done = true;
				break;
			}
		}

		if (!done) // Test the side point (r, 6r-1)
		{
			p_count = 0;
			if (primes.isPrime(6*r-1)) // Point(1)
				p_count++;
			if (primes.isPrime(12*r-7))// Point(3)
				p_count++;
			if (primes.isPrime(6*r+5)) // Point(6)
				p_count++;

			if (p_count==3)
			{
				count++;
				//cout << setw(14) << 3*r*(r+1)+1 << setw(8) << count << endl;
				if (count==END)
				{
					long long ans = r+1;
					ans *= 3*r;
					ans += 1;
					cout << "----------------\n";
					cout << "|" << setw(13) << ans << " |" << endl;
					cout << "----------------\n";
					cout << r << endl;
					done = true;
				}
			}
		}
		r++;
	}

	int end = clock();
	cout << endl << end - begin << endl;
	system("pause");
	return 0;
}
