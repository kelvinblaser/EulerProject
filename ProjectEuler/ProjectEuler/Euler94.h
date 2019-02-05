/*****************************************************************************
Solution to Project Euler 88 - http://projecteuler.net/problem=93
Author: Kelvin Blaser
Date: 12-25-2012 

Almost Equilateral
 1st Try - Brute Force
	- Too large of numbers (x^2 for x = 333,333,333; etc.)
	- Can't really get MPIR to work with cout  ?
 2nd Try - Primitive Pythagorean Triples with m < sqrt(perimeterLimit / 3)
    - Way better.  < 3ms
 Could try solving Pell equation x^2 - 3y^2 = 1.
*****************************************************************************/
//using namespace std;

//long Euler94(double perimeterLimit);