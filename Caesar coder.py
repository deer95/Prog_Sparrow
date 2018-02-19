import os

cipher = open('cipher.txt', 'w', encoding='utf-8')
text = open('text_caesar.txt', 'r', encoding='utf-8')
n = 3

for line in text:
    for sym in line:
        new_sym = chr(ord(sym) + n)
        cipher.write(new_sym)

text.close()
cipher.close()

os.startfile('D:\PyProjects_SD\Sparrow_2\cipher.txt')
