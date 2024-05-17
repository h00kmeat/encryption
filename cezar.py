def encode_cezar(string):

    print(string)
    n = 1
    new_string = ""
    alphabet_dict = {i: chr(i + 1040) for i in range(32)}
    while n < 32:
        new_string = ""
        for letter in string:
            if get_key(alphabet_dict, letter):
                key = int(get_key(alphabet_dict, letter))
                new_key = (key - n) % 32
                new_string = new_string + alphabet_dict[new_key]
            else:
                new_string = new_string + " "

                # print(get_key(alphabet_dict, letter), ":", letter)
        print(f"Новая строка при сдвиге '{n}' : '{new_string}'")

        n += 1


def get_key(d, value):
    for k, v in d.items():
        if v == value:
            return k


def decode_cezar(string, k):

    alphabet_dict = {(i + 1): chr(i + 1040) for i in range(32)}
    print(alphabet_dict)
    rev_alphabet_dict = {chr(i + 1040): (i + 1) for i in range(32)}
    print(rev_alphabet_dict)
    new_string = ""
    for letter in string:
        if rev_alphabet_dict.get(letter):
            key = int(rev_alphabet_dict[letter])
            # print(chr(1040) == "А")
            new_key = (key + k - 1) % 32 + 1
            new_string += alphabet_dict[new_key]
        else:
            new_string += " "

    print(new_string)


string1 = "ЖГООЮ РГФХЦТГБХ ЦХУСП"
encode_cezar(string1)
print("\n")
alphabet_dict = {i: chr(i + 1040) for i in range(32)}
print(alphabet_dict)
string2 = "НАСТУПАЙТЕ НОЧЬЮ"
k = 3
decode_cezar(string2, k)


print("\n")
string3 = "КЗТТВ ЙВ КТЪЦЭВ УХР ШМСЧМЩ ЙЗУ ФМ ЛХШЩЗФМЩШЖ"
encode_cezar(string3)
print("\n\n")
encode_cezar("ПГПГ ПЮОГ УГПЦ.")
