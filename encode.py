string = "ЖИЛ-БЫЛ СТАРИЧОК ИЗ ГОНКОНГА, ТАНЦЕВАВШИЙ ПОД МУЗЫКУ ГОНГА. НО ЕМУ ЗАЯВИЛИ: ПРЕКРАТИ ЭТО, ИЛИ УБИРАЙСЯ СОВСЕМ ИЗ ГОНКОНГА!"
alphabet_dict = {i: chr(i + 1040) for i in range(32)}

for k, v in alphabet_dict.items():
    a = input(f"Enter the '{v}' replace to: ")
    string = string.replace(v, a)
print(string)
