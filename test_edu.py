import re
from collections import Counter

def print_set(some_set):
    print(', '.join(str(i) for i in sorted(list(some_set))))

def print_dict(some_dict):
    print(', '.join(item + ' : ' + str(some_dict[item]) for item in some_dict))

def print_list(some_list):
    print(len(some_list[0]), ':', ', '.join(some_list))

def print_most_common(some_list):
    print(',\n'.join("'{}' : {}".format(str(elt[0]), str(elt[1])) for elt in some_list))

text = open('test_edu.txt', 'r', encoding='utf-8')

#x = int(input('Enter a threshold for vowels: '))
#y = int(input('Enter the needed number of most frequent words: '))
x = 5
y = 10

vowels = set('уеыаоэяиюё')
num_words, num_vowels_int, len_words_int = 0, 0, 0
short_words_set, x_vowels_set, proper_names_set = set(), set(), set()
max_len_list = []
cnt_symbol, cnt_words = Counter(), Counter()

for line in text:
    line_list = line.split()
    num_words += len(line_list)

    for raw_word in line_list:
        word = re.search("[A-Za-zЁёА-Яа-я'`-]*", raw_word).group()      # определяем, что такое слово
        if word == '':                                                  # если ничего не нашлось, приступаем к следующему слову
            continue
        word = word.lower()

        '''ДЛИНЫ СЛОВ'''
        word_len_int = len(word)                # смотрим длину конкретного слова
        len_words_int += word_len_int           # считаем суммарную длину слова

        if word_len_int <= 3:                   # находим слова длиной меньше 3
            short_words_set.add(word.lower())

        if max_len_list == []:                  # находим максимально длинное слово
            max_len_list.append(word.lower())
        elif len(max_len_list[0]) < word_len_int:
            max_len_list.clear()
            max_len_list.append(word)
        elif len(max_len_list[0]) == word_len_int:
            max_len_list.append(word.lower())

        '''ЧИСЛО ГЛАСНЫХ'''
        word_vowels = 0
        for letter in word:                         # считаем гласные
            if letter in vowels:
                word_vowels += 1
            num_vowels_int += word_vowels           # считаем общее число гласных

            if word_vowels >= x:                    # добавляем слова с числом гласных, большим Х
                x_vowels_set.add(word.lower())

    '''СЛОЖНАЯ СТАТИСТИКА'''
    cnt_symbol += Counter(line)                     # статистика по символам, несортированная
    cnt_words += Counter(line.lower().split())      # статистика по словам

    '''ИМЕНА СОБСТВЕННЫЕ'''
    for sentence in line.split('.'):
        name_list = re.findall('[a-zа-яё]*[\'`-]*[A-ZА-ЯЁ][a-zа-яё]*[\'`-]*[A-ZА-ЯЁ]*[a-zа-яё]+', sentence)
        proper_names_set |= set(name_list[1:])

'''СЧИТАЕМ СРЕДНИЕ ЗНАЧЕНИЯ И IPM'''
average_word_len = len_words_int / num_words        # средняя длина
average_vowels = num_vowels_int / num_words         # среднее число гласных
freq_words_list = cnt_words.most_common(y)          # находим Y самых частотных словоформ

cnt_freq = Counter()                                # считаем ipm символов
for unique_word in cnt_symbol:
    frequency = round(cnt_symbol[unique_word] * 1000000 / num_words, 3)
    cnt_freq[unique_word] = frequency
freq_sym_list = cnt_freq.most_common()

text.close()

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
print_most_common(freq_sym_list)
print('Имена собственные: ', end='')
print_set(proper_names_set)
