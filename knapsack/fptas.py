from dynamic import knapsack

def FPTAS(n, cap, wc, sf):
    nCap = int(float(cap)*sf)
    nWC = [(round(float(weight)* sf) + 1, cost) for weight, cost in wc]
    print "APPROXIMATED: ", nCap, nWC
    print
    return knapsack(n, nCap, nWC)
