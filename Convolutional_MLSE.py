import numpy as np
K = 3

################################################
#        getEncodedBits(uncodedBits)           #
#        --------------------------            #
# This method takes in a list of bits and      #
# returns a list of encoded bits               #
#                                              #
################################################

def getEncodedBits(uncodedBits):
    # Append K-1 Header Symbols
    uncodedBits = np.insert(uncodedBits, 0, [0]*(K-1), axis=0)

    codedBits = []
    for shiftIndex in range(len(uncodedBits) - (K-1)):
        codedBits = codedBits + getParityBits(uncodedBits[shiftIndex:shiftIndex + K])

    return codedBits


################################################
#            getParityBits(bits)               #
#        --------------------------            #
# This method takes in a list of bits, length  #
# 3 (the constraint length). And returns a     #
# list of the three parity bits [α, β, γ]      #
#                                              #
################################################

def getParityBits(bits):
    bits = bits[::-1]           # Reverse the list
    alpha = bits[0]
    beta = bits[0] ^ bits[1]
    gamma = bits[0] ^ bits[1] ^ bits[2]
    return [alpha, beta, gamma]


class Convolutional_MLSE(object):
    def __init__(self, r):
        self.R = np.append(r, [0]*6)
        print("List with appended 0's:", self.R)
        self.Symbols = [0, 1]
        self.N = len(self.R)
        self.Num_symbols = len(self.Symbols)
        self.Num_states = 4
        self.alphas = None
        self.Deltas = np.zeros((self.Num_symbols ** 3, int((self.N - 6)/3 + 3))) + np.inf
        self.build([self.Symbols[0]] * 3, 0)  # [1, 1, 1] , t = 0
        print(self.Deltas)
        self.ShortestPathArr = np.copy(self.Deltas)
        self.estimated_symbols = [1] * int((self.N - 6)/3)
        self.L = 3

    ################################################
    #        Constructing the Trellis              #
    ################################################

    # Used by build(), returns the state index for a given
    # sequence of past symbols. ex. [0, 0, 0] returns 0
    def get_index(self, past_symbols):
        # past_symbols = [-1 if x == 0 else x for x in past_symbols]
        ind = 0
        for i in range(3):  # For each symbol in past symbols, L = len(C)
            ind += self.Num_symbols ** (3 - i - 1) * self.Symbols.index(past_symbols[i])
        return ind


    # Recursively builds the entire delta array
    def build(self, past_symbols, t):
        if t > (self.N - 6)/3 + 2: return

        currentIndex = self.get_index(past_symbols)
        if self.Deltas[currentIndex][t] < np.inf: return

        for i in range(self.Num_symbols):
            self.build([self.Symbols[i]] + past_symbols[:-1], t + 1)
            if t >= (self.N - 6)/3:
                break
        if t == 0: return
        c = getParityBits(past_symbols[::-1])
        c = [-1 if x==0 else x for x in c]          # Replace 0's with -1 for calculation
        r1 = self.R[(t-1)*3 + 0]
        r2 = self.R[(t-1)*3 + 1]
        r3 = self.R[(t-1)*3 + 2]
        if r1 == 0: r1 = -1
        if r2 == 0: r2 = -1
        if r3 == 0: r3 = -1
        self.Deltas[currentIndex][t] = np.abs(r1 - c[0]) ** 2 + np.abs(r2 - c[1]) ** 2 + np.abs(r3 - c[2]) ** 2


message = np.array([1,0,1,0,0,0])
print("Message:", message)

encoded_message = getEncodedBits(message)
print("Encoded Message:", encoded_message)

conv_MLSE = Convolutional_MLSE(encoded_message)

