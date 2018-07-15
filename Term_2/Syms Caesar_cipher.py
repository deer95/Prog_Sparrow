from nltk import FreqDist
import os
import math
import re

'''ENTROPY COUNT'''
def entropy(labels):
    freqdist = FreqDist(labels)
    probs = [freqdist.freq(l) for l in freqdist]
    return -sum(p * math.log(p,2) for p in probs)

'''DECODER'''
def decode(sym):
    new_num = alphabet.index(sym) - n
    if new_num < 0:
        new_num += len(alphabet)
    new_sym = alphabet[new_num]
    return new_sym

'''MAKE TUPLE OF WORDS WITH THEIR ENTROPY'''
cipher = open('caesar_cipher.txt', 'r', encoding='utf-8')
word_set = set()
word_list = []

for line in cipher:                 # make a set of all words
    line = line.split()
    for word in line:
        word = re.sub('[^\w-]', '', word)
        word_set.add(word)

for word_form in word_set:          # make a tuple of words with their entropy
    word_list.append((word_form, entropy(word_form)))

word_list.sort(key= lambda x: x[1], reverse=True)   # make a tuple, sorted by entropy in reverse

'''MAKING GUESSES'''
sample = word_list[0][0]
alphabet = 'а б в г д е ж з и й к л м н о п р с т у ф х ц ч ш щ ъ ы ь э ю я'.split()
n = 0
new_word = ''
answer = input('Is ' + sample + ' ok? If no, press ENTER.')

while answer == '':             # try to guess until the answer satisfies us
    n += 1
    new_word = ''
    for sym in sample:
        new_sym = decode(sym)
        new_word += new_sym
    answer = input('Is ' + new_word + ' ok? If no, press ENTER.')

'''DECODING THE WHOLE TEXT'''
cipher = open('caesar_cipher.txt', 'r', encoding='utf-8')
decoded = open('caesar_uncoded.txt', 'w', encoding='utf-8')

for line in cipher:
    for sym in line:
        if sym.lower() in alphabet:
            if sym.lower() == sym:
                new_sym = decode(sym)
            else:
                new_sym = decode(sym.lower()).upper()
        else:
            new_sym = sym
        decoded.write(new_sym)

'''PRINT RESULTS, CLOSE FILES, START THE FINAL FILE'''
print('\nShift =', n)
cipher.close()
decoded.close()
os.startfile('caesar_uncoded.txt')
