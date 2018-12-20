import numpy as np

c = [0.69-0.27j, 0.54+0.30j]

r = [0.1747+0.7460j, -0.1165+1.6443j, -0.7804 +
     0.5543j, -0.3117-0.22226j, 0.00661-0.9386j]
n = 5

L = 2

symbols = [1, -1]

dataDetected = []
allData = []

for x in range(L-1):
    allData.append(1)


def getDelta(time, symbol):
    temp = 0
    t = 0

    for x in range(0, L):
        if(x == 0):
            temp += np.multiply(c[x], symbol)
        else:
            temp += np.multiply(c[x], allData[len(allData)+t])
        t = t-1
    temp = np.abs(r[time]-temp)**2
    return temp


def getSymbol(time):
    deltas = []

    for x in range(0, len(symbols)):
        deltas.append(getDelta(time, symbols[x]))

    return symbols[deltas.index(min(deltas))]


for x in range(0, len(r)):
    temp = getSymbol(x)
    allData.append(temp)
    dataDetected.append(temp)

print("Data", dataDetected)
print("all", allData)
