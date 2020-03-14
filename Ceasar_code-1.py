# -*- coding: utf-8 -*-
def crypt_ceasar(message):
    alphabet_lower = [chr(ord("а") + i) for i in range(32)]
    alphabet_upper = [chr(ord("А") + i) for i in range(32)]
    shifr = []
    for i in range(len(message)):
        if message[i] in alphabet_upper:
            k = alphabet_upper.index(message[i])
            shifr.append(alphabet_upper[(k + step) % 32])
        elif message[i] in alphabet_lower:
            k = alphabet_lower.index(message[i])
            shifr.append(alphabet_lower[(k + step) % 32])
        else:
            shifr.append(message[i])
    shifr_str = ''.join(shifr)
    return shifr_str

print('''Шифр Цезаря
Введите (1), чтобы зашифровать текст из потока ввода.
Введите (2), чтобы зашифровать текст из файла. 
 ''')

try:

    option = int(input(" - Выберите опцию:\n"))
    if option == 1:
        print(' - Введите ключ-число от 0 до 32')
        step = int(input())
        message = input("\n - Введите текст: \n")
        shifr_str = crypt_ceasar(message)
        crypt = open("./text_crypt.txt", "w")
        print("\n - Зашифрованный текст:" + shifr_str + "\n")
        crypt.write(shifr_str)
        crypt.close()

    elif option == 2:
        print(' - Введите ключ-число от 0 до 32')
        step = int(input())

        print("\n - Поместите текстовый файл в папку и назоваите его text_to_crypt.txt ")
        crypt = open("./text_to_crypt.txt","r", encoding="utf-8")
        read = crypt.read()
        shifr_str = crypt_ceasar(read)
        crypt = open("./text_crypt.txt", "w")
        print("\n - Зашифрованный текст:" + shifr_str + "\n")
        crypt.write(shifr_str)
        crypt.close()
    else:
        print(' - Опция не выбрана!')
except ValueError:
    print("Введите нормальное число!")