import libraries
import math
import random
import time

def timer(fn):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = fn(*args, **kwargs)
        end_time = time.time()
        print("total run-time of %r: %f ms" % (fn.__name__, (end_time - start_time) * 1000))
        return result
    return wrapper

@timer
def keygen(lamda):
    p = libraries.randomPrimeNumber(lamda//2 - 1)
    q = libraries.randomPrimeNumber(lamda//2)
    n = p * q
    phiN = (p - 1) * (q - 1)
    e = 3;
    while e < phiN:
        if math.gcd(e, phiN) == 1:
            break
        e += 2
    d = libraries.moduloInverse(e, phiN)
    return [n, e, d]

@timer
def encryption(n, e, m):
    c = libraries.pow(m, e, n)
    return c

@timer
def decryption(n, d, c):
    m = libraries.pow(c, d, n)
    return m

lamda = 32
for i in range(1, 10):
    n, e, d = keygen(lamda)
    print("n = ", n)
    print("e = ", e)
    print("d = ", d)
    m = random.randint(0, int(math.pow(2, lamda/2 - 1)))
    print("m random = ", m)
    c = encryption(n, e, m)
    print("c = ", c)
    m = decryption(n, d, c)
    print("m = ", m)

lamda = 64
for i in range(1, 10):
    n, e, d = keygen(lamda)
    print("n = ", n)
    print("e = ", e)
    print("d = ", d)
    m = random.randint(0, int(math.pow(2, lamda/2 - 1)))
    print("m random = ", m)
    c = encryption(n, e, m)
    print("c = ", c)
    m = decryption(n, d, c)
    print("m = ", m)

lamda = 128
for i in range(1, 10):
    n, e, d = keygen(lamda)
    print("n = ", n)
    print("e = ", e)
    print("d = ", d)
    m = random.randint(0, int(math.pow(2, lamda/2 - 1)))
    print("m random = ", m)
    c = encryption(n, e, m)
    print("c = ", c)
    m = decryption(n, d, c)
    print("m = ", m)
