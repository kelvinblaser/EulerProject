 #include <vector>
 #include <algorithm>
 #include <cmath>
 #include <iostream>

const int MAX = 64000;
bool isSquare(long long n);

int main() {
   std::vector<long long> sigma2(MAX+1);
   std::fill(sigma2.begin(), sigma2.end(), 1);
   for (int i = 1; i <= MAX; i++) {
     long long i2 = i*i;
     for (int j = i; j <= MAX; j+=i) {
       sigma2[j] += i2;
     }
   }

   std::cout << std::count_if(sigma2.begin()+1, sigma2.end(), isSquare) << std::endl;
  return 0;
}

 bool isSquare(long long n) {
   double root = std::sqrt((double) n);
   long long r = (long long) (root + 0.5);
   return (r*r == n);
 }
  
