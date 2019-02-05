/*****************************************************************************
Euler 166 - Criss Cross
http://projecteuler.net/problem=166

------------------------------------------------------------------------------
First Attempt:  Recursive depth first search for solutions.  

	Result:		Success:			Time:
------------------------------------------------------------------------------
Kelvin Blaser		2013-09-16
*****************************************************************************/
#include <iostream>
#include <iomanip>
#include <time.h>
#include <vector>
#include <algorithm>
#include <numeric>
using namespace std;

class CrissCross {
	int target;
	int size;
	vector <vector <int>> grid;

public:
	int count;
	CrissCross();
	CrissCross(int ss);
	void solve(int ix);
	void display();
};

CrissCross::CrissCross(int ss) {
	target = -1;
	size = ss;
	count = 0;
	grid.resize(ss);
	for (int i = 0; i < size; i++) {
		grid[i].resize(size);
		fill (grid[i].begin(), grid[i].end(), -1);
	}
}

void CrissCross::display() {
	for (int i = 0; i < size; i++)
	{
		for (int j = 0; j < size; j++)
			cout << grid[i][j] << ' ';
		cout << '\n';
	}
}

void CrissCross::solve(int ix = 0) {
	int row = ix / size;
	int col = ix % size;
	// The first row determines the sum for all the rows and cols
	if (ix < size) {
		for (int k = 0; k <= 9; k++) { 
			grid[row][col] = k;
			solve(ix+1);
		}
		return;
	}
	// Once the first row is filled, set the target
	if (ix == size) 
		target = accumulate(grid[0].begin(), grid[0].end(), 0);
	int val_min = 0;
	int val_max = 9;
	int col_sum = 0;	// Sum of column above current position
	int row_sum = 0;	// Sum of row to left of current position
	int dig_sum = 0;	// Sum of diagonal above (if needed)
	int adi_sum = 0;	// Sum of anti-diagonal above
	for (int i = 0; i < row; i++)
		col_sum += grid[i][col];
	row_sum = accumulate(grid[row].begin(), grid[row].begin()+col, 0);

	val_max = min(val_max, target-col_sum);
	val_max = min(val_max, target-row_sum);
	val_min = max(val_min, (target-col_sum) - (size-row-1)*9);
	val_min = max(val_min, (target-row_sum) - (size-col-1)*9);

	// If on the diagonal
	if (row == col) {
		for (int i = 0; i < row; i++)
			dig_sum += grid[i][i];
		val_max = min(val_max, target-dig_sum);
		val_min = max(val_min, (target-dig_sum) - (size-row-1)*9);
	}
	// On the anti-diagonal
	if (row == size-col-1) {
		for (int i = 0; i < row; i++)
			adi_sum += grid[i][size-i-1];
		val_max = min(val_max, target-adi_sum);
		val_min = max(val_min, (target-adi_sum) - (size-row-1)*9);
	}

	if (ix == size*size-1) {
		if (val_max == val_min) {
			count++;
			grid[size-1][size-1] = val_min;
		}
	}
	else {
		for (int k = val_min; k <= val_max; k++) {
			grid[row][col] = k;
			solve(ix+1);
		}
	}
}
		

int main() {
	int begin = clock();

	CrissCross cc(4);
	cc.solve();
	cout << endl << cc.count << endl;

	int end = clock();
	cout << endl << end - begin << endl;
	system("pause");
	return 0;
}