# array = [chr(i + 1040) for i in range(32)]
# matrix = [array[i:] + array[:i] for i in range(32)]

phrase_key = "ПОЛНАЯ ПОБЕДА"
open_text = "И ДЫМ ОТЕЧЕСТВА НАМ СЛАДОК И ПРИЯТЕН"


def decode(string, key):
    alphabet_dict = {i: chr(i + 1040) for i in range(32)}
    rev_alphabet_dict = {chr(i + 1040): (i) for i in range(32)}
    new_string = ""
    length_key = len(key)
    length_string = len(string)
    print(
        f"Словарь алфавита:\n '{alphabet_dict}'\n Словарь обратного алфавита:\n '{rev_alphabet_dict}'\n"
    )
    print(length_string)
    for i in range(length_string):
        if string[i].isalpha():
            print(f"string['{i}']", string[i])
            number_symb_open_text = rev_alphabet_dict[string[i]]
            if key[i % (length_key - 1)].isalpha():
                if i == 0:
                    number_symb_key = rev_alphabet_dict[key[i % (length_key - 1)]]
                else:
                    number_symb_key = rev_alphabet_dict[key[(i - 1) % (length_key - 1)]]
            else:
                number_symb_key = rev_alphabet_dict[key[i % (length_key - 1) + 1]]
            print(
                "Буква открытого текста :",
                alphabet_dict[number_symb_open_text],
                f"ей соответсвует номер:'{number_symb_open_text}'",
            )
            print(
                "Буква ключа, :",
                alphabet_dict[number_symb_key],
                f" ей соответсвтует номер:'{number_symb_key}'",
            )
            print((number_symb_open_text + number_symb_key) % 32)
            new_symb = alphabet_dict[(number_symb_open_text + number_symb_key) % (32)]
            new_string += new_symb
        else:

            new_string += string[i]

        print(f"Новая строка: '{new_string}'")

    return new_string


print(decode(open_text, phrase_key))
