import numpy as np

signal = 'AABABBBABAABABBBABBABBA'
#signal = 'BCCACBCCCCCCCCCCCACCCA'
dictionary = ['']
codeword = ['']

i = 0 
j = i+1

while(True):
    subString = signal[i:j]
    if( j == len(signal)):
        if(subString not in dictionary):
            dictionary.append(subString)
        else:
            print("Last String repeated ", subString)

        break
    
    if(subString not in dictionary):
        dictionary.append(subString)
        i = j
        j = i+1
        continue
    
    j = j+1

print(dictionary)

for x in range(1, len(dictionary)):
    item = dictionary[x][:-1]

    if(item in dictionary):
        codeword.append(str(dictionary.index(item)) + dictionary[x][-1])

print(codeword)