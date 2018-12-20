import numpy as np
import copy

r = [0.89, -0.32, 1.71, -1.13, 1.70, -0.04]
c = [0.62, -0.24, 0.56]
n = 4
l = 3
length = n+l-1
numStates = 4
states = [[1, 1], [1, -1], [-1, 1], [-1, -1]] #0,1,2,3

class node:
    def __init__(self, time, state):
        self.time = time
        self.state = state
        self.forward = []

def returnState(state):
    states = []
    temp = state[0]
    states.append([1, temp])
    states.append([-1, temp])
    return states

myTrellis = np.empty(shape = [4,n+l],dtype=node)

def buildTrellis(tempNode,n,l):

    if(tempNode.time == n+l-1):
        return
    
    if(tempNode.time >= (length-2)):
        newState = [1,tempNode.state[0]]   

        if(myTrellis[states.index(newState)][tempNode.time+1] == None):
            newNode = node(tempNode.time+1,newState)
            myTrellis[states.index(newState)][tempNode.time+1] = newNode
            tempNode.forward.append(newNode)
            buildTrellis(newNode,n,l)
            return
        
        else:
           tempNode.forward.append(myTrellis[states.index(newState)][tempNode.time+1])
           return
    
    newStates = returnState(tempNode.state)
   # print("In time", tempNode.time, "in state", tempNode.state)
   # print("Transition States", newStates)
    for x in range(0, len(newStates)):        
        newNode = node(tempNode.time+1, newStates[x])
        tempNode.forward.append(newNode)
        myTrellis[states.index(newStates[x])][tempNode.time+1] = newNode
        buildTrellis(newNode, n, l)
    return

tempNode = node(0,[1,1])
myTrellis[0][0] = tempNode
buildTrellis(tempNode,n,l)

def printDeltas(trellis):
    for time in range(length+1):
        for state in range(numStates):
            if(trellis[state][time] is not None):
                tempNode = trellis[state][time]
                for x in range(len(tempNode.forward)):
                    toPrint = "Delta time " + str(tempNode.forward[x].time) + " from " + str(states.index(tempNode.state)) + " to " + str(states.index(tempNode.forward[x].state))
                    
                    s1 = tempNode.forward[x].state[0]
                    s2 = tempNode.state[0]
                    s3 = tempNode.state[1]
                    delta = np.abs(r[time] - (c[0]*s1 + c[1]*s2 + c[2] *s3 ) )**2
                    toPrint = toPrint + " is " + str(delta)
                    print(toPrint)
        print()

printDeltas(myTrellis)

        
