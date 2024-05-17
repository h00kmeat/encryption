def test(m):
    for i in range(2, m):
        count = 0
        for j in range(1, m):
            res = i**j % m
            if res == 1:
                count += 1
        if count == 1:
            print(i)


def euclid(a, b):
    while a != 0 and b != 0:
        if a > b:
            a = a % b
        else:
            b = b % a
    return max(a, b)


def eiler(n):
    res = 0
    for i in range(1, n):
        if euclid(n, i) == 1:
            res += 1
    return res


m = 13
print(eiler(55))
