
import numpy as np

#???????
L = 2
c = [.75, -.24]
#???????

N = 4
S = np.array([1, -1, -1, 1])
F = 1/N * np.fft.fft(np.eye(N))

print("F", F)

iF = F.conj().T
print("iF", iF)

s = np.dot(iF, S)
print("s", s)

sc = np.concatenate( (s[N-L+1:], s), axis=0 )
print("sc", sc)

c_temp = list(c)

for x in range(N-len(c_temp)):
    c_temp.append(0)
c_temp = np.array(c_temp)

from scipy.linalg import circulant
C = circulant(c_temp)
print("C", C)

r = np.dot(C, s)
print("r", r)
