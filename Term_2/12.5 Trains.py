print('Trains are the world greatest evil.')

in_file = open('12_txt/12.5-travelling.txt', 'r', encoding='utf-8')
info = in_file.readlines()

spans = int(info.pop(0))
span_list = [0 for i in range(spans)]               # генерируем список перегонов, пока с нулевым числом пассажиров
for elt in info:
    new_list = elt.split()
    del new_list[:2]                                # удаляем имена
    start, end = int(new_list[0]), int(new_list[1])
    for j in range(start, end):                     # прибавляем 1 к каждому перегону, где кто-то едет
        span_list[j - 1] += 1

max_num = max(span_list)                            # ищем максимальное число пассажиров
for n in range(len(span_list)):                     # если число на перегоне максимально, печатаем его
    if span_list[n] == max_num:
        print('На перегоне {} - {}'.format(n + 1, n + 2))
print('число пассажиров было максимально. Их количество достигало {}.'.format(max_num))
