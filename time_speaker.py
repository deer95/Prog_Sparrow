import time
import random

def number2string(n, tens_ends, ones_ends, sg_root):
    result = []
    deca = n // 10
    uno = n % 10
    # for numbers > 19
    if deca > 1:
        result.append(tens[deca] + tens_ends[deca])
        if uno:
            result.append(ones_main[uno] + ones_ends[uno])
    # for numbers 9 < x < 20
    elif deca == 1 and uno != 0:
        result.append(teens[uno] + ones_ends[9])
    # for numbers < 10 - use the root for singulars
    elif deca <= 10:
        result.append(sg_root[uno] + ones_ends[uno])
    # if everything is zero
    elif deca == uno == 0:
        result.append(tens[deca] + tens_ends[deca])
    return ' '.join(result)


def even_time(hour, minute):
    if minute == 30:
        if hour == 12:
            hour = 0
        tens_ends = ['', 'и', 'и', 'и', 'а', 'и']
        ones_ends = ['ого', 'ого', 'ого', 'ьего', 'ого', 'и', 'и', 'и', 'ьми', 'и']
        h_str = number2string(hour + 1, tens_ends, ones_ends, ones_ordinal)
        return 'чертова половина {}'.format(h_str)
    else:
        tens_ends = ['', 'ь', 'ь']
        ones_ends = ['ь', '', 'а', 'и', 'е', 'ь', 'ь', 'ь', 'емь', 'ь']
        h_list = number2string(hour, tens_ends, ones_ends, ones_hour)

        if (hour % 10) == 1 and (hour // 10) != 1:
            scale = ''
        elif 1 < (hour % 10) < 5 and (hour // 10) != 1:
            scale = 'часа'
        else:
            scale = 'часов'
        return 'ровно {} {}'.format(h_list, scale)


def left_time(hour, minute):
    time_diff = 60 - minute
    if hour == 12:
            hour = 0
    h_tens_ends = ['', 'ь', 'ь']
    h_ones_ends = ['ь', '', 'а', 'и', 'е', 'ь', 'ь', 'ь', 'емь', 'ь']
    h_str = number2string(hour + 1, h_tens_ends, h_ones_ends, ones_hour)

    if minute in (40, 45, 50):
        m_tens_ends = ['', 'и', 'и', 'и', 'а', 'и', 'и']
        m_ones_ends = ['и', 'и', 'и', 'и', 'и', 'и', 'и', 'и', 'ьми', 'и']
        m_str = number2string(time_diff, m_tens_ends, m_ones_ends, ones_main)
    else:
        m_ones_ends = ['и', 'ной', 'ух', 'ех', 'ех', 'и', 'и', 'и', 'ьми', 'и']
        m_str = ' '.join([number2string(time_diff, [], m_ones_ends, ones_main), 'минут'])

    return 'без {} {}'.format(m_str, h_str)


def passed_time(hour, minute):
    if hour == 12:
            hour = 0
    h_tens_ends = ['', 'ь', 'ь']
    h_ones_ends = ['ого', 'ого', 'ого', 'ьего', 'ого', 'ого', 'ого', 'ого', 'ого', 'ого']
    h_str = number2string(hour + 1, h_tens_ends, h_ones_ends, ones_ordinal)

    m_tens_ends = ['', 'ь', 'ь', '', '', '', '']
    m_ones_ends = ['', 'на', 'е', 'и', 'е', 'ь', 'ь', 'ь', 'емь', 'ь']
    m_str = number2string(minute, m_tens_ends, m_ones_ends, ones_main)

    if (minute % 10) == 1 and (minute // 10) != 1:
        scale = 'минута'
    elif 1 < (minute % 10) < 5 and (minute // 10) != 1:
        scale = 'минуты'
    else:
        scale = 'минут'

    return '{} {} {}'.format(m_str, scale, h_str)


def concrete_time(hour, minute):
    h_tens_ends = ['', 'ь', 'ь']
    h_ones_ends = ['ь', '', 'а', 'и', 'е', 'ь', 'ь', 'ь', 'емь', 'ь']
    h_str = number2string(hour, h_tens_ends, h_ones_ends, ones_hour)

    m_tens_ends = ['', 'ь', 'ь', 'ь', '', '', '']
    m_ones_ends = ['ь', 'на', 'е', 'и', 'е', 'ь', 'ь', 'ь', 'емь', 'ь']
    m_str = number2string(minute, m_tens_ends, m_ones_ends, ones_main)

    if (hour % 10) == 1 and (hour // 10) != 1:
        h_scale = ''
    elif 1 < (hour % 10) < 5 and (hour // 10) != 1:
        h_scale = 'часа'
    else:
        h_scale = 'часов'

    if (minute % 10) == 1 and (minute // 10) != 1:
        m_scale = 'минута'
    elif 1 < (minute % 10) < 5 and (minute // 10) != 1:
        m_scale = 'минуты'
    else:
        m_scale = 'минут'

    return '{} {} {} {}'.format(h_str, h_scale, m_str, m_scale)


tens = ['ноль', 'десят', 'двадцат', 'тридцат', 'сорок', 'пятьдесят']
ones_main = ['десят', 'од', 'дв', 'тр', 'четыр', 'пят', 'шест', 'сем', 'вос', 'девят']
ones_hour = ['десят', 'час', 'дв', 'тр', 'четыр', 'пят', 'шест', 'сем', 'восем', 'девят']
ones_ordinal = ['десят', 'перв', 'втор', 'трет', 'четверт', 'пят', 'шест', 'седьм', 'восьм', 'девят']
teens = ['десят', 'одиннадцат', 'двенадцат', 'тринадцат', 'четырнадцат',
         'пятнадцат', 'шестнадцат', 'семнадцат', 'восемнадцат', 'девянадцат']
hour, minute = [int(i) for i in time.strftime('%I.%M').split('.')]
#hour, minute = random.randint(1, 12), random.randint(0, 59)
#hour, minute = 1, 0
print('Current time: {:0>2}:{:0>2}'.format(hour, minute))

if minute in (0, 30):
    print(even_time(hour, minute))
elif minute in (40, 45, 50) or minute > 50:
    print(left_time(hour, minute))
elif minute < 30:
    print(passed_time(hour, minute))
elif minute > 30:
    print(concrete_time(hour, minute))
