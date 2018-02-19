ind = 0
num_even = 0
num_printed = 0

while True:
    s = input('Слово N {}: '.format(ind))
    if s == '':
        break
    len_s = len(s)
    if len_s % 2 == 1:
        print('Слово "{}" длины {} с индексом {}'.format(s, len_s, ind))
        num_printed += 1
    else:
        num_even += 1
    ind += 1

if num_printed < 1:
    print('Все слова четной длины')

print('Количество чисел четной длины =', num_even)
