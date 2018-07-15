import pymystem3
from collections import Counter
import csv

def print_most_common(items_list):
    print('Lemma frequency:')
    print(',\n'.join("'{}' : {}".format(str(elt[0]), str(elt[1])) for elt in items_list))

def print_csv(item_list):
    with open('word_bag_stat.csv', 'w', newline = '') as csv_file:
        csv_writer = csv.writer(csv_file, delimiter = ';')
        for item in item_list:
            csv_writer.writerow(item)

file = open('word_bag_text.txt', 'r', encoding = 'utf-8')
text = file.read()
file.close()

stemmer = pymystem3.Mystem(entire_input = False, speedup = True)
statistics = Counter()

if text == '\n':
    print('Your text is empty.')
else:
    lemmas = stemmer.lemmatize(text)
    statistics += Counter(lemmas)

print()
stat_sorted_list = statistics.most_common()
print_most_common(stat_sorted_list)
print_csv(stat_sorted_list)
