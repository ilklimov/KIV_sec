from collections import Counter

crypt = open("./voyna-i-mir-tom-1.txt","r", encoding="utf-8")
text_original = list(crypt.read())
dict_original = dict(Counter(text_original))
list_original = list(dict_original.items())

list_original.sort(key=lambda i: i[1], reverse = True)
list_original = list(map(lambda i: i[0], list_original))

crypt = open("./text_crypt.txt","r", encoding="utf-8")
text_crypted = list(crypt.read())
dict_crypted = dict(Counter(text_crypted))
list_crypted = list(dict_crypted.items())

list_crypted.sort(key=lambda i: i[1], reverse = True)
list_crypted = list(map(lambda i: i[0], list_crypted))

for i in range(len(text_crypted)):
    text_crypted[i] = list_original[list_crypted.index(text_crypted[i])]

final_text = ''.join(text_crypted)
crypt = open("./text_decrypt.txt", "w")
crypt.write(final_text)
crypt.close()

print('Результаты частотного анализа:\n', final_text)

