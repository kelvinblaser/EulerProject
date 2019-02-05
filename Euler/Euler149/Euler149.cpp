/*****************************************************************************
Euler 149 -		Searching for a Maximum Sum Subsequence
http://projecteuler.net/problem=146

------------------------------------------------------------------------------
First Attempt:  Make the table.  Find the max sum on each row, column and 
				diagonal.  Print the maximum max sum.  Calculating the max sum
				for a sequence: Add one number at a time recording the 
				maximum.  If the sum goes negative, start over at zero with
				the next entry in the sequence.

	Result:		Success					Time:	629 ms
------------------------------------------------------------------------------
Kelvin Blaser		2013-08-30
*****************************************************************************/
#include <iostream>
#include <iomanip>
#include <time.h>
#include "boost/multi_array.hpp"
#include <vector>
using namespace std;

typedef boost::multi_array<long long, 2> long2d;
long2d create_table(int size);
void max_sum(vector<long long> &vec, long long &max_s);

int main(){
	int begin = clock();

	int size = 2000;
	long long sum, max_s = 0;
	long2d table = create_table(size);
	cout << "Done Calculating Table\n";
	vector<long long> vec;
	
	for (int i = 0; i < size; i++) {
		// ith row
		vec.resize(size);
		for (int j = 0; j < size; j++)
			vec[j] = table[i][j];
		max_sum(vec, max_s);
		// ith column
		for (int j = 0; j < size; j++)
			vec[j] = table[j][i];
		max_sum(vec, max_s);
		// ith diagonal above main
		vec.resize(size - i);
		for (int j = 0; j < size-i; j++)
			vec[j] = table[i+j][j];
		max_sum(vec, max_s);
		// ith diagonal below main
		for (int j = 0; j < size-i; j++)
			vec[j] = table[j][i+j];
		max_sum(vec, max_s);
		// ith anti-diagonal above main
		for (int j = 0; j < size-i; j++)
			vec[j] = table[j][size-i-j-1];
		max_sum(vec, max_s);
		// ith anti-diagonal below main
		for (int j = 0; j < size-i; j++)
			vec[j] = table[i+j][size-j-1];
		max_sum(vec, max_s);
	}
	cout << max_s << endl;

	int end = clock();
	cout << endl << end - begin << endl;
	system("pause");
	return 0;
}

long2d create_table(int size)
{
	long2d table(boost::extents[size][size]);
	vector<int> vec(size*size);
	for (long long k = 1; k <= size*size; k++)
		if (k <= 55)
			vec[k-1] = ((100003 - 200003*k + 300007*k*k*k) % 1000000) - 500000;
		else
			vec[k-1] = ((vec[k-25] + vec[k-56] + 1000000) % 1000000) - 500000;
	for (int i = 0; i < size; i++)
		for (int j = 0; j < size; j++) 
			table[i][j] = vec[i*size+j];

	return table;
}

void max_sum(vector<long long> &vec, long long &max_s)
{
	long long max_temp = 0;
	int size = vec.size();
	for (int i = 0; i < size; i++) {
		max_temp += vec[i];
		if (max_temp < 0)
			max_temp = 0;
		else if (max_temp > max_s)
			max_s = max_temp;
	}
	return;
}