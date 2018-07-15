import os

def code(sym):
    new_num = alphabet.index(sym) + n
    if new_num >= len(alphabet):
        new_num -= len(alphabet)
    new_sym = alphabet[new_num]
    return new_sym

cipher = open('caesar_cipher.txt', 'w', encoding='utf-8')
text = open('caesar_text.txt', 'r', encoding='utf-8')

n = 7
alphabet = 'а б в г д е ж з и й к л м н о п р с т у ф х ц ч ш щ ъ ы ь э ю я'.split()

for line in text:
    for sym in line:
        if sym == 'ё':
            sym = 'е'
        if sym.lower() in alphabet:
            if sym.lower() == sym:
                new_sym = code(sym)
            else:
                new_sym = code(sym.lower()).upper()
        else:
            new_sym = sym
        cipher.write(new_sym)

text.close()
cipher.close()

os.startfile('caesar_cipher.txt')
