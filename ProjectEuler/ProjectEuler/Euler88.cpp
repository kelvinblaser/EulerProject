#include "Euler88.h"
#include <vector>
#include <set>
using namespace std;

long Euler88(long limit)
{
	vector<long> leastProductSumList;
	set<long> leastProductSumSet;

	buildLeastProductSumList(&leastProductSumList, limit);
	convertListToSet(&leastProductSumList, &leastProductSumSet);
	long sum = sumSet(&leastProductSumSet);

	return sum;
}

int maxNumFactors(long limit)
{
	int count = 0;
	while (limit > 0)
	{
		count++;
		limit /= 2;
	}
	return count;
}

void buildLeastProductSumList(vector<long> *leastProductSumList, long limit)
{
	leastProductSumList->resize(limit, 2*limit);

	int numFactors = maxNumFactors(limit);
	vector<long> factors;
	factors.resize(numFactors, 1);

	int cIndex;
	while (factors[0] <= limit)
	{
		cIndex = numFactors - 1;
		while(factors[cIndex]+1 > maxFactorForIndex(&factors, cIndex, limit))
		{
			factors[cIndex] = 1;
			cIndex--;
		}
		factors[cIndex]++;

		// Calculate the product-sum number
		long pNum = 1;
		long sNum = 0;
		for (int i = 0; i < numFactors; i++)
		{
			pNum *= factors[i];
			sNum += factors[i];
		}

		// Calculate the number of factors (including ones)
		long psNumFactors = (pNum - sNum) + numFactors;

		// If the p-s number is the smallest for the number of factors, 
		   // Add it to the list
		if (psNumFactors <= limit && 
			pNum < leastProductSumList[0][psNumFactors-1])
			leastProductSumList[0][psNumFactors-1] = pNum;
	}
}

void convertListToSet(vector<long> *lpsList, set<long> *lpsSet)
{
	int size = lpsList->size();
	for (int i = 1; i < size; i++)
		lpsSet->insert(lpsList[0][i]);
}

long sumSet(set<long> *lpsSet)
{
	long sum = 0;
	for (set<long>::iterator it = lpsSet->begin();
		 it != lpsSet->end(); it++)
		 sum += *it;

	return sum;
}

long maxFactorForIndex(vector<long> *factors, int index, long limit)
{
	if (index != 0)
	{
		long max1 = factors[0][index-1];
		long max2 = 1;
		for (int i=0; i < index; i++)
			max2 *= factors[0][i];
		max2 = (2*limit) / max2;
		if (max1 < max2)
			return max1;
		else
			return max2;

	}
	return 2*limit;
}
