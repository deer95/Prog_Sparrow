while True:
    number = input('Number of cows = ')
    lastSym = int(number[-2:])
    if 10 < lastSym < 20 or (lastSym % 10) in [0, 5, 6, 7, 8, 9]:
        print(number + ' коров')
    elif lastSym % 10 == 1:
        print(number + ' корова')
    else:
        print(number + ' коровы')
