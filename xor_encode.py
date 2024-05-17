def encode(list, gamma):
    gamma2 = ""
    for symb in list:
        gamma2 = bin(gamma)[2:]
        length = len(gamma2)
        symb2 = bin(symb)[2:]
        result = ""
        symb2 = (length - len(symb2)) * "0" + symb2
        for i in range(len(gamma2)):
            if i <= len(symb2):
                result += ((int(symb2[i]) + int(gamma2[i])) % 2).__str__()

            else:
                pass
        print(result)

    mlist = [0x52, 0x6F, 0x61, 0x6D, 0x69, 0x6E, 0x67]
    for i in mlist:
        print(chr(i))

        # result = (i+)


shifr_text16 = [0x03, 0x3E, 0x30, 0x3C, 0x38, 0x3F, 0x36]
gamma = 0x51

encode(shifr_text16, gamma)
