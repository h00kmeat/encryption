def decode(string):
    row, column = 1, 0
    tabl = {}
    for word in string:
        for letter in word:
            column += 1
            if column == 8 + 1:
                column = 1
                if row <= 6:
                    row += 1
                else:
                    break

            tabl[(row, column)] = letter

    decode_tabl = ""
    for column in range(1, 9):
        for row in range(1, 7):
            decode_tabl = decode_tabl + tabl[(row, column)]

    print(decode_tabl)


string = "Джон истинный Таргариен и законный наследник Вестероса"
string1 = string.split(" ")
# print(string1)
decode(string1)
