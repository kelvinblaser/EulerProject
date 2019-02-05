#include <set>
#include <map>
using namespace std;

class Point
{
public:
	Point(long x0 = 0, long y0 = 0);
	friend bool operator<(Point lSide, Point rSide);
	long x;
	long y;
};

long Euler408(long limit, long modder);
long modChoose(long n, long k, long modder);
// modder must be prime and > n.

void calculateIaps(set<Point> *iaps, long limit);



