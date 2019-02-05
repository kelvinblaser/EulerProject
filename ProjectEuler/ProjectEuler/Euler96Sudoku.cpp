#include "Euler96Sudoku.h"
#include <string>
#include "Sudoku.h"
#include <iostream>
#include <fstream>
using namespace std;

int Euler96(string filename)
{
	Sudoku board1;
	ifstream fin(filename);
	char waste[256];
	char c;
	int numSolved = 0;
	int sum = 0;
	if (fin.is_open())
	{
		while (!fin.eof())
		{
			fin.getline(waste,256);
			cout << waste << endl;
			fin >> board1;
			board1.solve();
			fin.get(c);

			if (!board1.isSolved())
				cout << board1 << endl;
			else
			{
				numSolved++;
				sum += board1.getCornerNum();
				//cout << board1 << endl;
			}
		}
	}

	fin.close();
	return sum;
}