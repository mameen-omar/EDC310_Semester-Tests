import numpy as np

m = 4
l = 3
p = m*l
n = 16
s = [1,1,1,-1,1,-1,-1,-1,-1,-1,1,-1,-1,1,1,1]

r = [-2.1646 - 0.7886j ,  1.1519 - 1.6540j ,- 0.4113 + 1.1937j,   0.6158 + 0.1077j, - 1.0073 + 1.7146j,
     0.0531 - 2.5536j ,  0.4689 + 1.6432j ,- 1.8597 - 1.7295j ,  0.3251 + 0.1972j, - 1.4960 - 0.5573j,
     2.1646 + 0.7886j, - 1.8180 + 0.3358j ,  2.8283 - 0.9602j, - 1.0774 - 0.1245j, - 0.2696 + 0.3552j,
     0.1109 + 1.0658j ,- 0.1193 + 0.3803j,  0.3803 + 0.1193j ,  1.4375 - 1.0464j,   0.0383 + 0.3135j,
     - 0.5693 + 0.5990j,   0.3109 + 1.0486j, - 0.1804 - 0.1365j ,- 1.1725 - 0.4626j - 0.1733 - 0.5622j,
     - 0.8382 - 0.3469j, - 0.1193 + 0.3803j ,  2.1646 + 0.7886j ,  0.3251 + 0.1972j]

print(s)

Q = np.full((p-l+1,l),1)

indexStart = int((n-p)/2)
pilot = []

for x in range(0,p):
    pilot.append(s[indexStart+x])

pilot = np.array(pilot)

print("Pilot", pilot)
print("Length of pilot", len(pilot))

for x in range(l):
    for y in range(0, p-l+1):
        Q[y][x] = pilot[l-1-x+y]


print("Grammian (Q):", Q)

Q_H = np.conjugate(Q)
Q_H = np.transpose(Q_H)

print("Q Harmatian,", Q_H)

qhq = np.matmul(Q_H,Q)

print("QhQ:",qhq)

k = 10 #hard coded from qhq

#1/k*Qr
newR = np.array(r[indexStart:indexStart+p-l+1])

cir = (1/k) * np.matmul(Q_H,newR.T)
print("CIR",cir) 


print("EXACT", np.matmul(np.matmul(Q_H, newR.T),np.linalg.inv(qhq)))

