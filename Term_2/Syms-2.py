s = input('Your string: ')
eng = [list('ABCDEFGHIJKLMNOPQRSTUVWZYZ'), list('abcdefghijklmopqrstuvwxyz')]
rus = [list('АБВГДЕЁЖЗИКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'), list('абвгдеёжзиклмнопрстуфхцчшщъыьэюя')]
while s != '':
    for sym in s:
        if sym in eng[0]:
            print(eng[1][eng[0].index(sym)], end='')

        elif sym in rus[1]:
            print(rus[0][rus[1].index(sym)], end='')

        else:
            print(sym, end='')
    s = input('\nYour string: ')
