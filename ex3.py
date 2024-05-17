def fact(x):
    if x == 0:
        return 1
    return fact(x - 1) * x


def combinations(n, k):
    return fact(n) / (fact(n - k) * fact(k))


print(combinations(11, 6))
