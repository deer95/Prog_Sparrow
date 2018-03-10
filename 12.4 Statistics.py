import re

print('There are three kinds of lies: lies, damned lies and statistics.')

in_file = open('12_txt/12.4-input.txt', 'r', encoding='utf-8')
lines = 0
words = 0
letters = 0

for line in in_file:
    new_line = re.sub('[^\w\s]', '', line).split()
    lines += 1
    words += len(new_line)
    for word in new_line:
        letters += len(word)

print('Input file contains:')
print(letters, 'letters')
print(words, 'words')
print(lines, 'lines')
