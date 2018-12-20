import numpy as np


n = 4 #number of data bits
r = [-1.59,1.7,-1.26,1.82] #recieved vector - only data bits len(r) =  n
c = [0.72,-0.39] #convolution matrix
L = len(c) #length of the c vector
numHeader = L-1 #number of header bits
symbols = [1,-1, 1j, -1j]
dataDetected = [] #just the data bits detected

# Function to get the delta value for a single symbol
# symbol is the symbol we are estimating
# time is the time instance for the symbol we are getting the delta
def getDelta(time,symbol):
    temp = 0
    t = 0
    for x in range(0,L):
        if(x == 0):
            temp += c[x]*symbol
        else:
            #if we havent detected the first l symbols
            if(len(dataDetected)+t <0):
                temp += c[x]*1
            else:
                temp += c[x]* dataDetected[len(dataDetected)+t]                
        t = t-1
    return (np.abs( r[time] - temp) **2)


# Function to detect a single sumbol using 
# DFE Equalizer algorithm
def getSymbol(time):
    deltas = []
    for x in range(0,len(symbols)):
        deltas.append(getDelta(time, symbols[x]))
        print("Delta", x, "at time", time, "is", deltas[x])
    print()
    return symbols[deltas.index(min(deltas))]             
        
# Function to detect the symbols in the recieved vector
# using the DFE Equalizer
def detectSymbols():
    for x in range(0, len(r)):
         dataDetected.append(getSymbol(x))

print("Detecting symbols")
detectSymbols()
print("JUST DATA DETECTED SYMBOLS")
print(dataDetected)

