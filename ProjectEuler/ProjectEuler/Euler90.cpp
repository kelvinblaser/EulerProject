#include "Euler90.h"
#include <set>
#include <iostream>
#include <algorithm>
#include <fstream>
using namespace std;

class doubleDigits
{
public:
	int tens;
	int ones;
	doubleDigits(int t = 0, int o = 0){tens = t; ones = o;} 
};

const doubleDigits SQUARES[] = {doubleDigits(0,1),
								doubleDigits(0,4),
								doubleDigits(0,6),
								doubleDigits(1,6), 
								doubleDigits(2,5),
								doubleDigits(3,6),
								doubleDigits(4,6),
								doubleDigits(6,4),
								doubleDigits(8,1)};

int Euler90()
{
	// Build Valid Cube Combinations
	set<CubeCombo> combinations;
	set<int> c1;
	set<int> c2;
	c1.insert(0);
	c2.insert(1);
	buildCubes(c1,c2,1,&combinations);

	// Count them
	return combinations.size();
}

void buildCubes(set<int> c1, set<int> c2, int index, set<CubeCombo> *combinations)
{
	if (index == 9)
	{
		// We are done.  Build the Combinations
		buildCombinations(c1, c2, combinations);
		// Deal with the 6-9 ambiguity
		if (c1.count(6))
		{
			c1.erase(6);
			c1.insert(9);
			buildCombinations(c1, c2, combinations);
			if (c2.count(6))
			{
				c2.erase(6);
				c2.insert(9);
				buildCombinations(c1, c2, combinations);
				c1.erase(9);
				c1.insert(6);
				buildCombinations(c1, c2, combinations);
			}
		}
		else if (c2.count(6))
		{
			c2.erase(6);
			c2.insert(9);
			buildCombinations(c1, c2, combinations);
		}
		return;
	}

	set<int> c1a = c1;
	set<int> c2a = c2;

	c1.insert(SQUARES[index].tens);
	c2.insert(SQUARES[index].ones);
	c1a.insert(SQUARES[index].ones);
	c2a.insert(SQUARES[index].tens);

	buildCubes(c1, c2, index+1, combinations);
	buildCubes(c1a, c2a, index+1, combinations);
}

void buildCombinations(set<int> c1, set<int> c2, set<CubeCombo> *combinations)
{
	if (c1.size() > 6 || c2.size() > 6)
		return;

	Cube cube1;
	Cube cube2;
	
	// Set the used up faces on the cubes
	int index1 = 0;
	for (set<int>::iterator it = c1.begin(); it != c1.end(); it++)
	{
		cube1.sides[index1] = *it;
		index1++;
	}
	int index2 = 0;
	for (set<int>::iterator it = c2.begin(); it != c2.end(); it++)
	{
		cube2.sides[index2] = *it;
		index2++;
	}

	// Fill in the remaining faces to create all valid cubes
	for (; index1 < 6; index1++)
		cube1.sides[index1] = 0;
	for (; index2 < 6; index2++)
		cube2.sides[index2] = 0;
	Cube ordered1 = cube1;
	Cube ordered2 = cube2;
	ordered1.order();
	ordered2.order();
	if (ordered1.isValid() && ordered2.isValid())
		combinations->insert(CubeCombo(ordered1, ordered2));

	do
	{
		ordered1 = cube1;
		ordered1.order();
		if (ordered1.isValid())
		{
			Cube cube2Iterated = cube2;
			do
			{
				ordered2 = cube2Iterated;
				ordered2.order();
				if (ordered2.isValid())
					combinations->insert(CubeCombo(ordered1, ordered2));
			}
			while (nextCube(&cube2Iterated, c2.size()));
		}
	}
	while (nextCube(&cube1, c1.size()));
}

bool nextCube(Cube *cube, int minIndex)
{
	int i = minIndex;
	while (i < 6 && cube->sides[i] == 9)
		i++;
	if (i == 6)
		return false;

	cube->sides[i]++;
	for (int j = minIndex; j < i; j++)
		cube->sides[j] = cube->sides[i];

	return true;
}

Cube::Cube()
{
	for (int i = 0; i < 6; i++)
		sides[i] = 0;
}

bool Cube::operator<(Cube leftSide)
{
	for(int i = 0; i < 6; i++)
	{
		if (sides[i] < leftSide.sides[i])
			return true;
		else if (sides[i] > leftSide.sides[i])
			return false;
	}
	return false;
}

Cube Cube::operator=(Cube rightSide)
{
	for (int i = 0; i < 6; i++)
		sides[i] = rightSide.sides[i];

	return *this;
}

void Cube::order()
{
	sort(sides, sides+6);
}

bool Cube::isValid()
{
	for (int i = 0; i < 5; i++)
		if (sides[i] == sides[i+1])
			return false;
	return true;
}

ostream& operator<<(ostream& os, const Cube& c)
{
	os << '(';
	for (int i = 0; i < 5; i++)
		os << c.sides[i] << ',';
	os << c.sides[5] << ')';

	return os;
}

CubeCombo::CubeCombo(Cube c1, Cube c2)
{
	if (c1 < c2)
	{
		cube1 = c1;
		cube2 = c2;
	}
	else
	{
		cube1 = c2;
		cube2 = c1;
	}
}

bool operator<(CubeCombo leftSide, CubeCombo rightSide)
{
	if (leftSide.cube1 < rightSide.cube1)
		return true;
	if (rightSide.cube1 < leftSide.cube1)
		return false;
	if (leftSide.cube2 < rightSide.cube2)
		return true;
	return false;
}

ostream& operator<<(ostream& os, const CubeCombo& cc)
{
	os << '{' << cc.cube1 << ',' << cc.cube2 << '}';
	return os;
}
