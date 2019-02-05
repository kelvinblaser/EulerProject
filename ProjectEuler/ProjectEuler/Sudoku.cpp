#include "Sudoku.h"
#include <assert.h>
#include <set>
using namespace std;

SudokuSquare::SudokuSquare(int val)
{
	assert(val >= 0 && val <= 9);
	value = val;
	if (val == 0)
		for (int i = 0; i < 9; i++)
			possibles[i] = true;
	else
	{
		for (int i = 0; i < 9; i++)
			possibles[i] = false;
		possibles[val-1] = true;
	}
	
}
SudokuSquare::~SudokuSquare(void)
{
}


Sudoku::Sudoku(void)
{
	// Set all values to 0.
	for (int i = 0; i < 9; i++)
		for (int j = 0; j < 9; j++)
			squares[i][j] = SudokuSquare(0);
	initializePointers();	
}
Sudoku::Sudoku(const Sudoku &source)
{
	for (int i = 0; i < 9; i++)
		for (int j = 0; j < 9; j++)
			squares[i][j] = source.squares[i][j];
	initializePointers();
}
Sudoku::~Sudoku(void)
{
}

void Sudoku::initializePointers()
{
	for (int i = 0; i < 9; i++)
	{
		for (int j = 0; j < 9; j++)
		{
			rows[i][j] = &squares[i][j];
			cols[i][j] = &squares[j][i];
			boxes[3*(i/3)+(j/3)][3*(i%3)+(j%3)] = &squares[i][j];

			squares[i][j].row = i;
			squares[i][j].col = j;
			squares[i][j].box = 3*(i/3) + (j/3);
		}
	}
}
void Sudoku::refreshPossibles()
{
	// Loop through the squares
	for (int i = 0; i < 9; i++)
		for (int j = 0; j < 9; j++)
		{
			int val = squares[i][j].value;
			if (val != 0)
			{
				int box = 3*(i/3)+(j/3);
				for (int k = 0; k < 9; k++)
				{
					rows[i][k]->possibles[val-1] = false;
					cols[j][k]->possibles[val-1] = false;
					boxes[box][k]->possibles[val-1] = false;
					squares[i][j].possibles[k] = false;
				}
			}
		}
}
// Simple Logic
void Sudoku::possiblesSingletons()
{
	int numTrues;
	for (int i = 0; i < 9; i++)
	{
		for (int j = 0; j < 9; j++)
		{
			if (squares[i][j].value == 0)
			{
				numTrues = 0;
				for (int k = 0; k < 9; k++)
					if (squares[i][j].possibles[k])
						numTrues++;
				if (numTrues == 1)
				{
					int val = 0;
					while (squares[i][j].value == 0)
					{
						if (!squares[i][j].possibles[val])
							val++;
						else
						{
							squares[i][j].value = val+1;
							squares[i][j].possibles[val] = false;
						}
					}
					statusChanged = true;
				}
			}
		}
	}
}
void Sudoku::uniquesInGroups()
{
	for (int grp = 0; grp < 9; grp++)
	{
		for (int val = 1; val <= 9; val++)
		{
			uniqueValInGroup(rows[grp],val);
			refreshPossibles();
			uniqueValInGroup(cols[grp],val);
			refreshPossibles();
			uniqueValInGroup(boxes[grp],val);
			refreshPossibles();
		}
	}
}
void Sudoku::uniqueValInGroup(SudokuSquare **group, int val)
{
	int numPoss = 0;
	int kPosition;
	for (int k = 0; k < 9; k++)
	{
		if (group[k]->possibles[val-1])
		{
			numPoss++;
			kPosition = k;
		}
	}
	if (numPoss == 1)
	{
		group[kPosition]->value = val;
		statusChanged = true;
	}
}
// Advanced Logic
void Sudoku::lineSubGroup(SudokuSquare **line, int val, bool isRow)
{
	int lineNum;
	if (isRow)
		lineNum = line[0]->row;
	else
		lineNum = line[0]->col;
	int boxNum;
	// Find in which subgroups val is possible.
	bool groupsValIn[] = {false, false, false};
	for (int i = 0; i < 9; i++)
		if (line[i]->possibles[val-1])
			groupsValIn[i/3] = true;
	// Find how many subgroups val is possible.
	int numGroupsPossible = 0;
	for (int i = 0; i < 3; i++)
		if (groupsValIn[i])
		{
			numGroupsPossible++;
			if (isRow)
				boxNum = 3* (lineNum / 3) + i; 
			else
				boxNum = 3*i + (lineNum / 3);
		}
	// If only one, eliminate val from box
	if (numGroupsPossible == 1)
	{
		/*cout << "Changes in ";
		if (isRow)
			cout << "row-";
		else
			cout << "col-";
		cout << lineNum << " box-" << boxNum 
			<< " with value-" << val << endl;*/
		for (int i = 0; i < 9; i++)
		{
			if (isRow)
			{
				if (boxes[boxNum][i]->possibles[val-1] &&
					!(boxes[boxNum][i]->row == lineNum))
				{
					boxes[boxNum][i]->possibles[val-1] = false;
					statusChanged = true;
				}
			}
			else
			{
				if (boxes[boxNum][i]->possibles[val-1] &&
					!(boxes[boxNum][i]->col == lineNum))
				{
					boxes[boxNum][i]->possibles[val-1] = false;
					statusChanged = true;
				}
			}
		}
	}
}
void Sudoku::boxSubGroup(SudokuSquare **box, int val)
{
	int rowNum;
	int colNum;
	int boxNum = box[0]->box;
	bool rowGroupsValIn[] = {false, false, false};
	bool colGroupsValIn[] = {false, false, false};
	for (int i = 0; i < 9; i++)
		if (box[i]->possibles[val-1])
		{
			rowGroupsValIn[i/3] = true;
			colGroupsValIn[i%3] = true;
		}
	int rowGroupsPossible = 0;
	int colGroupsPossible = 0;
	for (int i = 0; i < 3; i++)
	{
		if (rowGroupsValIn[i])
		{
			rowGroupsPossible++;
			rowNum = 3*(boxNum/3) + i;
		}
		if (colGroupsValIn[i])
		{
			colGroupsPossible++;
			colNum = 3*(boxNum%3) + i;
		}
	}
	if (rowGroupsPossible == 1)
	{
		/*cout << "Changes to box-" << boxNum << " row-" << rowNum 
			<< " value-" << val << endl;*/
		for (int i = 0; i < 9; i++)
		{
			if (rows[rowNum][i]->possibles[val-1] &&
				rows[rowNum][i]->box != boxNum)
			{
				rows[rowNum][i]->possibles[val-1] = false;
				statusChanged = true;
			}
		}
	}
	if (colGroupsPossible == 1)
	{
		/*cout << "Changes to box-" << boxNum << " col-" << colNum 
			<< " value-" << val << endl;*/
		for (int i = 0; i < 9; i++)
		{
			if (cols[colNum][i]->possibles[val-1] &&
				cols[colNum][i]->box != boxNum)
			{
				cols[colNum][i]->possibles[val-1] = false;
				statusChanged = true;
			}
		}
	}
}
void Sudoku::subGroupExclusion()
{
	for (int i = 0; i < 9; i++)
		for (int val = 1; val <= 9; val++)
		{
			lineSubGroup(rows[i], val);
			lineSubGroup(cols[i], val, false);
			boxSubGroup(boxes[i], val);
		}
}
void Sudoku::tuplesInGroup(SudokuSquare **group)
{
	set<int> usedVals;
	set<int> freeVals;
	set<int> combVals;

	// Make the usedVals set
	for (int i = 0; i < 9; i++)
		if (group[i]->value != 0)
			usedVals.insert(group[i]->value);
	// Make the freeVals set
	for (int i = 1; i <= 9; i++)
		if (!usedVals.count(i))
			freeVals.insert(i);
	// Calculate the number of combinations
	int numCombinations = 1;
	int numFree = freeVals.size();
	int *freeV = new int[numFree];
	int index = 0;
	for (set<int>::iterator it = freeVals.begin(); it != freeVals.end(); it++)
	{
		freeV[index] = *it;
		index++;
	}
	while (numFree > 0)
	{
		numCombinations *= 2;
		numFree--;
	}
	// For each combination, see if there is a hidden tuple
	// If so, remove the values in freeVals from the possibles in the other 
	// squares.
	for (int comb = 0; comb < numCombinations; comb++)
	{
		makeCombination(combVals, freeV, comb);
		// There is a hidden tuple if size of tuple is exactly equal number of squares whose possibles are a subset of combVals
		// This is where there are problems!!!
		int numSubSets = 0;
		set<int> subSetIndices;
		// Find the squares whose possibles are a subset of combVals
		for (int k = 0; k < 9; k++)
		{
			if (group[k]->value == 0)
			{
				bool isSubSet = true;
				for (int j = 0; j < 9; j++)
					if (group[k]->possibles[j] && !combVals.count(j+1)) // Off by 1 error?
						isSubSet = false;

				if (isSubSet)
				{
					numSubSets++;
					subSetIndices.insert(k);
				}
			}
		}
		// If there is a hidden tuple, remove the numbers in the tuple from     
		// the other squares.
		if (numSubSets == combVals.size())
		{
			for(set<int>::iterator it = combVals.begin(); 
				it != combVals.end(); it++)
			{
				for (int i = 0; i < 9; i++)
				{
					if (!subSetIndices.count(i) && group[i]->value == 0)
					{
						if (group[i]->possibles[(*it)-1])
						{
							group[i]->possibles[(*it)-1] = false;
							statusChanged = true;
						}
					}
				}
			}
		}
	}
}
void Sudoku::makeCombination(set<int>& combVals, const int freeVals[], 
						 int comb)
{
	combVals.clear();
	int index = 0;
	while(comb > 0)
	{
		if (comb%2)
			combVals.insert(freeVals[index]);
		index++;
		comb /= 2;
	}
}
void Sudoku::hiddenTuples()
{
	//tuplesInGroup(boxes[6]);
	for (int i = 0; i < 9; i++)
	{
		tuplesInGroup(boxes[i]);
		tuplesInGroup(rows[i]);
		tuplesInGroup(cols[i]);
	}
}

void Sudoku::solve()
{
	statusChanged = true;
	while(statusChanged)
	{
		statusChanged = false;
		// Simple Logic
		refreshPossibles();
		possiblesSingletons();
		refreshPossibles();
		uniquesInGroups();
		refreshPossibles();

		// Advanced Logic
		if (!statusChanged && !isSolved())
		{
			subGroupExclusion();
			hiddenTuples();
		}
		//cout << *this << endl;
	}
}
bool Sudoku::isSolved()
{
	for (int i = 0; i < 9; i++)
		for (int j = 0; j < 9; j++)
			if (squares[i][j].value == 0)
				return false;
	return true;
}
int Sudoku::getCornerNum()
{
	return squares[0][0].value * 100 
		+ squares[0][1].value * 10 
		+ squares[0][2].value;

}

istream& operator>>(istream& ins, Sudoku& target)
{
	int in;
	for (int i = 0; i < 9; i++)
	{
		ins >> in;
		int tenner = 100000000;
		for (int j = 0; j < 9; j++)
		{
			target.squares[i][j] = SudokuSquare(in / tenner);
			in %= tenner;
			tenner /= 10;
		}
	}
	target.initializePointers();
	return ins;
}
ostream& operator<<(ostream& out, const Sudoku& source)
{
	for (int i = 0; i < 9; i++)
	{
		if (i==3 || i==6)
			out << "---+---+---\n";
		for (int j = 0; j < 9; j++)
		{
			if (j==3 || j==6)
				out << '|';
			out << source.squares[i][j].value;
		}
		out << endl;
	}
	return out;
}
