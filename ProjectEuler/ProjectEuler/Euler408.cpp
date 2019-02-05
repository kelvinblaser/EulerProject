#include "Euler408.h"
#include "Utilities.h"
#include <set>
#include <map>
#include <cmath>
#include <iostream>
using namespace std;

Point::Point(long x0, long y0)
{
	x = x0;
	y = y0;
}

bool operator<(Point lSide, Point rSide)
{
	if (lSide.x < rSide.x)
		return true;
	if (lSide.x > rSide.x)
		return false;
	if (lSide.y < rSide.y)
		return true;
	return false;
}

long Euler408(long limit, long modder)
{
	set<Point> iaps;
	map<Point, long long> chooseVals;
	cout << "Calculating inadmissible points .... " << endl;
	calculateIaps(&iaps, limit);
	// Calculate chooseVals
	cout << "Calculating (x+y)choose(y) at each inadmissible point ...\n";
	for (set<Point>::iterator it = iaps.begin(); it != iaps.end(); it++)
	{
		chooseVals[*it] = modChoose(it->x + it->y, it->y, modder);
		//cout << '(' << it->x << ',' << it->y << ") " << chooseVals[*it]
			//<< endl;
	}
	long long ans = modChoose(2*limit, limit, modder);
	cout << "Subtracting the effects of inadmissible points downstream from...\n";
	for (set<Point>::iterator it = iaps.begin(); it != iaps.end(); it++)
	{
		set<Point>::iterator jt = it;
		jt++;
		for (; jt != iaps.end(); jt++)
		{
			if (it->x <= jt->x && it->y <= jt->y)
			{
				long x = jt->x - it->x;
				long y = jt->y - it->y;
				chooseVals[*jt] -= chooseVals[*it] * modChoose(x+y,y,modder);
				chooseVals[*jt] %= modder;
			}
			if (it->y <= jt->x && it->x <= jt->y)
			{
				long x = jt->x - it->y;
				long y = jt->y - it->x;
				chooseVals[*jt] -= chooseVals[*it] * modChoose(x+y,y,modder);
				chooseVals[*jt] %= modder;
			}
		}
		ans -= 2 * chooseVals[*it] * modChoose(2*limit - it->x - it->y, limit - it->x, modder);
		ans %= modder;
		cout << '(' <<  it->x << ',' << it->y << ')' << endl;
	}
	cout << iaps.size() << endl;

	if (ans < 0)
		ans += modder;
	return ans;
}

long modChoose(long n, long k, long modder)
{
	if (k > n)
		return 0;

	if (2*k > n)
		k = n - k;

	long long num = 1;
	long long den = 1;
	for (long i = 1; i <= k; i++)
	{
		num *= n - i + 1;
		num %= modder;
		den *= i;
		den %= modder;
	}
	long long ans = num * modExp(den, modder-2, modder);
	ans %= modder;
	return long(ans);
}

void calculateIaps(set<Point> *iaps, long limit)
{
	long mMax = long(sqrt(double(2*limit)));

	for (long m = 2; m <= mMax; m++)
	{
		long nMax = long(sqrt(double(2*limit - m*m)));
		if (nMax > m)
			nMax = m;
		for (long n = 1+(m%2); n <= nMax; n+=2)
		{
			if (gcd(m,n) == 1)
			{
				long long a = 2*m*n;
				long long b = m*m - n*n;
				long long x,y;
				if (a > b)
				{
					x = a*a;
					y = b*b;
				}
				else
				{
					x = b*b;
					y = a*a;
				}
				long kMax = long(sqrt(double(limit / x)));
				for (long k = 1; k <= kMax; k++)
				{
					Point p(x*k*k, y*k*k);
					iaps->insert(p);
				}
			}
		}
	}
}