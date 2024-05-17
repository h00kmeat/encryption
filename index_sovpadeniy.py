from collections import defaultdict


def calculate_index_match(string: str):
    string = string.split()
    length_symb_in_string = 0
    count_symb = defaultdict(int)
    for word in string:
        length_symb_in_string += len(word)
        for letter in word:
            count_symb[letter] += 1
    list_keys = list(count_symb.keys())
    index_match = sum(
        [
            count_symb[list_keys[i]]
            * (count_symb[list_keys[i]] - 1)
            / (length_symb_in_string * (length_symb_in_string - 1))
            for i in range(len(list_keys))
        ]
    )
    # char : int
    return index_match


string = "ВАРИС ВАРИТ ВАТУ"

print(calculate_index_match(string))
