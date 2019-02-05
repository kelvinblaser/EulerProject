#include <iostream>
#include <time.h>
#include "Utilities.h"

using namespace std;

int main(){
	int begin = clock();

	cout << "GCD(285, 370) = " << gcd(285, 370) << endl;

	int end = clock();
	cout << endl << end - begin << endl;
	system("pause");
	return 0;
}
