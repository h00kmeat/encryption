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


def decode_rsa(array, open_key):
    alphabet_dict = {i: chr(i + 1040) for i in range(32)}
    rev_alphabet_dict = {chr(i + 1040): (i) for i in range(32)}

    e = open_key[0]
    n = open_key[1]
    p = eiler(n)
    d = pow(e, -1, p)
    new_string = ""
    for word in array:
        for letter in word:
            new_symb = letter**d % n

            new_string += alphabet_dict[new_symb % 32]
        new_string += " "
    print(new_string)


array = [
    [18, 2, 36, 24, 8, 7, 3, 4],
    [5, 36, 9, 10, 36, 0, 8, 17, 2, 7, 0, 17, 9, 36],
    [0, 36, 21, 2, 18, 2, 36, 24, 25, 17],
    [28, 23, 25, 26],
]
open_key = (27, 55)
decode_rsa(array, open_key)
