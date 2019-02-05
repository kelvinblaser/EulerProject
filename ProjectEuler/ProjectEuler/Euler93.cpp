#include "Euler93.h"
#include <set>
#include <iostream>
//#include <mpirxx.h>
#include "Utilities.h"
using namespace std;

int Euler93()
{
	// Cycle through all permutations of 4 distinct digits.
		// Then Cycle through all permutations operations between the digits
	int numSet[] = {0,1,2,3};
	int out = 1234;
	int maxString = 28;
	Operator ops[] = {ADD, ADD, ADD};
	do{
		// For each set of digits find the set of numbers that can be created.
		set<int> nums;
		do{
			do{
				int num = numSet[0];
				int den = 1;
				for (int i = 0; i < 3; i++)
				{
					switch (ops[i])
					{
					case ADD: num += numSet[i+1] * den;
						break;
					case SUB: num -= numSet[i+1] * den;
						break;
					case MUL: num *= numSet[i+1];
						break;
					case DIV: den *= numSet[i+1];
						break;
					}
				}
				if (den != 0)
				{
					int g = gcd(num, den);
					num /= g;
					den /= g;
				}
				if (num > 0 && den == 1)
					nums.insert(num);
				if (num < 0 && den == 1)
					nums.insert(-num);
			}while(nextOps(ops));
		}while(nextNumPermute(numSet));
		// Then see how long a string of numbers 1 ... n was created
		int count = 0;
		while (nums.count(count+1))
			count += 1;
		// If it was the longest so far, change the answer
		if (count > maxString)
		{
			maxString = count;
			out = 0;
			for (int i = 0; i < 4; i++)
			{
				out *= 10;
				out += numSet[i];
			}
		}
	}while(nextNumCombo(numSet));
	return out;
}

bool nextNumCombo(int *numSet)
{
	int index = 3;
	while (index >= 0 && numSet[index] == 6 + index)
		index--;
	if (index < 0)
	{
		for (int i = 0; i < 4; i++)
			numSet[i] = i+1;
		return false;
	}

	numSet[index]++; 
	for (int i = index + 1; i < 4; i++)
		numSet[i] = numSet[i-1]+1;
	return true;
}

bool nextNumPermute(int *numSet)
{
	// Get lexicographically next permutation.
	// http://en.wikipedia.org/wiki/Permutation
	// 1. Find the largest index k such that numSet[k] < numSet[k+1].
	int k = 2;
	while (k >= 0 && numSet[k] >= numSet[k+1])
		k--;
	if (k == -1)
	{
		// If this does not exist, then done. Reverse numSet.
		reverseArray(numSet, 0, 3);
		return false;
	}
	// 2. Find the largest index l such that numSet[l] > numSet[k] (l > k).
	int l = 3;
	while (numSet[l] <= numSet[k])
		l--;
	// 3. Swap numSet[k] and numSet[l].
	int temp = numSet[k];
	numSet[k] = numSet[l];
	numSet[l] = temp;
	// 4. Reverse sequence from numSet[k+1] up to and including the last.
	reverseArray(numSet, k+1, 3);
	return true;
}

bool nextOps(Operator *ops)
{
	int index = 0;
	while (index < 3 && ops[index] == DIV)
		index++;
	if (index == 3)
	{
		for (int i = 0; i < 3; i++)
			ops[i] = ADD;
		return false;
	}

	switch (ops[index])
	{
	case ADD: ops[index] = SUB;
		break;
	case SUB: ops[index] = MUL;
		break;
	case MUL: ops[index] = DIV;
		break;
	}
	for (int i = 0; i < index; i++)
		ops[i] = ADD;

	return true;
}

void reverseArray(int *numSet, int startIndex, int endIndex)
{
	while (endIndex > startIndex)
	{
		int temp = numSet[startIndex];
		numSet[startIndex] = numSet[endIndex];
		numSet[endIndex] = temp;
		startIndex++;
		endIndex--;
	}
}