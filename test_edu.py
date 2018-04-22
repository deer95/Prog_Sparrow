import re
from collections import Counter

def print_set(some_set):
    print(', '.join(str(i) for i in sorted(list(some_set))))

def print_dict(some_dict):
    print(', '.join(elt + ' : ' + str(some_dict[elt]) for elt in some_dict))

def print_list(some_list):
    print(len(some_list[0]), ':', ', '.join(some_list))

text = open('test_edu.txt', 'r', encoding='utf-8')

#x = int(input('Enter a threshold for vowels: '))
#y = int(input('Enter the needed number of most frequent words: '))
x = 5
y = 10

vowels = set('уеыаоэяиюё')
num_words, num_vowels, len_words = 0, 0, 0
little_words, big_vowels, proper_names = set(), set(), set()
max_len = []
cnt_letter, cnt_words = Counter(), Counter()

for line in text:
    line = re.sub('\d', '', line)
    line = re.sub('[^\w\s-]', '', line)
    line_list = line.split()
    num_words += len(line_list)

    for word in line_list:
        word.lower()
        '''ДЛИНЫ СЛОВ'''
        len_words += len(word)          # считаем суммарную длину слова

        if len(word) <= 3:              # находим слова длиной меньше 3
            little_words.add(word)

        if max_len == []:               # находим максимально длинное слово
            max_len.append(word)
        elif len(max_len[0]) < len(word):
            max_len.clear()
            max_len.append(word)
        elif len(max_len[0]) == len(word):
            max_len.append(word)

        '''СТАТИСТИКА СИМВОЛОВ'''
        word_vowels = 0
        for letter in word:                 # считаем гласные
            if letter in vowels:
                word_vowels += 1
            num_vowels += word_vowels       # считаем общее число гласных

            if word_vowels >= x:             # добавляем слова с числом гласных, большим Х
                big_vowels.add(word)

        '''СЛОЖНАЯ СТАТИСТИКА, RE'''
        cnt_letter += Counter(word)        # статистика по символам, несортированная

    cnt_words += Counter(line.lower().split())     # статистика по словам

    name = re.findall('(?!\A)[A-ZА-ЯЁ][a-zа-яё]*?\b', line)        # ищем имена собственные
    proper_names |= set(name)

'''СЧИТАЕМ СРЕДНИЕ ЗНАЧЕНИЯ И СОРТИРУЕМ'''
average_word_len = len_words / num_words        # средняя длина
average_vowels = num_vowels / num_words         # среднее число гласных
freq_most = cnt_words.most_common(y)

cnt_freq = Counter()                                                              # считаем ipm символов
for unique_word in cnt_words:
    frequency = cnt_words[unique_word] * 1000000 / num_words
    cnt_freq[frequency] = unique_word
    del cnt_freq[unique_word]

text.close()

'''ПЕЧАТЬ'''
print('Средняя длина слова =', average_word_len)
print('Среднее количество слогов =', average_vowels)
print('Самое длинное слово = ', end='')
print_list(max_len)
print('Слова из трёх и менее букв: ', end='')
print_set(little_words)
print('Слова с {} и более гласными: '.format(x), end='')
print_set(big_vowels)
print('{} самых частотных словоформ: '.format(y), end='')
print(cnt_words)
print('Статистика по символам: ', end='')
print(cnt_freq)
print('Имена собственные: ', end='')
print_set(proper_names)
