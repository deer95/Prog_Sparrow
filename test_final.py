import re
from collections import Counter
import pymystem3

def print_most_common(items_list):
    print(',\n'.join("'{}' : {}".format(str(elt[0]), str(elt[1])) for elt in items_list))


def print_stat(dictionary, num_tokens, x):
    ipm_dict = {}
    cnt_items = Counter(dictionary).most_common(x)
    for elt in cnt_items:
        print('{} : {}, ipm = {}'.format(elt[0], elt[1], elt[1] * 10**6 / num_tokens))


def authors_func(file):
    authors_set = set()
    authors_num = 0
    # считаем авторов
    for line in file:
        author = re.findall('(?<=<author>/)[\w_-]+?/([\w_.-]+)(?=/</author>)', line)
        authors_num += len(author)
        authors_set |= set(author)
    print('Number of all authors:', authors_num)
    print('Number of unique authors:', len(authors_set))

    # создаем файл и пишем туда отсортированных авторов
    file_path = input('What and where would you like to create a file?  ')
    authors_file = open(file_path + '.txt', 'w', encoding='utf-8')
    authors_sorted = sorted(list(authors_set))
    for i in range(len(authors_sorted)):
        authors_file.write(str(i + 1) + '. ' + authors_sorted[i] + '\n')
    authors_file.close()
  
    # выводим автора под нужным номером
    while True:
        num_name = input('What author would you like to see?  ')
        if num_name.isdigit():
            num_name = int(num_name)
            if num_name < 0 and num_name > len(authors_set):
                print('Sorry, your number is inappropriate. Try something between 0 and', len(authors_set))
                continue
            else:
                break
        else:
          print('Sorry, it is not a digit. Try to input a number.')
          continue
    print('{}. {}'.format(num_name, authors_sorted[num_name - 1]))


def messages(file):
    new_file = open('out2.txt', 'w', encoding='utf-8')
    text = file.read()
    nbsp_total, dots_total, links_total, hyphen_total = 0, 0, 0, 0
    len_start, len_middle, len_end = 0, 0, 0
    hyphen_longest, hyphen_most = (0, ''), (0, '')
    hyphen_words_total = []
    mnenonics_cnt = Counter()
    num_messages = 0

    # смотрим неразрывные пробелы и количество текстов
    messages_list = re.findall('(?<=<text><o>).*?(?=</o></text>)', text, flags=re.S)
    num_texts = len(messages_list)
    for message in messages_list:
        len_start += len(message)
        nbsp_total += len(re.findall('\xa0', message))
        dots_total += len(re.findall('…', message))

        # смотрим мнемоники
        text_mnemonics = re.findall('&[\w]+;', message)
        mnenonics_cnt += Counter(text_mnemonics)

        # производим замены
        message = re.sub('\xa0', '  ', message)
        message = re.sub('…', '...', message)
        message = re.sub('&quot;', '"', message)
        message = re.sub('&apos;', "'", message)
        message = re.sub('&amp;', '&', message)
        message = re.sub('&gt;', '>', message)
        message = re.sub('&lt;', '<', message)

        len_middle += len(message)

        # работаем со ссылками
        message, links_num = re.subn(r'\b(?:https?|ftp)://\S+', '', message)
        links_total += links_num

        # считаем дефисы и слова с ними
        hyphen_words = re.findall('[А-ЯЁ][а-яё]*(?:-[А-ЯЁа-яё]+){2,}', message)
        if hyphen_words:
            hyphen_total += len(hyphen_words)
            hyphen_words_total += hyphen_words
            for word in hyphen_words:
                hyphen_word_len = len(word)
                if hyphen_word_len > hyphen_longest[0]:
                    hyphen_longest = (hyphen_word_len, word)
                    # max (list, key = len)

                hyphen_num = word.count('-')
                if hyphen_num > hyphen_most[0]:
                    hyphen_most = (hyphen_num, word)


        # отрезаем пробелы и смотрим длину сообщения
        message = message.strip()
        len_end += len(message)

        # записываем русские сообщения в файл
        if re.fullmatch(r'[\WА-ЯЁа-яё0-9_]+', message):
            new_file.write(message + '\n===\n')
            num_messages += 1
    new_file.close()

    print('Number of texts:', num_texts)
    print('Number of unbreakable spaces:', nbsp_total)
    print('Number of three dots:', dots_total)
    print('Mnemonics:')
    print_most_common(mnenonics_cnt.most_common())
    print('Number of links:', links_total)
    print('Length of the text at the start:', len_start)
    print('Length of the text in the middle:', len_middle)
    print('Length of the text at the end:', len_end)
    print('Number of words with hyphen(s):', hyphen_total)
    print('The longest word with hypens:', hyphen_longest[1])
    print('The word with the biggest number of hyphens:', hyphen_most[1])

    #hyphen_instances_num = int(input('How many words with hyphens do you want?  '))
    hyphen_instances_num = 2
    print('The first {} instances are:'.format(hyphen_instances_num))
    for i in range(hyphen_instances_num):
        print('{}. {}'.format(i+1, hyphen_words_total[i]))

    print('\nNumber of Russian non-empty messages:', num_messages)


def stemming():
    case_set = set(['вин', 'пр', 'местн'])
    vowels_set = set('уеыаоэяиюё')
    num_words = 0
    pos_statistics, verb_stat, na_stat = {}, {}, {}

    # анализируем текст и считаем количество токенов
    stemmer = pymystem3.Mystem(entire_input=False)
    token_list = stemmer.analyze(file_path='out2.txt', speedup=True)
    num_tokens = len(token_list)

    # считаем абс. частоту для прилагательных, глаголов, существительных, предлогов
    for i in range(len(token_list)):
        token_dict = token_list[i]
        lemma_list = token_dict['analysis']
        if lemma_list != []:
            lexeme_dict = lemma_list[0]
            gr_description = lexeme_dict['gr']
            pos = re.match('\w+', gr_description)
            if pos is not None:
                num_words += 1
                pos = pos.group()
                pos_statistics[pos] = pos_statistics.get(pos, 0) + 1

                # статистика для глагола
                if pos == 'V':
                    word = lexeme_dict['lex']
                    verb_stat[word] = verb_stat.get(word, 0) + 1

            # статистика по 'на'
            if lexeme_dict['lex'] == 'на':
                next_token_dict = token_list[i + 1]
                next_lemma_list = next_token_dict['analysis']
                if next_lemma_list != []:
                    next_lexeme_dict = next_lemma_list[0]
                    next_gr_description = next_lexeme_dict['gr']
                    case = re.search('(?<==\()\w+', next_gr_description)
                    if case:
                        case = case.group()
                        if case in case_set:
                            if case == 'вин':
                                na_stat['внинительный'] = na_stat.get(case, 0) + 1
                            if case in set(['пр', 'местн']):
                                na_stat['предложный'] = na_stat.get('предложный', 0) + 1


        word_form = token_dict['text']




    verb_stat = Counter(verb_stat)


    print('Number of tokens:', num_tokens)
    print('Number of analysed words:', num_words)
    print_stat(pos_statistics, num_tokens, len(pos_statistics))
    print()
    x = int(input('How many verbs do you want to see?  '))
    print_stat(verb_stat, num_tokens, x)
    print('Statistics about cases:')
    for case_name in na_stat:
        print('{} : {}'.format(case_name, na_stat[case_name]))






file = open('test_final.txt', 'r', encoding='utf-8')
#authors_func(file)
#messages(file)
stemming()
