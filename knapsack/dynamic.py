from memory import memorize

def knapsack(n, cap, wc):
    # Zwraca sume najcenniejszego k elementowego podzbioru listy elementow, dla ktorych waga nie przekracza w
    @memorize
    def bestSubseq(k, w):
        if k == 0:
            return 0
        weight, cost = wc[k - 1]
        if weight > w:
            # jesli waga elementu jest za duza, pomin element
            return bestSubseq(k - 1, w)
        else:
            # w przeciwnymwypadku sprawdz czy daje lepszy wynik niz gdyby pominieto rozwiazanie (por wikipedia)
            return max(bestSubseq(k - 1, w), bestSubseq(k-1, w - weight) + cost)

    w = cap
    res = [0] * n
    for i in xrange(len(wc), 0, -1):
        if bestSubseq(i, w) != bestSubseq(i - 1, w):
            # nalezy zabrac element
            res[i -1] = 1
            w -= wc[i-1][0]
    return bestSubseq(len(wc), cap), res
