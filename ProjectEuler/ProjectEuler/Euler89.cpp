#include <string>
#include <vector>
#include <fstream>
#include "Euler89.h"
using namespace std;

int Euler89(string filename)
{
	vector<int> nums;
	// Read the numbers from file and get the number of symbols
	int initialNumSymbols = readNumsFromFile(filename, &nums);
	// Create new Roman numerals and count symbols
	int finalNumSymbols = 0;
	for (int i = 0; i < nums.size(); i++)
	{
		string newNumeral = makeRomanNumeral(nums[i]);
		finalNumSymbols += newNumeral.length();
	}
	return initialNumSymbols - finalNumSymbols;
}

int readNumsFromFile(string filename, vector<int> *nums)
{
	ifstream fin;
	fin.open(filename);

	int numSymbols = 0;
	if (fin.is_open())
	{
		while(!fin.eof())
		{
			string numeral;
			fin >> numeral;
			numSymbols += numeral.length();
			nums->push_back(numeralToInt(numeral));
		}
	}
	fin.close();
	return numSymbols;
}

string makeRomanNumeral(int n)
{
	string num = "";
	for (int i = 0; i < NUM_SYMBOLS; i++)
	{
		int numberOfSymbol = n / ROMAN_SYMBOLS[i].value;
		for (int j = 0; j < numberOfSymbol; j++)
			num += ROMAN_SYMBOLS[i].symbol;
		n %= ROMAN_SYMBOLS[i].value;
	}
	return num;
}

int numeralToInt(string numeral)
{
	int n = 0;
	int i = 0;
	for (; i < numeral.length()-1; i++)
	{
		char symb = numeral[i];
		switch (symb)
		{
		case 'M': n += 1000;
			break;
		case 'D': n += 500;
			break;
		case 'L': n += 50;
			break;
		case 'V': n += 5;
			break;
		default: char symb2 = numeral[i+1];
			switch (symb)
			{
			case 'C': 
				switch (symb2)
				{
				case 'M': n += 900;
					i++;
					break;
				case 'D': n += 400;
					i++;
					break;
				default:
					n += 100;
				}
				break;
			case 'X':
				switch (symb2)
				{
				case 'C': n += 90;
					i++;
					break;
				case 'L': n += 40;
					i++;
					break;
				default:
					n += 10;
				}
				break;
			case 'I':
				switch (symb2)
				{
				case 'X': n += 9;
					i++;
					break;
				case 'V': n += 4;
					i++;
					break;
				default:
					n += 1;
				}
				break;
			}
		}
	}

	if (i == numeral.length()-1)
	{
		char symb = numeral[numeral.length()-1];
		switch (symb)
		{
		case 'M': n += 1000;
			break;
		case 'D': n += 500;
			break;
		case 'C': n += 100;
			break;
		case 'L': n += 50;
			break;
		case 'X': n += 10;
			break;
		case 'V': n += 5;
			break;
		case 'I': n += 1;
			break;
		}
	}

	return n;
}

RomanSymbolValuePair::RomanSymbolValuePair(string symb, int val)
{
	symbol = symb;
	value = val;
}