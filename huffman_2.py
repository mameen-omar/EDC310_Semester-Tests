import numpy as np

signal = 'BAABABBBABAABABBBABBABBA'
#print(len(signal))

frequency = []
characters = []

for x in range(0,len(signal)):
    if(signal[x] in characters):
        frequency[characters.index(signal[x])] = frequency[characters.index(signal[x])]+1

    else:
        characters.append(signal[x])
        frequency.append(1)

summation = sum(frequency)

print(characters)

for x in range(0,len(characters)):
    frequency[x] = frequency[x]/summation


print(characters)
print(frequency)


sortedRes = sorted(zip(characters, frequency), key=lambda x: x[0])


print(sortedRes)