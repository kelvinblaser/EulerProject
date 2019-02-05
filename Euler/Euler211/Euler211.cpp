#include <vector>
#include <algorithm>
#include <cmath>
#include <iostream>
#include <iomanip>
#include <time.h>
using namespace std;

const int MAX = 64000000;
bool isSquare(_int64 n);

int main() {
	int begin = clock();

	std::vector<_int64> sigma2(MAX+1);
	std::fill(sigma2.begin(), sigma2.end(), 1);

	_int64 sum = 0;
	for (_int64 i = 2; i <= MAX; i++) {
		_int64 i2 = i*i;
		for (int j = i; j <= MAX; j+=i) {
			sigma2[j] += i2;
		}
		if (isSquare(sigma2[i])) {
			//cout << setw(10) << i 
				//<< setw(20) << sigma2[i] 
				//<< setw(10) << (_int64) (sqrt((long double) sigma2[i]) + 0.5) << endl;
			sum += i;
		}
	}

	cout << sum << endl;

	int end = clock();
	cout << endl << end - begin << endl;
	system("pause");
	return 0;
}

 bool isSquare(_int64 n) {
	double root = std::sqrt((double) n);
	_int64 r = (_int64) (root + 0.01);
	return (r*r == n);
 }
  
