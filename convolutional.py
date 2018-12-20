#MAMEEN

import numpy as np

generator = [4,6,7]
K = 3 #consraint length
numOutputs = 3 #numOutputs



#data with appended 0's - not prepened
def encode(generator,data):
    
    shiftRegister = []
    genBinary = []

    for x in range(len(generator) ):
        genBinary.append("{0:b}".format(generator[x]))

    #print(genBinary)

    for x in range(0,len(generator)):
        shiftRegister.append(0)

    parity = []
    for x in range(0,len(data)):
        shiftRegister.insert(0,data[x])
        shiftRegister.pop()
        temp = 0

        for y in range(len(generator)):
            temp = 0
            for z in range(0,len(shiftRegister)):  
                temp+= shiftRegister[z]*int(genBinary[y][z])
            temp = temp%2
            parity.append(temp)

    return parity


class trellisNode:
    def __init__(self,state,time):
        self.time = time
        self.state = state
        self.delta = 0
        self.alpha = 0
        self.bestPrevious = None
        self.previous = []
        self.foward = []

def buildTrellis(tempNode,myTrellis):
    if(tempNode.time == len(myTrellis[0])):
        return
    
    if(tempNode.time>=len(myTrellis[0])-1):

        
        state = [-1,tempNode.state[0]]
        if(myTrellis[states.index(state)][tempNode.time+1] == None):        
            newNode = trellisNode(state,tempNode.time+1) 
            newNode.previous.append(tempNode)
            tempNode.foward.append(newNode)
            buildTrellis(newNode,myTrellis)
        
        else:
            return
    
    else:
        

    # shiftRegister = []
    # genBinary = []
    # #get binary representation of generator
    # for x in range(0, len(generator)):
    #     genBinary.append("{0:b}".format(generator[x]))

    # #sort shift register to begin in state 0
    # for x in range(0, len(genBinary[x])):
    #     shiftRegister.append(0)
    # # list to contain all parity bits
    # parity = []
    # #encode the data
    # # for every bit in the bitStream, insert into shfit register
    # # take shift reggister elements, multiply by genertor in binar%2
    # for x in range(0, len(data)):
    #     #print("Inserting", bitStream[x])
    #     shiftRegister.insert(0, data[x])
    #     shiftRegister.pop()
    #     #print("Shift after insert:", shiftRegister)
    #     temp = 0
    #     for y in range(0, len(generator)):
    #         #print("Output bit ", y)
    #         temp = 0
    #         for z in range(0, len(shiftRegister)):
    #             temp += shiftRegister[z]*int(genBinary[y][z]).__round__()
    #         #print("TEMP",temp)
    #         temp = temp % 2
    #         #print("temp after mod 2", temp)
    #         parity.append(temp)
    #         #print("Parity so far", parity)
    # return parity

data = [1,0,1,0,0,0]

print(encode(generator,data))
        

    
    # shiftRegister = []
    # genBinary = []
    # #get binary representation of generator
    # for x in range(0, len(generator)):
    #     genBinary.append("{0:b}".format(generator[x]))

    # #sort shift register to begin in state 0
    # for x in range(0, len(genBinary[x])):
    #     shiftRegister.append(0)
    # # list to contain all parity bits
    # parity = []
    # #encode the data
    # # for every bit in the bitStream, insert into shfit register
    # # take shift reggister elements, multiply by genertor in binar%2
    # for x in range(0, len(bitStream)):
    #     #print("Inserting", bitStream[x])
    #     shiftRegister.insert(0, bitStream[x])
    #     shiftRegister.pop()
    #     #print("Shift after insert:", shiftRegister)
    #     temp = 0
    #     for y in range(0, len(generator)):
    #         #print("Output bit ", y)
    #         temp = 0
    #         for z in range(0, len(shiftRegister)):
    #             temp += shiftRegister[z]*int(genBinary[y][z]).__round__()
    #         #print("TEMP",temp)
    #         temp = temp % 2
    #         #print("temp after mod 2", temp)
    #         parity.append(temp)
    #         #print("Parity so far", parity)
    # return parity
    # return
