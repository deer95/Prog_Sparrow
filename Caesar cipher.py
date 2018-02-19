from nltk import FreqDist
import os

def uncoder(n):
    cipher = open('caesar_cipher.txt', 'r', encoding='utf-8')
    uncoded_list = []
    i = 0
    for line in cipher:
        uncoded_list.append('')
        for sym in line:
            new_sym = chr(ord(sym) - n)
            uncoded_list[i] += new_sym
        i += 1
    cipher.close()
    return uncoded_list


n = 1
ok = False

while ok == False:
    full_text = uncoder(n)
    sample_list = full_text[0].split()
    uncoded_dict = FreqDist(sample_list).most_common(10)
    list_freqs = [elt[1] for elt in uncoded_dict]
    if max(list_freqs) > 2:
        ok = True
        print(n, 'is the right shift')
        print(uncoded_dict)
        uncoded_text = open('caesar_uncoded.txt', 'w', encoding='utf-8')
        for elt in full_text:
            uncoded_text.write(elt + '\n')
        uncoded_text.close()
        os.startfile('caesar_uncoded.txt')
    else:
        print(n, 'is not the right shift')
        n += 1
