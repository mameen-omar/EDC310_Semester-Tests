import numpy as np


L = 2
n = 4
c = [0.75, -0.24]
# Generate Source Symbols
S = np.array([1, -1, -1, 1])
print("S:")
print(S)

def dftmtx(n):
    return np.fft.fft(np.identity(n))


F = dftmtx(n)/n
iF = np.transpose(F)
iF = np.conjugate(iF)

s = np.matmul(iF,S)

#cyclic prefix
s = np.append(s[-(L-1):],s)

print("with Cyclic", s)


# Create channel matrix

C_ = np.array([[0.75,   0,      0,      0,      0],  # Circulant Matrix - SAME DIMERNSIONS AS S_ THE SHIT WE MULTIPLY BY
               [-0.24,  0.75,   0,      0,      0],
               [0,      -0.24,  0.75,   0,      0],
               [0,      0,      -0.24,  0.75,   0],
               [0,      0,      0,      -0.24,  0.75]])

#send it
r = np.matmul(C_,s)

#remove cyclic
r = r[L-1:]
r = np.matmul(F,r)
D = np.matmul(F,np.append(c,np.zeros(n-L)))

print("EST", r/D)
