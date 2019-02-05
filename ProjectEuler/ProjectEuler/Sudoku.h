/*****************************************************************************
Sudoku - A class for the number game Sudoku
Author - Kelvin Blaser
Date - 1/2/2013

---****   SudokuSquare - class    ****----
A class used by Sudoku. A Sudoku object consists of 81 squares.  Not meant to
be used outside of Sudoku.  Should be nested class?
MEMBERS of SudokuSquare
	value	-	The value of the square.  This should be  a number 
				between 0 and 9 inclusive.  0 indicates the value is unknown.
	possibles -	An array of 9 bools which indicate which numbers value can 
				possibly take.  As the board is solved, the possible values 
				are set to false until only one remains.  When this is the 
				case, the square is set to the corresponding value.
	row	-	The row number of the square within the Sudoku object.
	col -	The column number of the square
	box	-	The box number of the square.

CONSTRUCTOR of SudokuSquare
	Precondition: val is an integer between 0 and 9 inclusive. val defaults to
		0.
	Postcondition: The square's value is set to val, and the possibles are all
		set to appropriate values.  A value of 0 indicates an unknown, and all
		possibles are true.  For any other value, the possibles are all set to
		false except the possible corresponding to value.
	INPUTS:		val		- Initial value of the square.  Defaults to 0
	OUTPUTS:	NONE

----****    Sudoku - class    ****----
DEFAULT CONSTRUCTOR of Sudoku
	Postcondition: The 81 SudokuSquares are initialized to 0, and the row and 
		column pointers are are all set.

COPY CONSTRUCTOR
	Sudoku(const Sudoku &source)
		Postcondition: The new Sudoku object has the same squares as source.

MEMBER FUNCTIONS
	void initializePointers() - only called by constructors
		Precondition: Function is being called by a constructor
		Postcondition: rows, cols, and boxes pointers all point to the correct
			squares

	void refreshPossibles() - loops through the squares and eliminates any set
				values from the possibles of the squares in the same row, 
				column and box
		Precondition: this is a valid Sudoku object.
		Postcondition: Possibles are updated.

	void possiblesSingletons() - loops through the squares and for each square
				with only one true possible, sets that square's value to the 
				corresponding possible.
		Precondition: this is a valid Sudoku object.
		Postcondition: Singletons are set.

	void uniquesInRows() - Looks for squares which are the only ones that can
				be a particular value
		Precondition: this is a valid Sudoku object.
		Postcondition: Uniques in rows are set.


	void solve() - The main function for this object.  Solves the Sudoku board.
		Precondition: this is a valid Sudoku board.
		Postcondition: The Sudoku board is solved.

OPERATOR OVERLOADS
	operator>> - Extraction operator.  Reads the Sudoku board from the format
			used in http://projecteuler.net/problem=96
	operator<< - Writes the Sudoku board in an easy to read format.
*****************************************************************************/
#pragma once
#include <iostream>
#include <set>
using namespace std;

// Could be nested class in Sudoku?
class SudokuSquare
{
public:
	SudokuSquare(int val = 0);
	~SudokuSquare(void);

	// All public for ease of access. Only used as private members in 
	// a Sudoku object.
	bool possibles[9];
	int value;
	int row;
	int col;
	int box;
};

class Sudoku
{
	SudokuSquare squares[9][9]; // The board
	SudokuSquare *rows[9][9]; // Pointers to the board.  The first index is the
	SudokuSquare *cols[9][9]; // row/col/box number; the second indicates the 
	SudokuSquare *boxes[9][9]; // square it with in the row/col/box it points 
								// to.

	bool statusChanged; // Used in solve to determine if anything has changed.

	void initializePointers(); // A loop that initializes rows, cols, boxes.
	void refreshPossibles();
	// Simple Logic
	void possiblesSingletons();
	void uniquesInGroups();
	void uniqueValInGroup(SudokuSquare **group, int val); 
	// Advanced Logic
	void lineSubGroup(SudokuSquare **line, int val, bool isRow = true);
	void boxSubGroup(SudokuSquare **box, int val);
	void subGroupExclusion();
	void tuplesInGroup(SudokuSquare **group);
	void makeCombination(set<int>& combVals, const int freeVals[], 
						 int comb);
	void hiddenTuples();

public:
	Sudoku(void);
	Sudoku(const Sudoku &source);
	~Sudoku(void);

	void solve();
	bool isSolved();
	int getCornerNum();

	friend istream& operator>>(istream& ins, Sudoku& target);
	friend ostream& operator<<(ostream& out, const Sudoku& source);
};
