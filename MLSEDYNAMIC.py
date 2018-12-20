import numpy as np

n = 4
l = 3

c = [0.62, -0.24, 0.56]
r = [0.89, -0.32, 1.71, -1.13, 1.70, -0.04]

length = n+l-1

states = [[1,1], [1,-1], [-1,1], [-1,-1]]

def getStates(state):
    returnStates = []
    returnStates.append([1, state[0]])
    returnStates.append([-1, state[0]])
    return returnStates

class node:
    def __init__(self,time,state):
        self.time = time
        self.state = state
        self.foward = []

myTrellis = np.empty(shape = [4,n+l], dtype=node)

def buildTrellis(tempNode,n,l):
    if(tempNode.time == length):
        return    
    if(tempNode.time >= length - 2):
        state = [1,tempNode.state[0]]
        if(myTrellis[states.index(state)][tempNode.time+1] == None):
            newNode = node(tempNode.time+1, state)
            myTrellis[states.index(state)][tempNode.time+1] = newNode
            tempNode.foward.append(newNode)
            buildTrellis(newNode,n,l)
            return        
        else:
            tempNode.foward.append(myTrellis[states.index(state)][tempNode.time+1])
            return      

    newStates = getStates(tempNode.state)
    for x in range(len(newStates)):
        newNode = node(tempNode.time+1, newStates[x])
        myTrellis[states.index(newStates[x])][tempNode.time+1] = newNode
        tempNode.foward.append(newNode)
        buildTrellis(newNode, n, l)

def printT(trellis):
    for time in range(0,n+l):
        for state in range(0,4):
            if(myTrellis[state][time] is not None):
                tempNode = myTrellis[state][time]

                for x in range(len(tempNode.foward)):
                    delta = np.abs(r[time] -  c[0]*tempNode.foward[x].state[0] -c[1]*tempNode.state[0] - c[2]*tempNode.state[1])**2
                    print("Delta ", str(time+1) , " from" , str(states.index(tempNode.state)) , " to " , str( states.index(tempNode.foward[x].state) ) , "is ", delta)

tempNode = node(0,[1,1])
myTrellis[0][0] = tempNode
buildTrellis(tempNode,n,l)
printT(myTrellis)
print(myTrellis)
