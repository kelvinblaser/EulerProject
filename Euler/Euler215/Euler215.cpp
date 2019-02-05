/*****************************************************************************
Euler 215 - Crack-free Walls
http://projecteuler.net/problem=215

------------------------------------------------------------------------------
First Attempt:  Recursive depth first search for solutions.  

	Result:	Failure 			Time: Way too long
------------------------------------------------------------------------------
Second Attempt: Memoized solution
				For each way of partitioning a row into bricks, there are a 
				certain number of ways of creating a wall n bricks high on 
				top of it.

				f(part, n) = sum(f(part, n-1)) where the sum runs over all 
				partitions that don't create a crack. (compatible partitions.)

				Enumerate partitions.
				Figure out which are compatible.
				Compute sum(f(part, 9)) over all partitions
	
	Result: Success		806844323190414		Time: About 115 s
------------------------------------------------------------------------------
Kelvin Blaser		2013-09-27
*****************************************************************************/
#include <iostream>
#include <iomanip>
#include <time.h>
#include <set>
#include <stack>
#include <vector>
#include <map>
#include <algorithm>
using namespace std;

class Wall {
public:
	int count_ways(int min_len, int max_len);
	void fill_row(int row_num, set<int> cracks, int min_len, int max_len);
	void place_brick();

	Wall(int ww, int hh){width=ww, height=hh;}

private:
	int width;
	int height;
	int count;
};

int Wall::count_ways(int min_len, int max_len) {
	count = 0;
	set<int> cracks;
	fill_row(1, cracks, min_len, max_len);
	return count;
}

void Wall::fill_row(int row_num, set<int> cracks, int min_len, int max_len) {
	vector<int> bricks;

	int len_tot = 0;
	int brick_len = min_len;

	bool done = false;
	if (row_num == 1) {
		cout << "Row: " << row_num << endl;
		for (int i = 0; i < bricks.size(); i++) 
			cout << ' ' << bricks[i];
		cout << endl;
	}
	do {
		if (brick_len + len_tot >= width) {
			if (brick_len + len_tot == width) {
				if (row_num == height) {
					count++;
				} 
				else {
					set<int> new_cracks;
					int crack = 0;
					for (int i = 0; i < bricks.size(); i++) {
						crack += bricks[i];
						new_cracks.insert(crack);
					}
					fill_row(row_num+1, new_cracks, min_len, max_len);
					if (row_num == 1) {
						cout << "Row: " << row_num << "\tCount: " << count << endl;
						for (int j = 0; j < bricks.size(); j++)
							cout << ' ' << bricks[j];
						cout << endl;
					}
				}
			}
			brick_len = max_len+1;
		}
		else if (cracks.count(len_tot + brick_len) > 0) {
			brick_len++;
		}
		else {
			bricks.push_back(brick_len);
			len_tot += brick_len;
			brick_len = min_len;
		}
		// Brick fits
			// Add brick
			// Reset brick_len
		// Brick makes crack
			// Don't Add brick
			// Increment brick
		// Brick finishes row
			// Go to next row
			// Set brick_len > max_len
		// Brick extends over row
			// Set brick_len > max_len

		if (brick_len > max_len) {
			while (!bricks.empty() && bricks[bricks.size()-1] == max_len) {
				len_tot -= bricks[bricks.size()-1];
				bricks.pop_back();
			}
			if (bricks.empty())
				done = true;
			else {
				len_tot -= bricks[bricks.size()-1];
				brick_len = bricks[bricks.size()-1]+1;
				bricks.pop_back();
			}
		}

		// If brick_len > max_len
			// Remove bricks until find one < max_len
			// Set brick_len to last brick + 1
	} while(!done);
}

//-------------------------------------------------------------
struct Partition {
	vector<int> bricks;
};

struct Key {
	Partition part;
	int level;
};

bool operator<(Partition pL, Partition pR);
bool operator<(Key kL, Key kR);

bool next_partition(vector<int> &bricks);
bool is_compatible(const Partition &p1, const Partition &p2);

_int64 count_ways(Partition p, int level, map<Partition, vector<Partition>> &ad_mat, map<Key, _int64> &memo);

int main() {
	int begin = clock();

	int width  = 32;
	int height = 10;

	// Create the partitions
	vector<Partition> partitions;
	vector<int> bricks(width / 2);
	fill(bricks.begin(),bricks.end(),2);
	Partition p;
	do {
		p.bricks = bricks;
		partitions.push_back(p);
	} while (next_partition(bricks));
	// Create the adjacency matrix
	map<Partition, vector<Partition>> ad_mat;
	for (vector<Partition>::iterator it = partitions.begin(); it != partitions.end(); it++) {
		for (vector<Partition>::iterator jt = it+1; jt != partitions.end(); jt++) {
			if (is_compatible(*it, *jt)) {
				if (ad_mat.count(*it) == 0)
					ad_mat[*it] = vector<Partition>(jt, jt+1);
				else
					ad_mat[*it].push_back(*jt);
				if (ad_mat.count(*jt) == 0)
					ad_mat[*jt] = vector<Partition>(it, it+1);
				else
					ad_mat[*jt].push_back(*it);
			}
		}
	}
	// Memoized solution
	map<Key, _int64> memo;
	_int64 ans = 0;
	for (vector<Partition>::iterator it = partitions.begin(); it != partitions.end(); it++)
		ans += count_ways(*it, height-1, ad_mat, memo);

	cout << ans << endl;
	
	int end = clock();
	cout << endl << end - begin << endl;
	system("pause");
	return 0;
}

bool next_partition(vector<int> &bricks) {
	int free_space = 0;
	do {
		free_space += bricks.back();
		bricks.pop_back();
	} while(!bricks.empty() && (bricks.back() == 3 || free_space < 3));

	if (bricks.empty())
		return false;

	free_space += bricks.back();
	bricks.pop_back();

	if (free_space % 2 == 0) {
		bricks.push_back(3);
		for (int i = 0; i < free_space-6; i+=2)
			bricks.push_back(2);
		bricks.push_back(3);
	}
	else {
		bricks.push_back(3);
		for (int i = 0; i < free_space-3; i+=2)
			bricks.push_back(2);
	}

	return true;
}

bool is_compatible(const Partition &p1, const Partition &p2) {
	int len1 = 0;
	int len2 = 0;
	vector<int>::const_iterator it1 = p1.bricks.begin();
	vector<int>::const_iterator it2 = p2.bricks.begin();
	while(it1 != p1.bricks.end() && it2 != p2.bricks.end()) {
		if (len1 == len2 && len1 != 0)
			return false;
		if (len1 < len2) {
			len1 += *it1;
			it1++;
		}
		else {
			len2 += *it2;
			it2++;
		}
	}
	return true;
}

bool operator<(Partition pL, Partition pR) {
	for (int i = 0; i < min(pL.bricks.size(), pR.bricks.size()); i++) {
		if (pL.bricks[i] < pR.bricks[i])
			return true;
		if (pL.bricks[i] > pR.bricks[i])
			return false;
	}

	return (pL.bricks.size() < pR.bricks.size());
}

bool operator<(Key kL, Key kR) {
	if (kL.level < kR.level)
		return true;
	if (kL.level > kR.level)
		return false;
	return (kL.part < kR.part);
}

_int64 count_ways(Partition p, int level, map<Partition, vector<Partition>> &ad_mat, map<Key, _int64> &memo) {
	if (level == 0)
		return 1;
	Key key;
	key.level = level;
	key.part  = p;
	if (memo.count(key) == 1)
		return memo[key];

	_int64 sum = 0;
	for (vector<Partition>::const_iterator it = ad_mat[p].begin(); it != ad_mat[p].end(); it++)
		sum += count_ways(*it, level-1, ad_mat, memo);

	memo[key] = sum;
//	cout << '(';
//	for (int i = 0; i < p.bricks.size(); i++)
//		cout << p.bricks[i] << ',';
//	cout << "\b)  " << level  << "\t" << sum << endl;
	return sum;
}
	