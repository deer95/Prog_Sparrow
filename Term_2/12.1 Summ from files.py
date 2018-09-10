import re

first = open('12_txt/12.1-first.txt', 'r', encoding='utf-8')
second = open('12_txt/12.1-second.txt', 'r', encoding='utf-8')

alltext = first.readlines()
alltext.extend(second.readlines())
summ = 0

for elt in alltext:
    decimal = re.sub('\D', '', elt)
    if decimal != '':
        summ += int(decimal)
print(summ)
