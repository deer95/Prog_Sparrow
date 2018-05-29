import pymystem3
import re
from collections import Counter

def print_most_common(items_list):
    print('Lemma frequency:')
    print(',\n'.join("'{}' : {}".format(str(elt[0]), str(elt[1])) for elt in items_list))


file = open('word_bag_text.txt', 'r', encoding = 'utf-8')
text = file.read()
file.close()

stemmer = pymystem3.Mystem(entire_input = False, disambiguation = True, speedup=True)
statistics_list = []
num_line = 0
pos = set(['A', 'ANUM', 'APRO'])


num_line += 1
if text == '\n':
    print('Your text is empty.')
else:
    stems_list = stemmer.analyze(str(text))
    for token_dict in stems_list:
        lemma_list = token_dict['analysis']
        if lemma_list != []:
            lexeme_dict = lemma_list[0]
            gr_description = lexeme_dict['gr']
            a = str(re.findall('\A[\w]+=\(]', gr_description))
            if a in pos:
                statistics_list.append(lexeme_dict['lex'])

    print('Line #', num_line, 'analysed.')

    print()
    print_most_common(Counter(statistics_list).most_common())
