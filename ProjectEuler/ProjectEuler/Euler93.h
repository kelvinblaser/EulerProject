/*****************************************************************************
Solution to Project Euler 88 - http://projecteuler.net/problem=93
Author: Kelvin Blaser
Date: 12-25-2012 
*****************************************************************************/
using namespace std;

enum Operator {ADD, SUB, MUL, DIV};

int Euler93();
bool nextNumCombo(int *numSet);
bool nextNumPermute(int *numSet);
bool nextOps(Operator *ops);
void reverseArray(int *numSet, int startIndex, int endIndex);