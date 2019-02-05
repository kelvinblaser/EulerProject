/*****************************************************************************
Euler 229 - Four Representations Using Squares
http://projecteuler.net/problem=229

------------------------------------------------------------------------------
First Attempt:  
	Going to try to brute force it by trying all possible combinations of a
	and b for each condition, noting which numbers are built, then counting
	those which fullfill all four conditions.

	Result:	11325263		Time:	113s

------------------------------------------------------------------------------
Kelvin Blaser		2014-12-31		Happy New Year!!
*****************************************************************************/
#include <iostream>
#include <iomanip>
#include <time.h>
#include <vector> // For vector<bool>
#include <cmath>  // For sqrt
using namespace std;

int Euler229(int n);
void representable(int n, int coeff, vector<bool> &pool);

int main() {
	int begin = clock();

	cout << "How many numbers N can be written in the forms \n" 
		<< "\t a^2 +  b^2 = N\n"
		<< "\t a^2 + 2b^2 = N\n"
		<< "\t a^2 + 3b^2 = N\n"
		<< "\t a^2 + 7b^2 = N?\n\n";

	cout << "There are " << Euler229(10000000) 
		<< " such numbers which do not exceed 10^7.\n";
	cout << "There are " << Euler229(2000000000) 
		<< " such numbers which do not exceed 2x10^9.\n";


	int end = clock();
	cout << endl << end - begin << endl;
	system("pause");
	return 0;
}

int Euler229(int n) {
	vector<bool> valid(n+1,true);
	representable(n, 1, valid);
	representable(n, 2, valid);
	representable(n, 3, valid);
	representable(n, 7, valid);

	int count = 0;
	for (int i=0; i <= n; i++)
		if (valid[i])
			count++;
	return count;
}

void representable(int n, int coeff, vector<bool> &pool) {
	vector<bool> new_valid(n+1, false);
	int bmax = int(sqrt(n / double(coeff)));
	int amax, s,a,b;
	for (b=1; b <= bmax; b++) {
		s = coeff * b*b;
		amax = int(sqrt(double(n - s)));
		for (a=1; a <= amax; a++)
			new_valid[a*a + s] = true;
	}
	for (int i=0; i <= n; i++)
		pool[i] = pool[i] && new_valid[i];
	return;
}