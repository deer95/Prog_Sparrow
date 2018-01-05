def sorter(word):
    return [hierarchy.index(c) for c in word]

words = 'ёжик ёцугаве елка ёлка жук животное ёёёшка её ёе еда ёруба'.lower()

hierarchy = 'абвгдеёжийклмнопрстуфхцчшщъыьэюя-'

word_list = words.split()

word_list.sort(key = sorter)

for word in word_list:
    print(word)
