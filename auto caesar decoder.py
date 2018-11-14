import random
import numpy as np
import time_speaker
from collections import Counter

def shifter(int_letter, shift, start_letter, end_letter):
    new_int_letter = int_letter + shift
    if new_int_letter > ord(end_letter):
        new_int_letter = new_int_letter - ord(end_letter) + ord(start_letter) - 1
    new_letter = chr(new_int_letter)
    return new_letter


def shift_text(text, shift):
    # кодируем текст, сдвигая символы на случайное число
    new_text = ''
    for line in text:
        new_line = ''
        for letter in line:
            int_letter = ord(letter)
            if ord('а') <= int_letter <= ord('я'):
                new_letter = shifter(int_letter, shift, 'а', 'я')
            elif ord('А') <= int_letter <= ord('Я'):
                new_letter = shifter(int_letter, shift, 'А', 'Я')
            else:
                new_letter = letter
            new_line += new_letter
        new_text += new_line
    return new_text


def get_freq(text):
    # делаем список частот, упорядоченный по алфавиту
    letter_freq = Counter()
    for line in text:
        for letter in line:
            if ord('А') <= ord(letter) <= ord('я'):
                letter_freq[letter.lower()] += 1
    # добавляем недостающие буквы
    letter_set = set(letter_freq.keys())
    for check_let in 'йцукенгшщзхъфывапролджэячсмитьбю':
        if check_let not in letter_set:
            letter_freq[check_let] = 0
    letter_freq = sorted(letter_freq.items(), key=lambda x: x[0])
    return [elt[1] for elt in letter_freq]


def decoder(text, ex_freq):
    shift = 0
    max_prod = 0
    for i in range(len(ex_freq)):
        shifted_text = shift_text(text, i)
        text_freq = get_freq(shifted_text)
        current_diff = np.vdot(ex_freq, text_freq)
        if current_diff > max_prod:
            max_prod = current_diff
            shift = i
    return shift

t = time_speaker.time_speaker()
# задаем сдвиг
start_shift = 32
#start_shift = random.randint(1, 32)
#start_shift = int(input('Ваш сдвиг: '))
print('Стартовый сдвиг =', start_shift)

# открываем и шифруем текст
infile = open('start_text.txt', 'r', encoding='utf-8')
intext = infile.readlines()
infile.close()
coded_text = shift_text(intext, start_shift)

# пишем зашифрованный текст
outfile = open('coded_text.txt', 'w', encoding='utf-8')
outfile.write(coded_text)
outfile.close()

# учим машину частоте символов
example_text = open('caesar_teacher.txt', 'r', encoding='utf-8')
example_freq = get_freq(example_text)
example_text.close()

# расшифровываем
shift2know = decoder(coded_text, example_freq)
print('Декодированный сдвиг =', -(shift2know-32))

# пишем рсшифрованный текст
uncoded_file = open('uncoded_text.txt', 'w', encoding='utf-8')
uncoded_text = shift_text(coded_text, shift2know)
uncoded_file.write(uncoded_text)
uncoded_file.close()
print(time_speaker.time_speaker() - t)
