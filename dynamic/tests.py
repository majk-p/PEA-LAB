#!/usr/bin/python
from tsp import tour_len, tsp_dp_solve

# testdata:
d1 = [
        [0,1,2],
        [3,0,4],
        [5,6,0]
    ]

d2 = [
        [0, 5, 17, 3],
        [13, 0, 7, 15],
        [15, 3, 0, 3],
        [16, 14, 6, 0]
    ]

if __name__ == '__main__':
    
    print "Testing tour_len..."
    assert tour_len((1, 2), d1) == 10
    assert tour_len((2, 1), d1) == 11
    assert tour_len((3, 1, 2), d2) == 39
    print "Passed!\n"

    print "Testing tsp_dp_solve..."
    assert tsp_dp_solve(d1) == (1, 2)
    assert tsp_dp_solve(d2) == (3, 2, 1)
    print "Passed!"