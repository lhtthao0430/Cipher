import libraries
import binascii

def findM(n, e, c):
    # Using https://www.alpertron.com.ar/ECM.HTM to find p, q
    p = 39947403757434948516359261516230412449
    q = 252843356915213360241123618656441151517 
    phiN = (p - 1) * (q - 1)
    d = libraries.moduloInverse(e, phiN)
    m = pow(c, d, n)
    return m

n = 10100435666077259960314423346452149560810676634535245753517155815117412035133
e = 33456783984329849302849023849384905
c = 532306137711434808432697212515513191867552159124375611785929052242430458057
m = findM(n, e, c)

print("Message = ", bytearray.fromhex(format(m, '02x')).decode())