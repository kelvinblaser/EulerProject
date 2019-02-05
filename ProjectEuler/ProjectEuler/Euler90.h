/*****************************************************************************
Solution to Project Euler 88 - http://projecteuler.net/problem=90
Author: Kelvin Blaser
Date: 12-25-2012 

Making some cubes yeah!
*****************************************************************************/
#include <set>
#include <iostream>
using namespace std;

class Cube
{
public:
	int sides[6];
	Cube();
	void order();
	bool isValid();
	bool operator<(Cube leftSide);
	Cube operator=(Cube rightSide);
	friend ostream& operator<<(ostream& os, const Cube& c);
};

class CubeCombo
{
public:
	Cube cube1;
	Cube cube2;
	CubeCombo(Cube c1 = Cube(), Cube c2 = Cube());
	friend bool operator<(CubeCombo leftSide, CubeCombo rightSide);
	friend ostream& operator<<(ostream& os, const CubeCombo& cc);
};

int Euler90();
void buildCubes(set<int> c1, set<int> c2, int index, set<CubeCombo> *combinations);
void buildCombinations(set<int> c1, set<int> c2, set<CubeCombo> *combinations);
bool nextCube(Cube *cube, int minIndex);