def encode(string: str, key: str):
    alphabet_dict = {i: chr(i + 1040) for i in range(32)}
    rev_alphabet_dict = {chr(i + 1040): (i) for i in range(32)}
    lenght_string, lenght_key = 0, 0

    string = string.split()
    key = key.split()
    new_string = ""
    new_key = ""
    for word in string:
        for letter in word:
            new_string += letter
        lenght_string += len(word)
    for word in key:
        for letter in word:
            new_key += letter
        lenght_key += len(word)

    new_key1 = ""
    print(string, " ", lenght_string, " ", new_string)
    print(key, " ", lenght_key, " ", new_key)
    new_key += (lenght_string // lenght_key - 1) * new_key + new_key[
        : lenght_string % lenght_key
    ]
    print(key, " ", len(new_key), " ", new_key)

    i = 0
    abc = ""
    numb_decode_text = 0
    for word in string:
        for letter in word:

            number_symb_code_text = rev_alphabet_dict[letter]
            if i <= len(new_key):
                number_symb_key = rev_alphabet_dict[new_key[i]]

            else:
                i = 0
            numb_decode_text = (number_symb_code_text - number_symb_key) % 32
            abc += alphabet_dict[numb_decode_text]
            i += 1

        abc += " "

    return abc
    # number_symb_key = rev_alphabet_dict[]


string = "ШШЯССАБРШЭЭЧШЫ АФЫЛДВО"
phrase_key = "ОКТЯБРЬ"

print(encode(string, phrase_key))
