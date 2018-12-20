
import numpy as np
r = [-0.5472 - 0.0033j,-1.1118 + 0.5679j,-1.6797 + 0.0000j,-1.7294 + 0.0497j,-1.0828 - 0.5969j,-1.2145 - 0.5646j,0.0820 - 0.5679j,-0.5505 + 0.0000j,-0.5936 - 0.0497j,-1.1325 + 0.5472j,-0.5182 + 1.1615j,-0.5472 + 1.1325j,-1.1118 + 0.5679j,-1.7294 + 0.0497j,-1.1822 - 0.5969j,0.0787 - 0.5646j,-0.0820 - 0.5679j,0.6002 + 0.0000j,-0.0033 + 0.0000j,0.5679 + 0.0000j]
r = np.array(r)
N = 20
L = 4
m = 3
s = np.array([-1j, 1j, -1, -1, -1, -1, -1j, -1, 1, -1, -1, 1j, 1j, -1, -1, -1, -1j, 1, -1, 1])

# s = np.array([1, 1, 1, -1, -1, 1, 1, -1, -1, 1, 1, 1, -1, 1, -1, -1, 1, 1, 1, 1])
# r = np.array([0.8492, 1.4264, -.8492, -1.4264, -1.0226, .8492, -0.4454, .4454, 1.4264])

# N = 20
# m = 3
# L = 3
P = m*L # no. of pilot symbols


Pstart = (len(s)-P)/2 # number of s to left+right, divide by two
Pstart = int(Pstart)


Ps = []
for x in range(P):
    Ps.append(s[Pstart+x])
Ps = np.array(Ps)
print("PS",Ps)

Q = np.full( (P-L+1, L), 1j)

print(Pstart)

for x in range(L):
    for y in range(0, P-L+1):
        print(x, y, Ps[L-1-x+y])
        Q[y][x] = Ps[L-1-x+y]

print(Q)

QhQ = np.dot(Q.conj().T, Q)
print(QhQ)

# r = r[:-2]
Qhr = np.dot(Q.conj().T, r[Pstart:Pstart+P-L+1])
# Qhr = np.dot(Q.conj().T, r)
print(Qhr)

k = 9

cir = 1/k * Qhr
print(cir)

# else
# cir = np.divide(Qhr, (np.dot(Q.conj().T, Q)))
cir2 = np.dot(Qhr, np.linalg.inv(QhQ))
print("HERE")
print(cir2)