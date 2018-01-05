n = int(input('The number = '))
ceiling = 10 ** n - 1
floor = 10 ** (n - 1) - 1
print('Нечетные числа: ', end='')
for i in range(ceiling, floor, -2):
    print(i, end=' ')
