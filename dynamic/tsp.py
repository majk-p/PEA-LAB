#!/usr/bin/python
from itertools import permutations

def tsp_dp_solve(d):
    def memoize(f):
        memory = {}
        def wrapped_function(*args):
            if args not in memory:
                memory[args] = f(*args)
            return memory[args]
        wrapped_function.clear = lambda: memory.clear()
        return wrapped_function

    @memoize
    def rec_tsp_solve(c, ts):
        assert c not in ts
        if ts:
            return min((d[lc][c] + rec_tsp_solve(lc, ts - set([lc]))[0], lc)
                       for lc in ts)
        else:
            return (d[0][c], 0)

    best_tour = []
    c = 0
    cs = frozenset(range(1, len(d)))
    while True:
        l, lc = rec_tsp_solve(c, cs)
        if lc == 0:
            break
        best_tour.append(lc)
        c = lc
        cs = cs - frozenset([lc])

    best_tour = tuple(reversed(best_tour))

    return best_tour

if __name__ == '__main__':   
    d2 = [[ 0,  5, 17,  3],
          [13,  0,  7, 15],
          [15,  3,  0,  3],
          [16, 14,  6,  0]]
    print d2
    print tsp_dp_solve(d2)


