# Euler 198 - Ambiguous Numbers
# Kelvin Blaser    2014.05.16

from fractions import Fraction
from math import sqrt

def Euler198(denBound, ltNum=Fraction(1,100)):
	queue = [(1,0,0,1)]  # (p_last, p, q_last, q)
	ambis = []
	r = int(sqrt(denBound+1))
	count = 1
	n_ambis = 0
	while queue:
		p_last, p, q_last, q = queue.pop()
		conv = Fraction(p,q)
		g = abs(Fraction(p_last +p, q_last+q) - conv)
		if conv - ltNum > g:
			continue
		# print p_last, p, q_last, q
		for a in range(1,(r-q_last)/q + 1):
			p_next = p*a + p_last
			q_next = q*a + q_last
			if q_next <= r:
				queue.append((p, p_next, q, q_next))
				count += 1
			if a%2 == 1:
				continue
			p_next = p*(a/2) + p_last
			q_next = q*(a/2) + q_last
			ambiCandidate = (Fraction(p,q) + Fraction(p_next, q_next))/2
			if ambiCandidate < ltNum and ambiCandidate.denominator <= denBound:
				ambis.append(ambiCandidate)
				n_ambis += 1
	ambis.sort()
	print '%d iterations' % count
	print '%d ambiguous numbers between 0 and %d / %d with denominator bound %d.' % (n_ambis, ltNum.numerator, ltNum.denominator, denBound)
	return ambis, len(ambis)

