/*****************************************************************************
Euler 142 - Perfect Square Collection
http://projecteuler.net/problem=142

------------------------------------------------------------------------------
First Attempt:  x = (p1^2 + q1^2)/2, (p2^2 + q2^2)/2
				y = (p1^2 - q1^2)/2, (p3^2 + q3^2)/2
				z = (p2^2 - q2^2)/2, (p3^2 - q3^2)/2
				p = q mod 2

				Loop through p & q, creating all possible pairs 
				(p^2 + q^2, p^2 - q^2)  Find pairs with the same larger number
				(x).  The smaller numbers are then the candidates for y and z.
				See if these also constitute a pair.

	Result:		Success: 1006193	Time:	2656ms (Better solutions out 
													there)
------------------------------------------------------------------------------
Kelvin Blaser		2013-08-04
*****************************************************************************/
#include <iostream>
#include <iomanip>
#include <time.h>
#include <map>
#include <set>
using namespace std;

int main(){
	int begin = clock();

	map<long, set<long> > pairs;
	long pmin = 3;
	long pmax = 1600;
	long x, y, z, p2, q2;

	map<long, set<long> >::iterator it, jt;
	set<long>:: iterator kt, lt;

	bool done = false;

	do {
		// Make list of pairs
		for (long p = pmin; p < pmax; p++)
		{
			p2 = p*p;
			for (long q = (p-1)%2 + 1; q < p; q+=2)
			{
				q2 = q*q;
				x = p2 + q2;
				y = p2 - q2;
				if (!pairs.count(x))
					pairs[x] = set<long>();
				pairs[x].insert(y);
			}
		}

		// See if any set of pairs is a solution
		// Go through each possible x
		for (it = pairs.begin(); it != pairs.end(); it++)
		{
			set<long> *sec = &(it->second);
			// There must be at least 2 pairs which give the same x
			if (sec->size() > 1)
			{
				x = it->first;
				// Go through the possible y's
				for (kt = sec->begin(); kt != sec->end(); kt++)
				{
					y = *kt;
					// Go through the possible z's
					for (lt = kt; lt != sec->end(); lt++)
					{
						z = *lt;
						// Swap if y < z.
						if (y < z)
						{
							long temp = y;
							y = z;
							z = temp;
						}

						if (pairs.count(y))
						{
							jt = pairs.find(y);
							if (jt->second.count(z))
							{
								// Solution Found
								done = true;
								cout << "(x,y,z) = (" << x/2 << ',' << y/2 
									<< ',' << z/2 << ").\tx+y+z = " 
									<< (x+y+z)/2 << endl;
							}
						}
					}
				}
			}
		}

		pmin = pmax;
		pmax *= 2;
		cout << "Increasing pmax to " << pmax << endl;
	} while (!done);

	int end = clock();
	cout << endl << end - begin << endl;
	system("pause");
	return 0;
}