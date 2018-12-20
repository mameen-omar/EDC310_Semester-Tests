import numpy as np

c = [0.86 - 0.43j, -.27 + 0.66j, 0.31 + 0.17j]

r = [-0.77 + 1.79j, 0.75 - 0.77j, 0.55 - 0.08j, -0.46 + 1.09j,
     -0.50 + 0.09j, 0.69 - 0.90j, 0.05 + 0.35j, -0.89 + 1.95j,
     1.07 - 1.32j, 0.75 - 0.01j, -0.44 + 0.02j, 0.16 + 0.33j]
n = 8

l = 3

symbols = [1,-1]


allDetected = []
dataDetected = []

for x in range(0,l-1):
    allDetected.append(1)

def getDelta(time,symbol):
    temp = 0
    t = 0
    for x in range(l):
        if(x == 0):
            temp += c[x]*symbol
        else:
            temp += np.multiply(c[x],allDetected[len(allDetected)+t])
        t = t-1
    return(np.abs(r[time]-temp)**2)

def getSymbol(time):
    deltas = []
    for x in range(0,len(symbols)):
        deltas.append(getDelta(time,symbols[x]))
        print("Delta", time, "for symbol = ", deltas[x])
    return symbols[deltas.index(min(deltas))]

for x in range(0,n):
    temp = getSymbol(x)
    allDetected.append(temp)
    dataDetected.append(temp)

print("All", allDetected)
print("DATa", dataDetected)