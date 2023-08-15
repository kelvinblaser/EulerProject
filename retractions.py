"""retractions defines common functions and classes for Euler 445 - 447."""
import collections

class PrimeFactorization(collections.defaultdict):
  def __init__(self):
    super().__init__(int)

  def __repr__(self):
    return 'x'.join([self.TermString(p, v) for p, v in self.items() if v > 0])

  def TermString(self, p, v):
    if v == 0: return ''
    if v == 1: return f'{p}'
    return f'{p}^{v}'