#!/usr/bin/python
from fptas import FPTAS
from dynamic import knapsack
import sys

def readInstance(filename):
    with open(filename, 'r') as f:
        n = int(f.readline())
        cap = int(f.readline())
        wc = []
        for line in f:
            x, y = line.split()
            wc.append((int(x), int(y)))
        return n, cap, wc
        
if __name__ == '__main__':
    if len(sys.argv) != 3:
        print "Usage: {0} approx filename".format(sys.argv[0])
        sys.exit()
    approx = float(sys.argv[1])
    n, cap, wc = readInstance(sys.argv[2])
    print "INPUT: ", n, cap, wc
    print
    print FPTAS(n, cap, wc, approx)
    print
    print "DYNAMIC: ", knapsack(n, cap, wc)
