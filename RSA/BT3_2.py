import libraries

def findM(n, e, c):
    p, q = libraries.fermat(n)
    phiN = (p - 1) * (q - 1)
    d = libraries.moduloInverse(e, phiN)
    m = pow(c, d, n)
    return m


n = 2112911153
e = 101
c = 279116279
print("2. 1. m = ", findM(n, e, c))

n = 14362066833408544673
e = 101
c = 11361370803024022411
print("2. 2. m = ", findM(n, e, c))

n = 256716203167233510573625242978135122243
e = 101
c = 49125737493624903754363666821533332965
print("2. 3. m = ", findM(n, e, c))