import numpy as np

N = 4
L = 3
c = [0.62, -0.24, 0.56]
r = [0.89, -0.32, 1.71, -1.13, 1.70, -0.04]

length = N+L-1-2  # exclude the tails to be added in, in this case 2 = L - 1 = 3 - 1
cheapest = []
s = []

deltas = []
current_state = [1, 1]
all_states = [1, 1]
#intermediate_deltas = [];
num_shift = 2  # number of posssibilities of bits that can be shifted in
intermediate_deltas = []
bits_shift = [1, -1]
count = 0  # to keep index in intermediate_deltas of where the new deltas were added

for i in range(length):  # traverse the trellis ecluding last 2 time states
    
    intermediate_deltas = []
    
    #calculate the deltads for time t = i
    for j in range(num_shift):
        intermediate_deltas.append(np.abs(
            r[i] - (bits_shift[j]*c[0] + current_state[0]*c[1] + current_state[1]*c[2]))**2)

    cheapest = intermediate_deltas[count]

    #find the cheapest route for current time t amongst the different deltas x
    for x in range(count+1, len(intermediate_deltas)):
        #print intermediate_deltas;
        if (intermediate_deltas[x] < cheapest):
            cheapest = intermediate_deltas[x]

    #set the states and append the cheapest cost to deltas
    for k in range(num_shift):
        if (cheapest == intermediate_deltas[k]):
            temp = 0
            temp = current_state[0]
            current_state[0] = bits_shift[k]
            all_states.append(bits_shift[k])
            current_state[1] = temp

    intermediate_deltas[count] = cheapest
    deltas.append(cheapest)
    del intermediate_deltas

print(current_state)

#Append last 2 states which are just 1's
for i in range(L-1):
    #print("hello")
    #print(i)
    intermediate_deltas = []
    #print(intermediate_deltas)
    intermediate_deltas.append(
        np.abs(r[i+4] - (1*c[0] + current_state[0]*c[1] + current_state[1]*c[2]))**2)
    deltas.append(intermediate_deltas[0])
    print("HERE ", end = "")
    print(intermediate_deltas)
    temp = 0
    temp = current_state[0]
    current_state[0] = 1
    all_states.append(1)
    current_state[1] = temp
    print("CS", end = "")
    print(current_state)

print(intermediate_deltas)

#for j in range(L-1):
#    all_states.append(1)

print(all_states)
print(deltas)
total = 0
for i in range(len(deltas)):
    total += deltas[i]

print(total)
