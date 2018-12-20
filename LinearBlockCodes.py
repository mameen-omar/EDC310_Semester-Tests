import numpy as np

def checkZero(arr):
    for x in range(0,len(arr)):
        if(arr[x] != 0):
            return False    
    return True
s = [] #symbols to encode
c = [] #codeword encoded

#d = n-k+1

p = [   [1, 1, 1, 0, 1, 0, 1, 1, 1, 0],
          [0, 0, 1, 0, 1, 1, 0, 0, 0, 0],
          [0, 1, 1, 1, 0, 1, 0, 1, 1, 1],
          [1, 0, 1, 1, 0, 1, 0, 0, 1, 1],
          [0, 1, 0, 0, 0, 1, 0, 1, 0, 1],
          [1, 1, 0, 1, 1, 0, 0, 1, 0, 1],
          [0, 1, 1, 1, 1, 0, 1, 0, 0, 0],
          [0, 0, 1, 0, 1, 1, 0, 1, 0, 0],
          [1, 0, 0, 1, 1, 1, 0, 0, 1, 0],
          [1, 1, 1, 0, 0, 0, 1, 0, 0, 1]] #parity

c_ = [0, 1, 0, 1, 1, 0, 0, 1, 0, 1, 1, 0, 1, 0, 0, 0, 1, 0, 0, 1] # estimated Code word
 

G = np.identity(len(p))
G = np.concatenate((G,p),axis=1)
H = np.transpose(p)
H = np.concatenate((H, np.identity(len(H))), axis=1)  # parity check pt|I

print(G)
print()
print(H)
print()
print("Transpose H" , np.transpose(H))
syndrome = np.matmul(c_,np.transpose(H))%2
print("Syndrome = ", syndrome)

if(checkZero(syndrome) == True):
    print("Syndrome is zero")
    exit()

#check H matrix now for the syndrome
syndromeT = np.transpose(syndrome)
print(syndromeT)

for col in range(0,len(H[0])):
    if(np.array_equiv(H[:,col],syndromeT)):
        print("Equivalent in H column", col)
        needXOR = False
        exit()

#now we xor 2
for x in range(0,len(H[0])):
    for j in range(0,len(H[0])):
        if(x != j):
            XOR = np.logical_xor(H[:,x], H[:, j])
            #print("XOR", XOR)
            if(np.array_equiv(np.transpose(XOR), syndromeT)):
                print("Found at cols, ",x,j)
                exit()
#3 xor now
found = False
for x in range(0, len(H[0])):
    if(found is True):
        break
    for j in range(0, len(H[0])):
        if(found is True):
            break
        for y in range(0,len(H[0])):
            if(found is True):
                break
            if(x != j != y):
                XOR = np.logical_xor(np.logical_xor(H.T[x], H.T[j]), H.T[y])
                if(np.array_equiv(XOR, syndrome)):
                    print("Found at cols, ", x, j,y)
                    found = True
                    break
                    
#4 xor now
for x in range(0, len(H[0])):
    for j in range(0, len(H[0])):
        for y in range(0, len(H[0])):
            for z in range(0, len(H[0])):
                if(x != j != y != z):
                    XOR = H.T[x] + H.T[j] + H.T[y] + H.T[z]
                    XOR = XOR % 2
                    #print("XOR", XOR)
                    if(np.array_equiv(XOR, syndrome)):
                        print("Found at cols, ", x, j, y,z)
                        exit()
'''
Carrim:


import numpy as np

################### Given ########################
P = [ [0, 0, 0, 1, 0, 1, 1, 1, 0, 0, 0, 0],
      [1, 0, 1, 0, 1, 1, 1, 0, 0, 1, 1, 0],
      [0, 0, 0, 1, 0, 0, 0, 1, 1, 0, 1, 0]]

c = [1, 1, 1, 0, 1, 1, 0, 1, 1, 0, 0, 1, 1, 0, 0]
##################################################

G = np.concatenate((np.identity(len(P)),P),axis=1)
H = np.concatenate((np.transpose(P), np.identity(len(P[0]))), axis=1)

print("G:")
print(G)
print("H:")
print(H)

# cHt%2
syndrome = np.matmul(c, np.transpose(H))%2
print(syndrome)

# check syndrome
needXOR = True
for i in syndrome:
    if i != 0:
        needXOR = True

if not needXOR:
    print("Syndrome is")
    print(syndrome)
    exit(0)

# print(H[:,2])
# print([row[2] for row in H])

for i in range(len(H[0])):
    for j in range(len(H[0])):
        for k in range(len(H[0])):
            XOR = np.logical_xor(np.logical_xor(H.T[i], H.T[j]), H.T[k])
            if (np.array_equiv(XOR, syndrome)):
                print (i, j, k)
                exit()
'''
