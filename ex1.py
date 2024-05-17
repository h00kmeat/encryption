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


string = ""
list = [3, 5, 43, 564, 5435, 57, 66]
for i in range(list.__len__()):
    string = string + eiler(list[i]).__str__() + ";"
print(string)
