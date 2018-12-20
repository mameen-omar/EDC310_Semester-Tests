import numpy as np

c = [0.86 - 0.43j, -.27 + 0.66j, 0.31 + 0.17j]

r = [-0.77 + 1.79j, 0.75 - 0.77j, 0.55 - 0.08j, -0.46 + 1.09j,
     -0.50 + 0.09j, 0.69 - 0.90j, 0.05 + 0.35j, -0.89 + 1.95j,
     1.07 - 1.32j, 0.75 - 0.01j, -0.44 + 0.02j, 0.16 + 0.33j]
n = 8

l = 3


symbols = [-1,1]
allData = []
data = []

for x in range(l-1):
     allData.append(1)


def getDelta(time,symbol):
     temp = 0
     t = 0
     for x in range(0,len(c)):
          if(x == 0):
               temp+= np.multiply(c[x],symbol)
          else:
               temp += np.multiply(c[x],allData[len(allData)+t])
          t = t-1
     return(np.abs(r[time]-temp)**2)


def getSymbol(time):
     delta = []
     for x in range(0,len(symbols)):
          delta.append(getDelta(time,symbols[x]))
     return symbols[delta.index(min(delta))]

def getData():
     for x in range(n):
          temp = getSymbol(x)
          allData.append(temp)
          data.append(temp)
getData()
print("All", allData)
print("No gead", data)
