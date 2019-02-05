/*****************************************************************************
Solution to Project Euler 88 - http://projecteuler.net/problem=89
Author: Kelvin Blaser
Date: 12-24-2012 
*****************************************************************************/
#include <string>
#include <vector>
using namespace std;

int Euler89(string filename);
int readNumsFromFile(string filename, vector<int> *nums);
string makeRomanNumeral(int n);
int numeralToInt(string numeral);

class RomanSymbolValuePair
{
public:
	RomanSymbolValuePair(string symb = "I", int val = 0);
	string symbol;
	int value;
};

const RomanSymbolValuePair ROMAN_SYMBOLS[] = {RomanSymbolValuePair("M", 1000),
											  RomanSymbolValuePair("CM", 900),
											  RomanSymbolValuePair("D", 500),
											  RomanSymbolValuePair("CD", 400),
											  RomanSymbolValuePair("C", 100),
											  RomanSymbolValuePair("XC", 90),
											  RomanSymbolValuePair("L", 50),
											  RomanSymbolValuePair("XL", 40),
											  RomanSymbolValuePair("X", 10),
											  RomanSymbolValuePair("IX", 9),
											  RomanSymbolValuePair("V", 5),
											  RomanSymbolValuePair("IV", 4),
											  RomanSymbolValuePair("I", 1)};

const int NUM_SYMBOLS = 13;
