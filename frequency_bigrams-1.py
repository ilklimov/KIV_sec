from collections import Counter
from nltk import bigrams 

crypt = open("./voyna-i-mir-tom-1.txt","r", encoding="utf-8")
text_original = list(crypt.read())
text_original = list(bigrams(text_original))
text_original = list(map(lambda i: i[0] + i[1], text_original))

dict_original = dict(Counter(text_original))
list_original = list(dict_original.items())

list_original.sort(key=lambda i: i[1], reverse = True)
list_original = list(map(lambda i: i[0], list_original))


text_crypted_source = list(open("./text_crypt.txt","r", encoding="utf-8").read())
text_crypted = list(bigrams(text_crypted_source))
text_crypted = list(map(lambda i: i[0] + i[1], text_crypted))

dict_crypted = dict(Counter(text_crypted))
list_crypted = list(dict_crypted.items())

list_crypted.sort(key=lambda i: i[1], reverse = True)
list_crypted = list(map(lambda i: i[0], list_crypted))

for i in range(0,len(text_crypted_source)-1,2):
    current = text_crypted_source[i]+text_crypted_source[i+1]
    index = list_crypted.index(current)
    text_crypted_source[i] = list_original[index][0]
    text_crypted_source[i+1] = list_original[index][1]

final_text = ''.join(text_crypted_source)
crypt = open("./text_decrypt.txt", "w")
crypt.write(final_text)
crypt.close()

print('Результаты частотного анализа c биграмами\n', final_text)