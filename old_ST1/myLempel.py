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

# import numpy as np

# toEncode = '101011011010101010110'

# i = 0
# j = 1

# dictionary = ['']


# while(True):
#     subString = toEncode[i:j]
#     if(j == len(toEncode)):
#         if(subString not in dictionary):
#             dictionary.append(subString)
        
#         break
    
#     if(subString not in dictionary):
#         dictionary.append(subString)
#         i = j
#         j = j+1
#         continue
#     j = j+1

# print("Dcitionary", dictionary)

# codeWord = ['']

# for x in range(1,len(dictionary)):
#     temp = dictionary[x]
#     index = dictionary.index(temp[:-1])
#     codeWord.append(str(index)+temp[-1])

# print("codeWords", codeWord)
