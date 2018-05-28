import re
from collections import Counter

def print_set(some_set):
    print(', '.join(str(i) for i in sorted(some_set)))

def print_dict(some_dict):
    print(', '.join(key + ' : ' + str(some_dict[key]) for key in some_dict))

def print_list(some_list):
    print(len(some_list[0]), ':', ', '.join(some_list))

def print_most_common(items_list):
    print(',\n'.join("'{}' : {}".format(str(elt[0]), str(elt[1])) for elt in items_list))


def print_most_common_percents(cnt):
    n_symbols = sum (cnt.values())
    print(',\n'.join("{} : {:.3%}".format(repr (sym), n_sym / n_symbols) for sym, n_sym in cnt.most_common()))

file = open('test_edu.txt', 'r', encoding='utf-8')

#x = int(input('Enter a threshold for vowels: '))
#y = int(input('Enter the needed number of most frequent words: '))
x = 5
y = 10

vowels = set('уеыаоэяиюё')
num_words, total_num_vowels_int, total_len_words_int, total_symbols_int = 0, 0, 0, 0
short_words_set, x_vowels_set, proper_names_set = set(), set(), set()
max_len_list = []
cnt_symbol, cnt_words = Counter(), Counter()

for line in file:
    line_list = line.split()

    for raw_word in line_list:
        word = re.search("[А-Яа-яЁё]+(['`-][А-Яа-яЁё]+)*", raw_word)        # определяем, что такое слово
        if word:
            word = word.group()
        else:
            continue

        word = word.lower()
        num_words += 1
        cnt_words[word] += 1                    # считаем статистику словоформ

        '''ДЛИНЫ СЛОВ'''
        word_len_int = len(word)                # смотрим длину конкретного слова
        total_len_words_int += word_len_int           # считаем суммарную длину слова

        if word_len_int <= 3:                   # находим слова длиной меньше 3
            short_words_set.add(word)

        if (not max_len_list) or (len(max_len_list[0]) < word_len_int):
            max_len_list = [word]
        elif len(max_len_list[0]) == word_len_int:
            max_len_list.append(word)

        '''ЧИСЛО ГЛАСНЫХ'''
        word_vowels = 0
        for letter in word:                         # считаем гласные
            if letter in vowels:
                word_vowels += 1
            total_num_vowels_int += word_vowels           # считаем общее число гласных

            if word_vowels >= x:                    # добавляем слова с числом гласных, большим Х
                x_vowels_set.add(word)

    '''СЛОЖНАЯ СТАТИСТИКА'''
    cnt_symbol += Counter(line.lower())                     # статистика по символам, несортированная
    total_symbols_int += len(line)

    '''ИМЕНА СОБСТВЕННЫЕ'''
    for sentence in re.split(r'[.?!\n]+', line):
        name_list = re.findall("(?x)    ((?:[а-яё]['`])?     [А-ЯЁ][А-ЯЁа-яё]*    (?:['`-][А-ЯЁа-яё]+)*)", sentence)
        proper_names_set |= set(name_list[1:])
file.close()

'''СЧИТАЕМ СРЕДНИЕ ЗНАЧЕНИЯ И ПРОЦЕНТЫ'''
average_word_len = total_len_words_int / num_words        # средняя длина
average_vowels = total_num_vowels_int / num_words         # среднее число гласных
freq_words_list = cnt_words.most_common(y)          # находим Y самых частотных словоформ

'''ПЕЧАТЬ'''
print('Средняя длина слова =', average_word_len)
print('Среднее количество слогов =', average_vowels)
print('Самое длинное слово = ', end='')
print_list(max_len_list)
print('Слова из трёх и менее букв: ', end='')
print_set(short_words_set)
print('Слова с {} и более гласными: '.format(x), end='')
print_set(x_vowels_set)
print('{} самых частотных словоформ: '.format(y))
print_most_common(freq_words_list)
print('Статистика по символам: ')
print_most_common_percents(cnt_symbol)
print('Имена собственные: ', end='')
print_set(proper_names_set)
