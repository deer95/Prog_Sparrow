import pymystem3
from collections import Counter

def print_most_common(items_list):
    print('Lemma frequency:')
    print(',\n'.join("'{}' : {}".format(str(elt[0]), str(elt[1])) for elt in items_list))


text = open('word_bag_text.txt', 'r', encoding = 'utf-8')
stemmer = pymystem3.Mystem(entire_input = False)
statistics = Counter()
num_line = 0

for line in text:
    num_line += 1
    print('Line #', num_line, 'analysed.')
    if line == '\n':
        continue
    lemmas = stemmer.lemmatize(line)
    statistics += Counter(lemmas)

print()
print_most_common(statistics.most_common())
