import pymystem3
import re
from collections import Counter

def print_most_common(items_list):
    print('Lemma frequency:')
    print(',\n'.join("'{}' : {}".format(str(elt[0]), str(elt[1])) for elt in items_list))


file = open('word_bag_text.txt', 'r', encoding = 'utf-8')
text = file.read()
file.close()

stemmer = pymystem3.Mystem(entire_input = False, disambiguation = True)
adj_set = set(['A', 'ANUM', 'APRO'])
statistics_list = []

if text == '\n':
    print('Your text is empty.')
else:
    stems_list = stemmer.analyze(str(text), speedup=True)
    for token_dict in stems_list:
        print(token_dict)
        lemma_list = token_dict['analysis']
        print(lemma_list)
        if lemma_list != []:
            lexeme_dict = lemma_list[0]
            print(lexeme_dict)
            gr_description = lexeme_dict['gr']
            pos = re.match('\A[\w]+(?==)', gr_description)
            if pos is not None:
                pos = pos.group()
                if pos in adj_set:
                    statistics_list.append(lexeme_dict['lex'])

print_most_common(Counter(statistics_list).most_common())
