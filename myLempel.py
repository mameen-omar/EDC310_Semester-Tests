# import numpy as np

# signal = 'AABABBBABAABABBBABBABBA'
# #signal = 'BCCACBCCCCCCCCCCCACCCA'
# dictionary = ['']
# codeword = ['']

# i = 0 
# j = i+1

# while(True):
#     subString = signal[i:j]
#     if( j == len(signal)):
#         if(subString not in dictionary):
#             dictionary.append(subString)
#         else:
#             print("Last String repeated ", subString)
#         break
    
#     if(subString not in dictionary):
#         dictionary.append(subString)
#         i = j
#         j = i+1
#         continue
    
#     j = j+1

# print(dictionary)

# for x in range(1, len(dictionary)):
#     item = dictionary[x][:-1]

#     if(item in dictionary):
#         codeword.append(str(dictionary.index(item)) + dictionary[x][-1])

# print(codeword)

import numpy as np

toEncode = '101011011010101010110'

i = 0
j = 1

dictionary = ['']


#get dictionary - unique subStrings
while(True):
    
    subString = toEncode[i:j]
    if(j >= len(toEncode)):
        #print("HERE")
        if(subString not in dictionary):
            if((len(subString) == 0)):
                break
            dictionary.append(subString)
            break
        else:
            break

    if(subString not in dictionary):
        dictionary.append(subString)
        i = j
        j = i+1 
        continue
    
    j += 1

print("Unique substrings - ", dictionary)


#Just to confirm bs works
temp = 0
for x in range(len(dictionary)):
    temp += len(dictionary[x])

print(temp == len(toEncode))
##########

numBits = int(np.ceil(np.log2(len(dictionary)-1)))

#We have the dictionary - now to do the encoding
codeWord = ['']

for x in range(1,len(dictionary)):
    if(len(dictionary[x]) == 1):
        codeWord.append(str(0) + dictionary[x][-1])
        continue
    
    temp =  dictionary[x][:-1]

    codeWord.append(str(np.binary_repr(dictionary.index(temp),numBits)) + dictionary[x][-1])
    print(numBits)


print("CodeWords = ", codeWord)

for x in range(0,len(dictionary)):
    print("The code word for", dictionary[x], "is", codeWord[x])

    