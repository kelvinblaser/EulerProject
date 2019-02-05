# Euler 192 - Best Approximations
# Kelvin Blaser   2014.05.16

from math import sqrt
from decimal import Decimal, getcontext

getcontext().prec = 60

def bestApproxSqrt(n, denBound):
	''' Returns the numerator and denominator of the best rational 
	approximation to sqrt(n) with denominator bound denBound'''
	nD = Decimal(n)
	a0 = int(sqrt(n))
	# If n is a perfect square, the best approximation is the sqrt itself
	if a0*a0 == n:
		return (a0,1)
	if (a0+1)*(a0+1) == n:
		return (a0+1, 1)
	
	# Calculate continued fraction until denominator > denBound
	m = q = 0
	d = q_next = p = 1
	a = p_next = a0
	while q_next <= denBound:
		p, p_last, q, q_last = (p_next, p, q_next, q)
		m = d*a - m
		d = (n - m*m) / d
		a = (a0 + m) / d
		p_next = p*a+p_last
		q_next = q*a+q_last
		# print '%d / %d' % (p_next,q_next)
		
	# Decrement a (the last value of a) until and if denominator <= denBound
	# If denominator <= denBound, return numerator and denominator
	for x in range(a-1,a/2, -1):
		p_next = p*x+p_last
		q_next = q*x+q_last
		if q_next <= denBound:
			# print 'Decremented'
			return (p_next, q_next)
	# Special case if a is even
	if a%2==0:
		p_next = p*a/2 + p_last
		q_next = q*a/2 + q_last
		if (q_next <= denBound and abs(Decimal(p_next)/Decimal(q_next) - 
					nD.sqrt()) < abs(Decimal(p)/Decimal(q) - nD.sqrt())):
			# print 'Even Exception'
			return (p_next, q_next)
	# If all else fails, return the previous truncated continued fraction
	# print 'Fail'
	return (p, q)
	
def isSquareFree(x):
	r = int(sqrt(x))
	if r*r == x or (r+1)*(r+1) == x:
		return False
	return True	

def Euler192(N, denBound):
	s = 0
	for n in range(2,N+1):
		p,q = bestApproxSqrt(n,denBound)
		# print 'sqrt(%d) => %d / %d  \t\t %f => %f' % (n,p,q, sqrt(n), float(p)/q)
		# if q == denBound:
			# print n, p, q
		if q != 1:
			s += q
	return s
		
	
	# return sum([bestApproxSqrt(n,denBound)[1] for n in range(2,N+1) 
				# if isSquareFree(n)])
	# num, den = bestApproxSqrt(N,denBound)
	# print '%d / %d' %(num, den)

if __name__ == '__main__':
	# print Euler192(13,30)
	print Euler192(10**5,10**12)