import numpy as np

s = [complex(1,0),complex(0,1), complex(-1,0), complex(0,-1)]
r = complex(0.2,0.35)
sigma = 0.5
def getProbs(s,r):
    probs = []
    for x in range(0,len(s)):
        temp = 0
        temp = np.abs(r-s[x])**2
        temp = -1*temp
        temp = temp/(2*(sigma**2))
        probs.append(0.5*np.exp(temp))
    
    return probs

probs = getProbs(s,r)

beta = sum(probs)

print(probs)
print(sigma)

for x in range(0,len(probs)):
    probs[x] = probs[x] *beta


mostLikely = probs.index(max(probs)) + 1

print(mostLikely)