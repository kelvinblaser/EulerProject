/******************************************************************************
Project Euler 126 - http://projecteuler.net/problem=126

Number of cubes in layers of cuboids
The (q+1)th layer of an m x n x p cuboid has 2(mn+np+mp) + 4q(m+n+p) + 4q(q+1)
cubes.

------------------------------------------------------------------------------
First Attempt Strategy
	Choose some N_max, hopefully higher than the answer.  Generate all cuboids
	with layers less than N_max.  Count the number of layers with z cubes.

	Outcome:  Success.  Answer: 18522   Time: 1.5 sec

Kelvin Blaser		2013-07-28
******************************************************************************/
#include <map>
#include <iostream>
#include <iomanip>

long Euler126(long N_max, int first_to)
{
	using namespace std;

	// First generate all layers of all cuboids with less than N_max 
	long m_max, n_max, p_max;
	long surf, perim, num_cubes;
	int out = 6;

	map<long, int> num_layers;

	m_max = (N_max - 2) / 4;
	for (long m=1; m <= m_max; m++)
	{
		n_max = (N_max - 2*m)/(2*(m+1));
		if (n_max > m)
			n_max = m;
		for (long n = 1; n <= n_max; n++)
		{
			p_max = (N_max - 2*n*m) / (2 * (n + m));
			if (p_max > n)
				p_max = n;
			for (long p = 1; p <= p_max; p++)
			{
				surf  = m*n + n*p + p*m;
				perim = m + n + p;

				for (long q = 0;  (2*surf + 4*q*perim + 4*q*(q-1) )<= N_max; q++)
				{
					num_cubes = 2*surf + 4*q*perim + 4*q*(q-1); 
					if (num_layers.count(num_cubes))
						num_layers[num_cubes]++;
					else
						num_layers[num_cubes] = 1;
				}
			}
		}
	}

	// Now find the first layer number to have first_to layers.
	map<long, int>::iterator it;
	for (it = num_layers.begin(); it != num_layers.end(); it++)
		if (it->second == first_to)
			break;

	if (it == num_layers.end())
		cout << "There are no values less than " << N_max << " for which C(n) equals " << first_to << endl;
	else
		cout << "C(" << it->first << ") = " << it->second << ".  This is the first value n for which C(n) = " << first_to << endl;
	return 0;
}