#include <iostream>
#include <time.h>
#include "Utilities.h"
#include "Euler126.h"

using namespace std;

int main(){
	int begin = clock();

	Euler126(20000, 1000);

	int end = clock();
	cout << endl << end - begin << endl;
	system("pause");
	return 0;
}
