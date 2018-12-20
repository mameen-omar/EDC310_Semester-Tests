#!/usr/bin/python3

import numpy as np

P = np.array(
    [np.array([0, 0, 0, 1, 0, 1, 1, 1, 0, 0, 0, 0]),
    np.array([1, 0, 1, 0, 1, 1, 1, 0, 0, 1, 1, 0]),
    np.array([0, 0, 0, 1, 0, 0, 0, 1, 1, 0, 1, 0])]
)
print(P)
c = np.array([1, 1, 1, 0, 1, 1, 0, 1, 1, 0, 0, 1, 1, 0, 0])

G = np.concatenate((np.eye(3), P), axis=1)

H = np.concatenate( (P.T, np.eye(12)), axis=1)

cHT = np.dot(c, H.T)%2

k = 15
n = 3

print(cHT)

ccor = np.array(c)

print(H.T)
one_error = False

cols = H.T.shape[0]
for colI in range(cols):
    col = H.T[colI, :]
    if (cHT == col).all():
        print("Found it", colI)
        one_error = True
# for i in range(len(H.T[0])):
#     if (cHT == H.T[:,i]):
#         print("Here")
#         one_error = True

for colI1 in range(cols):
    for colI2 in range(cols):

            col1 = H.T[colI1, :]
            col2 = H.T[colI2, :]

            xor = col1+col2
            xor = xor%2

            if (cHT == xor).all():
                print("Found it", colI1, colI2)

for colI1 in range(cols):
    for colI2 in range(cols):
        for colI3 in range(cols):

            col1 = H.T[colI1, :]
            col2 = H.T[colI2, :]
            col3 = H.T[colI3, :]

            xor = col1+col2+col3
            xor = xor%2

            if (cHT == xor).all():
                print("Found it", colI1, colI2, colI3)

