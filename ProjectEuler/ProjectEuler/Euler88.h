/*****************************************************************************
Solution to Project Euler 88 - http://projecteuler.net/problem=88
Author: Kelvin Blaser
Date: 12-24-2012   <- World didn't end
*****************************************************************************/
#include <vector>
#include <set>
using namespace std;

long Euler88(long limit);
int maxNumFactors(long limit);
void buildLeastProductSumList(vector<long> *leastProductSumList, long limit);
void convertListToSet(vector<long> *lpsList, set<long> *lpsSet);
long sumSet(set<long> *lpsSet);
long maxFactorForIndex(vector<long> *factors, int index, long limit);