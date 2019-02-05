#include "Euler95AmicableChains.h"
#include <iostream>
#include <vector>
using namespace std;

void Euler95(int limit)
{
	int *sumDivs = new int[limit+1];
	int *chainSize = new int[limit+1];

	calculateSumsOfDivisors(sumDivs, limit);
	calculateChainSizes(chainSize, sumDivs, limit);

	int maxChainSize = 0;
	int smallestMember;
	for (int i = 0; i <= limit; i++)
	{
		if (chainSize[i] > maxChainSize)
		{
			maxChainSize = chainSize[i];
			smallestMember = i;
		}
	}

	cout << "The largest chain has " << maxChainSize << 
		" links with smallest link " << smallestMember << ".\n";

	/*int j;
	for (int k = 2; k < limit; k++)
	{
		if (chainSize[k] > 0)
		{
			j = k;
			cout << j << ": " << chainSize[j] << "; " << j;
			j = sumDivs[j];
			for (int i = 0; i < 12; i++)
			{
				cout << "->" << j;
				if (sumDivs[j] <= limit)
					j = sumDivs[j];
				else
					j = 0;
			}
			cout << endl;
		}
	}*/

	delete[] sumDivs;
	delete[] chainSize;
	sumDivs = 0;
	chainSize = 0;
}

void calculateSumsOfDivisors(int *sumDivs, int limit)
{
	sumDivs[0] = 0;
	sumDivs[1] = 0;
	// Every number is divisible by 1
	for (int i = 2; i <= limit; i++)
		sumDivs[i] = 1;

	for (int i = 2; i <= limit/2; i++)
		for (int j = 2*i; j <= limit; j+=i)
			sumDivs[j] += i;
}

void calculateChainSizes(int *chainSize, int *sumDivs, int limit)
{
	// -1 means chain not found, 0 means not in chain
	for (int i = 0; i <= limit; i++)
		chainSize[i] = -1;
	chainSize[0] = 0;
	chainSize[1] = 0;

	for (int i = 2; i <= limit; i++)
	{
		int j = i;
		// Go until find a zero, a sum over limit, or a chain.
		while(chainSize[j] == -1)
		{
			chainSize[j] = -2;
			if (sumDivs[j] <= limit)
				j = sumDivs[j];
			else
				chainSize[j] = 0;
		}
		// If found a -2, then we have a chain.
		if (chainSize[j] == -2)
		{
			int count = 0;
			while(chainSize[j] == -2)
			{
				chainSize[j] = -3;
				j = sumDivs[j];
				count++;
			}
			while(chainSize[j] == -3)
			{
				chainSize[j] = count;
				j = sumDivs[j];
			}
			j = i;
			while(chainSize[j] == -2)
			{
				chainSize[j] = 0;
				j = sumDivs[j];
			}
		}
		// If found anything else, make all the chainSizes explored 0.
		else 
		{
			j = i;
			while(chainSize[j] == -2)
			{
				chainSize[j] = 0;
				j = sumDivs[j];
			}
		}
	}
}