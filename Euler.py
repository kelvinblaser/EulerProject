# Some useful routines for project Euler Problems
from __future__ import print_function
from __future__ import division
import operator
import numpy as np
import smtplib

def sendGmail(msgText, subject, username, password,
              fromaddr, toaddr):
    import smtplib
    from email.mime.text import MIMEText

    msg = MIMEText(msgText)
    msg['Subject'] = subject
    msg['From'] = fromaddr
    msg['To'] = toaddr

    try:
        server = smtplib.SMTP('smtp.gmail.com',587)
        server.ehlo()
        server.starttls()
        server.login(username,password)
        server.sendmail(fromaddr, [toaddr], msg.as_string())
        server.close()
        print('Succesfully sent mail')
    except:
        print('Failed to send mail')

    return

def sendVerizonText(msgText, subject, username, password,
                    fromaddr, phoneNumber):
    ''' Sends an email from fromaddr as a text message to phoneNumber.
    phoneNumber needs to be a string in the form '1234567890' and needs to be
    a Verizon client.'''
    toaddr = phoneNumber+'@vtext.com'
    sendGmail(msgText, subject, username, password, fromaddr, toaddr)
    return


def memoize(f):
    cache = {}
    def wrapped(*args):
        if args not in cache:
            cache[args] = f(*args)
        return cache[args]
    return wrapped



def restrictedPrimeFactorizations(primes, N):
    ''' Generates all numbers less than N such that their prime factorizations
    only include primes in the set primes '''
    ps = [p for p in primes if p < N]
    ps.sort()
    exp = [0]*(len(ps))
    ix = 0
    n = 1
    yield n
    while ix < len(ps) and ps[ix] < N:
        n*= ps[ix]
        exp[ix] += 1
        if n >= N:
            n //= ps[ix] ** exp[ix]
            exp[ix] = 0
            ix += 1
        else:
            yield n
            ix = 0
    return


def tonelliShanks(n,p):
    '''Computes the square root of n modulo p (You need to guarantee it has
    a square root)'''
    if n == 0:
        return 0
    # Write p-1 = q*2^s
    q = p-1
    s = 0
    while q%2 == 0:
        q //= 2
        s += 1
    if s == 1:   # p = 3 mod 4
        return pow(n,(p+1)//4,p)
    # Find non-residue z
    z = 2
    while pow(z,p//2,p) != p-1:
        z += 1
    c = pow(z, q, p)
    r = pow(n, (q+1)//2, p)
    t = pow(n, q, p)
    m = s
    while t != 1:
        i = 0
        t2 = t
        while t2 != 1:
            t2 = (t2*t2)%p
            i += 1
        b = pow(c,2**(m-i-1),p)
        r = (r*b)%p
        t = (t*b*b)%p
        c = (b*b)%p
        m = i
    return r


def positivePell(D,N):
    ''' Generater that yields the first N solutions to the Pell equation
        x^2 - Dy^2 = 1 '''
    a0 = int(D**0.5)
    a = a0
    if a*a == D or (a+1)*(a+1) == D:
        return
    p,q,P,Q = a,1,0,1
    p1,q1,P1,Q1,a1 = p,q,P,Q,a
    P = a0
    Q = D - a0*a0
    a = (a0 + P)//Q
    p = a0*a + 1
    q = a
    n = 1
    count = 0
    while count < N:
        if n%2 == 0 and Q == 1:
            count += 1
            yield (p1,q1)
        p2,q2 = p1,q1
        n,p1,q1,P1,Q1,a1 = n+1,p,q,P,Q,a
        P = a1*Q1 - P1
        Q = (D-P*P)//Q1
        a = (a0 + P)//Q
        p = a*p1 + p2
        q = a*q1 + q2

def isQuadResidue(n,p):
    ''' Tests to see if n is a quadratic residue mod p, where p is odd and
    prime.  p must be prime to guarantee a correct response.'''
    if n == 0 or pow(n,p//2,p) == 1:
        return True
    return False


def laggedFibonacci(n, MOD=1000000):
    ''' Lagged Fibonacci Generator '''
    S = [(100003 - 200003*k + 300007*k*k*k)%MOD for k in range(1,56)]
    for k in range(1,56):
        if k > n:
            return
        yield S[k-1]
    for j in range(k,n+1):
        S.append((S[-24]+S[-55])%MOD)
        S.pop(0)
        yield S[-1]
    return

def matModExp(A,e,m):
    ''' Computes A^e mod m where A is a square numpy array representing the
    matrix to be exponentiated, e is the non-negative integer exponent and m is
    the modulus. '''
    if e == 0:
        return np.eye(A.shape[0],dtype=np.int64)
    if e == 1:
        return A

    X = matModExp(A,e//2,m)
    X = X.dot(X) % m
    if (e%2 == 1):
        X = X.dot(A) % m
    return X



def uniquePermutations(iterator):
    '''Generates the unique permutations of the elements in iterator.  Requires
    elements which can be compared with <, <=, and == .

    This is different from itertools.permutations in that if there are repeated
    elements, it will not generate repeated permutations.

    For example, let iterator = [1,1,2,2]
    itertools.permutations          uniquePermutations
    ----------------------          ------------------
    [1,1,2,2]                       [1,1,2,2]
    [1,1,2,2]                       [1,2,1,2]
    [1,2,1,2]                       [1,2,2,1]
    [1,2,2,1]                       [2,1,1,2]
    [1,2,1,2]                       [2,1,2,1]
    [1,2,2,1]                       [2,2,1,1]
    [1,1,2,2]
    [1,1,2,2]
    [1,2,1,2]
    [1,2,2,1]
    [1,2,1,2]
    [1,2,2,1]
    [2,1,1,2]
    [2,1,2,1]
    [2,1,1,2]
    [2,1,2,1]
    [2,2,1,1]
    [2,2,1,1]
    [2,1,1,2]
    [2,1,2,1]
    [2,1,1,2]
    [2,1,2,1]
    [2,2,1,1]
    [2,2,1,1] '''
    pool = list(iterator)
    pool.sort()
    n = len(pool)
    if n == 0:
        return
    yield tuple(pool)
    if n == 1:
        return
    while True:
        # Find the first ix from the right where pool[ix] < pool[ix+1]
        ix = n-2
        while ix >= 0 and pool[ix+1] <= pool[ix]:
            ix -= 1
        if ix == -1:
            return # We're done if there is no such index

        # Find the first jx from the right where pool[ix] < pool[jx]
        jx = n-1
        while pool[jx] <= pool[ix]:
            jx -= 1

        # Swap pool[jx] and pool[ix]
        temp = pool[jx]
        pool[jx] = pool[ix]
        pool[ix] = temp

        # Reverse the pool to the right of ix and yield
        pool[ix+1:] = pool[:ix:-1]
        yield tuple(pool)
