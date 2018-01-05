import re

def sorter(word):
    return word[::-1]


text = open('8.Backwards_Dictionary_text.txt', 'r', encoding = 'utf-8')
text_array = set()

for line in text:
    line = line.split()
    for word in line:
        text_array.add(re.sub('[^\w-]', '', word))

text_array = list(text_array)
text_array.sort(key=sorter)

for elt in text_array:
    print(elt)


text.close()
