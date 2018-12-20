def dfe(r, c, symbols):
    """
    :param r: The received symbols, header + tail symbol must be symbols[0]
    :param c: The CIR vector
    :param symbols: The Modulation Map (e.g. [1, -1] for BPSK, [1, 1j, -1, -1j] for QPSK
    The first element in symbols (symbols[0]) is assumed to be the head and tail symbol type

    :return: the DFE path []
    """


    L = len(c)          # L is the length of the CIR vector
    N = len(r) - (L-1)  # r has tail bits, so those (of size L-1) must be taken out of the length

    # Array to hold the symbols that are estimated to have been transitted
    estimated_symbols = []

    # Hold the total cost for the chosen path
    path_cost = 0.0


    # Prefilled with the header symbols
    # number of header symbols = L-1
    for x in range(L-1):
        estimated_symbols.append(symbols[0])


    # For every time in the received. Exclude adding the tail symbols - these are known
    # We say N+L-1 for the length of the trellis, +1 since we start at t==1, -2 to exclude tail bits
    for t in range(1, (N+L-1)+1-2):

        # the lowest cost and paired symbol encountered in this t
        minCost = float("inf")
        minCostSymbol = None

        # For DFE, try out every possible symbol as the next symbol. Save the cone with the lowest resulting delta
        for symbol in symbols:

            # delta = |r - (s2*c0 + s1*c1 + s0*c2)|**2

            # we go back L-1 previous symbols
            # sc_sum is the sum of s2*c0+s1*c1...
            sc_sum = 0.0
            for x in range(L-1):
                # sc is the current s_n * c_n pair
                sc = estimated_symbols[t-x] * c[x+1]
                sc_sum += sc

            # now add the currently considered symbol
            sc = symbol*c[0]
            sc_sum += sc

            delta_current = abs(r[t-1] - sc_sum)**2

            # if delta_current is less than minCost, use this symbol instead
            if delta_current < minCost:
                minCost = delta_current
                minCostSymbol = symbol

        # minCost is the cost of the minimum delta for this t, add it to the total path cost
        path_cost += minCost

        # minCostSymbol is the symbol that's estimated to have been received by DFE, add it to the array
        estimated_symbols.append(minCostSymbol)

    # strip the header symbols
    estimated_symbols_no_header = estimated_symbols[2:]

    # Return the estimated received symbols (without the header)
    return path_cost, estimated_symbols_no_header