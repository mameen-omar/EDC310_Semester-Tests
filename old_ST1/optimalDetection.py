# Mohamed Ameen Omar
# Optimal Detection
# Given constellation map, determine most likely symbol recieved - No Multipath

import numpy as np

def expP(r,s,sigma):
    temp = r-s
    temp = np.abs(temp)**2 *-1
    temp = temp/(2*( (sigma) **2))
    return np.exp(temp)

sigma = 0.6
#r = np.complex(0,0)
r = -0.46 + 0.76j

symbols = [1,1j,-1,-1j]

Bprobs = []

for x in range(0,len(symbols)):
    Bprobs.append((1/len(symbols))*expP(r,symbols[x],sigma))

beta = 1/sum(Bprobs)

probs = []

for x in range(0,len(Bprobs)):
    probs.append(Bprobs[x]*beta)

ml = symbols[probs.index(max(probs))]

print("Probs", probs)
print("Beta" , beta)
print("BProbs", Bprobs)
print("Most likely", ml)