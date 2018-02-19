import os

cipher = open('caesar_cipher.txt', 'w', encoding='utf-8')
text = open('caesar_text.txt', 'r', encoding='utf-8')
n = 5

for line in text:
    for sym in line:
        new_sym = chr(ord(sym) + n)
        cipher.write(new_sym)

text.close()
cipher.close()

os.startfile('caesar_cipher.txt')
