import random
import math

from gmpy2 import isqrt

def factor(n):
    s = 0
    while ((n & 1) == 0):
        s +=1 
        n >>= 1
    return [s, n]

def pow(a, d, n):
    result = 1
    a = a % n
    while d > 0:
        if d & 1:
        	result = result * a % n
        d >>= 1
        a = a * a % n
    return result

def test_a(s, d, n, a):
    if n == a:
    	return True
    p = pow(a, d, n)
    if p == 1:
    	 return True
    while s > 0:
        if p == n-1:
        	return True
        p = p * p % n
        s -= 1
    return False

def miller(n):
    if n < 2:
        return False
    if n & 1 == 0:
        return n == 2
    s, d = factor(n - 1)
    a = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37]
    for i in a:
        if test_a(s, d, n, i) == False:
            return False
    return True

def randomPrimeNumber(n):
    x = 0
    while miller(x) == False:
        x = random.getrandbits(n)
    return x

def moduloInverse(a, m):
    xa = 1
    xm = 0
    n = m
    while m != 0:
        q = a // m
        xr = xa - q * xm
        xa = xm
        xm = xr
        r = a % m
        a = m
        m = r
    if xa < 0:
        xa += n
    return xa

def fermat(n):
    a = isqrt(n)
    b2 = a*a - n
    b = isqrt(n)
    count = 0
    while b*b != b2:
        a = a + 1
        b2 = a*a - n
        b = isqrt(b2)
        count += 1
    p = a+b
    q = a-b
    assert n == p * q
    return p, q