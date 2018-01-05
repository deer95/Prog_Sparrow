import re

def sorter(word):
    return [hierarchy.index(ord(word[i])) for i in range(len(word))]

text = 'Qatna (modern: Arabic, Tell al-Mishrifeh) is an ancient city located in Homs Governorate, Syria. Its remains constitute a tell situated about 18 km (11 mi) northeast of Homs near the village of al-Mishrifeh. The city was an important center throughout most of the second millennium BC and in the first half of the first millennium BC. It contained one of the largest royal palaces of Bronze Age Syria and an intact royal tomb that provided a great amount of data on the funerary habits of that period.'.lower()
text = re.sub('[!@$%\^&\*\(\)\?><,\.\":;1234567890]', '', text)
text_array = set(text.split())
#list(text_array).sort(key = sorter)
#for elt in text_array:
#    print(elt)

text_array = sorted(list(text_array))
for i in range(len(text_array) - 1, -1, -1):
    print(text_array[i])
