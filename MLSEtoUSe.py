import numpy as np
n = 4
l = 3
c = [0.62, - 0.24,	      0.56]
r = [0.89, - 0.32,     1.71, - 1.13,    1.70, - 0.04]


trellisStates = [[1, 1], [1, -1], [-1, 1], [-1, -1]]


class node:
    def __init__(self, time, state):
        self.state = state
        self.time = time
        self.previous = []
        self.foward = []
        self.delta = []
        self.alpha = 0


myTrellis = np.empty((4, n+l), dtype=node)

newNode = node(0, [1, 1])
myTrellis[0][0] = newNode


def getDelta(time, state1, state2):
    temp = c[0]*state2[0]
    temp += c[1] * state2[1]
    temp += c[2] * state1[1]
    print(time, state1, state2)
    temp = r[time-1] - temp
    temp = np.abs(temp)**2
    print("Delta", time, "from", state1, "to", state2, "is", temp)
    return temp


def getStates(state):
    returnS = [[1, state[0]], [-1, state[0]]]
    return returnS


print("LENGHT", len(myTrellis[0]))


def buildTrellis(tempNode):
    if(tempNode.time >= len(myTrellis[0])-1):
        print("FUIGEGU")
        return

    if(tempNode.time >= (n+l-1-2)):
        newState = [1, tempNode.state[0]]

        if(myTrellis[trellisStates.index(newState)][tempNode.time+1] == None):
            newNode = node(tempNode.time+1, newState)
            delta = getDelta(newNode.time, tempNode.state, newNode.state)
            newNode.alpha = delta
            newNode.delta.append(delta)
            tempNode.foward.append(newNode)
            newNode.previous.append(tempNode)
            myTrellis[trellisStates.index(newState)][tempNode.time+1] = newNode
            buildTrellis(newNode)
            return
        else:
            newNode = myTrellis[trellisStates.index(newState)][tempNode.time+1]
            if(tempNode.state not in newNode.previous):
                newNode.previous.append(tempNode)
                tempNode.foward.append(newNode)
                delta = getDelta(newNode.time, tempNode.state, newNode.state)
                newNode.delta.append(delta)
                return
            else:
                return
    allStates = getStates(tempNode.state)

    for x in range(len(allStates)):
        newState = allStates[x]

        if(myTrellis[trellisStates.index(newState)][tempNode.time+1] == None):
            newNode = node(tempNode.time+1, newState)
            delta = getDelta(newNode.time, tempNode.state, newNode.state)
            newNode.delta.append(delta)
            newNode.alpha = delta
            tempNode.foward.append(newNode)
            newNode.previous.append(tempNode)
            myTrellis[trellisStates.index(newState)][tempNode.time+1] = newNode
            buildTrellis(newNode)
        else:
            newNode = myTrellis[trellisStates.index(newState)][tempNode.time+1]
            if(tempNode.state not in newNode.previous):
                newNode.previous.append(tempNode)
                tempNode.foward.append(newNode)
                delta = getDelta(newNode.time, tempNode.state, newNode.state)
                newNode.delta.append(delta)
                continue
            else:
                continue


print(myTrellis)
buildTrellis(myTrellis[0][0])
print(myTrellis)


for x in range(0, len(myTrellis)):
    for y in range(0, len(myTrellis[0])):
        temp = myTrellis[x][y]
        if(temp is None):
            continue
        if(len(temp.previous) < 1):
            continue
        if(len(temp.previous) == 1):
            temp.alpha = temp.previous[0].alpha + temp.delta[0]
            continue

        bestIndex = 0
        bestAlpha = temp.previous[0].alpha + temp.delta[0]

        for t in range(1, len(temp.previous)):
            tempAlpha = temp.previous[t].alpha + temp.delta[t]

            if(tempAlpha < bestAlpha):
                bestAlpha = tempAlpha
                bestIndex = t

        temp.previous = [temp.previous[bestIndex]]
        temp.delta = [temp.delta[bestIndex]]
        temp.alpha = bestAlpha


detected = []

temp = myTrellis[0][-1]

while(temp.time > 0):
    detected.insert(0, temp.state[0])
    temp = temp.previous[0]

detected.insert(0, temp.state[0])

print("Dettec", detected)
