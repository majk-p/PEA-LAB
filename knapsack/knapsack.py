#!/usr/bin/python
from fptas import FPTAS
from dynamic import knapsack
import sys
from random import randint

def readInstance(filename):
    with open(filename, 'r') as f:
        n = int(f.readline())
        cap = int(f.readline())
        wc = []
        for line in f:
            x, y = line.split()
            wc.append((int(x), int(y)))
        return n, cap, wc

def generateInstance(filename, n, cap):
    with open(filename, 'w') as f:
        f.write(str(n) + '\n')
        f.write(str(cap) + '\n')
        for i in range(int(n)):
            w, c = randint(0, int(cap)), randint(0, 100)
            f.write(str(w) + ' ' + str(c) + '\n')

if __name__ == '__main__':
    if len(sys.argv) < 3:
        print "Usage:\n"
        print "{0} approx filename".format(sys.argv[0])
        print "{0} -g filename n capacity".format(sys.argv[0])
        sys.exit()
    if sys.argv[1] == '-g':
        _, _, filename, n, cap = sys.argv
        generateInstance(filename, n, cap)
        sys.exit()

    approx = float(sys.argv[1])
    n, cap, wc = readInstance(sys.argv[2])
    print "INPUT: ", n, cap, wc
    print
    print FPTAS(n, cap, wc, approx)
    print
    print "DYNAMIC: ", knapsack(n, cap, wc)
