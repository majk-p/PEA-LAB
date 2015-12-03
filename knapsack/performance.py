#!/usr/bin/python
from fptas import FPTAS
from dynamic import knapsack
from random import randint
from knapsack import readInstance, generateInstance
from time import time
import sys

sys.setrecursionlimit(100000)

if len(sys.argv) != 6:
    print "Usage: {} type prefix minsize step approx".format(sys.argv[0])
    sys.exit()

_, t, prefix, minsize, step, approx = sys.argv
minsize, step = int(minsize), int(step)
approx = float(approx)

if t == 'time':
    counter = [[0 for x in range(100)] for y in range(10)]
    averages = []
    fptasSum, dynSum, j = 0, 0, 0
    for n in range(minsize, 10*step + minsize, step):
        for i in range(100):
            filename = "tests/{0}_{3}_time_s{1}_i{2}".format(prefix, str(step), str(i), str(approx))
            generateInstance(filename, int(n), int(n)*randint(1,n))
            n, c, w = readInstance(filename)
            begin = time()
            fptasResult, _ = FPTAS(n, c, w, approx)
            fptasTime = time() - begin
            begin = time()
            dynResult, _ = knapsack(n, c, w)
            dynTime = time() - begin
            # counter[j][i] = [dynResult, fptasResult, dynTime, fptasTime]
            fptasSum += fptasTime
            dynSum += dynTime
        averages.append([n, dynSum/100.0, fptasSum/100.0, abs(dynSum-fptasSum)/float(dynSum)*100])
        j += 1
        fptasSum, dynSum = 0, 0
    filename = "results/res_{0}_{1}_{3}_t_{2}".format(prefix, str(step), str(approx), str(minsize))
    with open(filename, 'w') as f:
        for n in averages:
            print n
            f.write(str(n)[1:-1]+"\n")

elif t == 'quality':
    res = []
    for n in range(minsize, 10*step + minsize, step):
        filename = "tests/{0}_{2}_quality_s{1}.csv".format(prefix, str(step), str(approx))
        generateInstance(filename, int(n), int(n)*randint(1,n))
        n, c, w = readInstance(filename)
        fptas, _ = FPTAS(n, c, w, approx)
        dyn, _ = knapsack(n, c, w)
        q = abs(dyn-fptas)/float(dyn)
        res.append([n, dyn, fptas, q, q * 100])
    filename = "results/res_{0}_{1}_{3}_q_{2}.csv".format(prefix, str(step), str(approx), str(minsize))
    with open(filename, 'w') as f:
        for n in res:
            print n
            f.write(str(n)[1:-1]+"\n")

else:
    print "Analysis type not found"
