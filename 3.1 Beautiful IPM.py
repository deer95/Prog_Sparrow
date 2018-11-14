import pymystem3
import re

def count_ipm(text):
    num_words = 0
    pos_statistics = {}

    # анализируем текст и считаем количество токенов
    stemmer = pymystem3.Mystem(entire_input=False)
    token_list = stemmer.analyze(text, speedup=True)

    # считаем абс. частоту для прилагательных, глаголов, существительных, предлогов
    for i in range(len(token_list)):
        token_dict = token_list[i]
        lemma_list = token_dict['analysis']
        num_words += 1
        if lemma_list:
            lexeme_dict = lemma_list[0]
            gr_description = lexeme_dict['gr']
            pos = re.match('\w+', gr_description)
            if pos:
                pos = pos.group()
                pos_statistics[pos] = pos_statistics.get(pos, 0) + 1
    # считаем ipm и проценты
    for gen_pos in pos_statistics:
        abs_stat = pos_statistics[gen_pos]
        ipm_stat = round(pos_statistics[gen_pos] * 1000000 / num_words, 1)
        perc_stat = round(pos_statistics[gen_pos] / num_words * 100, 2)
        print('{:<6} IPM: {:>8} absolute: {:<5} percent: {:>5}%'.format(gen_pos, ipm_stat, abs_stat, perc_stat))


file = open('caesar_teacher.txt', 'r', encoding='utf-8')
count_ipm(file.read())
file.close()
