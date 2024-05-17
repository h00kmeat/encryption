def encode(string: str, gamma: str):
    alphabet_dict = {i: chr(i + 1040) for i in range(32)}
    rev_alphabet_dict = {chr(i + 1040): (i) for i in range(32)}
    new_string = ""
    if len(string) == len(gamma):
        for i in range(len(string)):
            number_symb_shifr_text = rev_alphabet_dict[string[i]]
            number_symb_gamma = rev_alphabet_dict[gamma[i]]
            number_symb_encode_text = (number_symb_shifr_text - number_symb_gamma) % 32
            new_string += alphabet_dict[number_symb_encode_text]
    return new_string


shift_text = "ФРЗОРРТЯЫРЗГТЭЕХКФЯБЮФМЫОМОЯЬ"
gamma = "РАЗДРАКОНДВАДРАКОНАТРИДРАКОНА"
print(encode(shift_text, gamma))
