
import numpy as np

L = 2
c = np.array([.75, -.24])

N = 4
r = np.array([ 0.3750 + 0.3750j,  -0.1200 - 0.1200j,   0.3750 - 0.3750j,  -0.1200 + 0.1200j,   0.3750 + 0.3750j ])

r = r[L-1:]
print("R, non-circ", r)
F = 1/N * np.fft.fft(np.eye(N))

print("F", F)
R = np.dot(F, r)

print("R", R)

c_temp = list(c)
while len(c_temp) < N:
    c_temp.append(0)
cpadded = np.array(c_temp)

print(cpadded)

D = np.dot(F, cpadded)

print("D", D)

S  = R/D
# S = np.dot(R, np.linalg.inv(D))
print("S", S)
