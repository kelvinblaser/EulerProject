/******************************************************************************
Euler 485 - Maximum Number of Divisors
https://projecteuler.net/problem=485

Kelvin Blaser   2014.10.21
******************************************************************************/

#include <vector>
#include <deque>
#include <algorithm>
#include <iostream>
//using namespace std;

long long S(const long long u, const long long k);
void add_history(std::deque<int> &hist_d, std::deque<int> &hist_i, 
		 const long long d, const long long k);
void update_history(std::deque<int> &hist_d, std::deque<int> &hist_i);

int main(){
  std::cout << "S(20,5) = " << S(20,5) << std::endl;
  std::cout << "S(1000,10) = " << S(1000,10) << std::endl;
  std::cout << "S(100 000 000, 100 000) = " << S(100000000,100000) << std::endl;
  return 0;
}

long long S(const long long u, const long long k){
  std::vector <int> d(u+1);
  std::vector <int> M(u+1);
  std::deque <int> hist_d; // History of d(j)
  std::deque <int> hist_i; // How long ago d occured
  long long sum = 0;

  //const int MOD = 100000;

  // Sieve to calculate number of divisors
  std::fill(d.begin(), d.end(), 1);
  for (long long i = 2; i <= u; i++) {
    //if (i%MOD == 0)
    //  std::cout << "d: " << i << std::endl;
    for (long long j = i; j <= u; j+=i) {
      d[j] += 1;
    }
  }
  
  // Calculate M(n,k)
  for (long long i = u; i > 0; i--) {
    //if (i%MOD == 0)
    //  std::cout << "M: " << i << std::endl;
    // add to history
    add_history(hist_d, hist_i, d[i], k);
    // Set M(i,k)
    M[i] = hist_d.front();
    // update history
    update_history(hist_d, hist_i);
  }
  
  // std::cout << "i, d[i], M[i]\n";
  // for (int i = 1; i <= u; i++)
  //   std::cout << i << ", "<< d[i] << ", " << M[i] << std::endl;

  // Sum and return
  for (long long i = 1; i <= u-k+1; i++)
    sum += M[i];
  return sum;
}

void add_history(std::deque<int> &hist_d, std::deque<int> &hist_i, 
		 const long long d, const long long k) {
  while (!hist_d.empty() && hist_d.back() < d){
    hist_d.pop_back();
    hist_i.pop_back();
  }

  if (hist_d.empty()) {           // d is bigger than all in history
    hist_d.push_front(d);
    hist_i.push_front(k);
  }
  else if (hist_d.back() == d) {  // d is equal to at least one in history
    hist_i.pop_back();
    hist_i.push_back(k);
  }
  else {                          // d is not bigger than all, but is not in history
    hist_d.push_back(d);
    hist_i.push_back(k);
  }
  return;
}

void update_history(std::deque<int> &hist_d, std::deque<int> &hist_i) {
  // Decrement all
  for (std::deque<int>::iterator it = hist_i.begin(); it != hist_i.end(); it++)
    *it -= 1;
  
  // If initial is zero, remove it.
  if (hist_i[0] == 0) {
    hist_i.pop_front();
    hist_d.pop_front();
  }

  return;
}
