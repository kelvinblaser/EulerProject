"""Euler 445 - Retractions A

    f(n, a, b, x) = ax + b mod n
    f(n, a, b, x) is a retraction if f(f(x)) = f(x) for all 0 <= x < n

    f(f(x)) = a(ax + b) + b mod n
            = a^2x + b(a + 1) mod n =

    f(f(0)) = f(0) => ab + b = b mod n
                   => ab = 0 mod n

    f(f(x)) = a^2x + b mod n  (ab = 0 mod n)

    f(f(1)) = f(1) => a^2 + b = a + b mod n
                   => a^2 = a mod n
                   => a(a - 1) = 0 mod n

    From x = 0 and x = 1, we have the following conditions:
      ab = 0 mod n
      a(a - 1) = 0 mod n

    From these we can re-write the retraction condition

    f(f(x)) = ax + b = f(x)  which is true for all other x.
    x = 0, and x = 1 are sufficient to determine whether f is a retraction.

    R(n) is the number of retractions for n.

    If n is prime, then either a = 0 or a = 1.
    But we are not considering the case where a = 0. (f is just constant then.)
    If a = 1, then b = 0. 

    So for prime p, R(p) = 1

    For a prime power, p^m, if p divides a, then p does not divide a - 1.
    So p^m has to divide either a or a - 1.  So again, a = 0 or a = 1
    We have to have a = 1 and b = 0

    R(p^m) = 1

    a*(a - 1) = 0 mod n
    For each solution a to this equation, there are gcd(n, a) retractions.

    If n = prod(p^v_p), then there are prod((1 + p^v_p)).  But R(n) doesn't
    count the retractions where a = 0, so ...

    R(n) = prod((1 + p^v_p), p | n) - n

    So this tells us the function Q(n) = R(n) + n is multiplicative.
    Q(n) = prod(p | n, 1 + p^v_p) = R(n) + n
    Q(p^m) = 1 + p^m  for primes p
"""
import retractions

MOD = 10**9 + 7

class QPFAccumulator:
  """QPFAccumulator keeps track of Q as it changes multiplicatively.
  
  Here we keep track of n, Q(n), and PF(n) as we multiply or divide by
  new PrimeFactorizations.

  In all methods of this class, pf must be the PrimeFactorization of n.
  """
  def __init__(self, n: int, pf: retractions.PrimeFactorization):
    self.n = n
    self.pf = pf
    self.q = QFromPF(pf)

  def Mul(self, n: int, pf: retractions.PrimeFactorization):
    self.n *= n
    self.n %= MOD
    for p, dv in pf.items():
      v = self.pf[p]
      if v > 0:
        # Divide by the old term.
        self.q *= pow((1 + pow(p, v, MOD)), MOD - 2, MOD)
      self.q *= 1 + pow(p, v + dv, MOD)  # Multiply by the new.
      self.q %= MOD
      self.pf[p] += dv

  def Div(self, n: int, pf: retractions.PrimeFactorization):
    self.n *= pow(n, MOD - 2, MOD)
    self.n %= MOD
    for p, dv in pf.items():
      v = self.pf[p]
      # Divide by the old term.
      self.q *= pow((1 + pow(p, v, MOD)), MOD - 2, MOD)
      if v > dv:
        # Multiply by the new.
        self.q *= 1 + pow(p, v - dv, MOD)
      self.q %= MOD
      self.pf[p] -= dv

def QFromPF(pf: retractions.PrimeFactorization) -> int:
  q = 1
  for p, v in pf.items():
    q *= (1 + pow(p, v, MOD))
    q %= MOD
  return q

def Euler445(N: int) -> int:
  """Returns sum(R(N choose x), x = 1 .. N - 1)."""
  # Get the prime factorizations for 1 through N
  pfs = PrimeFactorizations(N)
  # Iteratively calculate the prime factorizations of N choose x
  # Keep track of Q(NCx) and NCx prime factorizations
  # Sum up R(NCx)
  r = 0
  acc = QPFAccumulator(1, retractions.PrimeFactorization())
  for k in range(1, N):
    acc.Mul(N + 1 - k, pfs[N + 1 - k])
    acc.Div(k, pfs[k])
    r += acc.q - acc.n
    if k % 100_000 == 0:
      print(k, acc.n, acc.q)
  return r % MOD

def PrimeFactorizations(N: int) -> list[retractions.PrimeFactorization]:
  """Returns the prime factorizations of all integers up to N."""
  pfs = [retractions.PrimeFactorization() for _ in range(N + 1)]
  nums = list(range(N + 1))
  for p in range(2, N + 1):
    if nums[p] != p:
      # Not a prime.
      continue
    for x in range(p, N + 1, p):
      while nums[x] % p == 0:
        pfs[x][p] += 1
        nums[x] //= p
  return pfs


if __name__ == '__main__':
  for x in [10, 100_000, 10_000_000]:
    print(f'{x} => {Euler445(x)}')
