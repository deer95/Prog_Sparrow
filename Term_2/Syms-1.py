inp = list(input('Your symbols: '))
while inp != []:
    if len(inp) != 2 or inp[0] > inp[1]:
        print('Enter the proper data')
        inp = list(input('Your symbols: '))
        continue
    else:
        a, b = inp[0], inp[1]
        for i in range(ord(a), ord(b) + 1):
            print('{0} {1} {2}'.format(chr(i), i, hex(i)))
        inp = list(input('Your symbols: '))
