#include <vector>
using namespace std;

class Triple
{
public:
	Triple();
	Triple(int A, int B, int C);
	int a;
	int b;
	int c;
};

long Euler86(int limit);
void generateTriples(vector<Triple> *trips, int max);
long countCuboidsInTriple(Triple trip, int M);
long countCuboids(vector<Triple> *trips, int M);