import heapq


def counter_char_in_string(string):
    count_letter = {}
    for letter in string:
        if letter.isalpha():
            if letter in count_letter:
                count_letter[letter] += 1
            else:

                count_letter[letter] = 1
    return count_letter


def get_letter_freq(dict):
    sum_all_values = sum(dict.values())
    freq = {}
    for i, j in dict.items():
        freq[i] = j / sum_all_values * 100

    return freq


def replace_letter_in_string(string, freq_letter, most_freq_letter):
    new_freq_letter = {
        k: v
        for k, v in freq_letter.items()
        if any(v == e for e in heapq.nlargest(4, freq_letter.values()))
    }

    new_freq_letter = dict(sorted(new_freq_letter.items(), key=lambda x: -x[1]))
    new_string = ""
    let_most = {k1: k2 for k1, k2 in zip(new_freq_letter, most_freq_char)}
    for letter in string:

        if letter.isalpha():
            if any(letter == char for char in let_most.keys()):
                new_string = new_string + let_most[letter]
            else:
                new_string = new_string + letter
        else:
            new_string = new_string + letter

    print(new_freq_letter)
    print(let_most)
    print(new_string)


string = "ФЙИ-ЭЕИ ЦСИЧМСО М ШДТЫСЮБШДС, ЩС ЦЙТЫЙМЖЙЬ ЖИПГА УЧБШДЙ. ЧЩ М ЩСЬ ЩСМЛЩШЦШЬ ЛШМШЮЙМШИ ЦШЬ Й М ЩСЬ ФС УАИПИ М ШДТЫСЮБШДС."
print(string)
print("\n")

# string = string.replace("И", "Е")

string = string.replace("Ж", "ш")
string = string.replace("О", "к")
string = string.replace("Ф", "ж")
string = string.replace("И", "л")
string = string.replace("Й", "и")
string = string.replace("Э", "б")
string = string.replace("Е", "ы")
string = string.replace("С", "е")

string = string.replace("Щ", "н")
string = string.replace("Ч", "о")

string = string.replace("Ц", "ч")
string = string.replace("М", "в")
string = string.replace("Ь", "й")
string = string.replace("Т", "с")
string = string.replace("Ы", "т")
string = string.replace("П", "я")
string = string.replace("Г", "п")
string = string.replace("А", "у")
string = string.replace("У", "г")
string = string.replace("Б", "д")
string = string.replace("Ш", "а")
string = string.replace("Д", "м")
string = string.replace("Ю", "р")
string = string.replace("Л", "з")

# string = string.replace("Е", "В")
print(string)
# char_count = counter_char_in_string(string)
# most_freq_char = {"О": 8.02, "Е": 7.98, "А": 8.02, "И": 7.54}
# most_freq_char = dict(sorted(most_freq_char.items(), key=lambda x: -x[1]))
# print(most_freq_char)
# print("\n")
# replace_letter_in_string(string, get_letter_freq(char_count), most_freq_char)
