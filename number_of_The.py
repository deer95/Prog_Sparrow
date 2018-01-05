n = int(input('The number: '))
numberOfThe = 0
for i in range(n):
    if input('Word #{} = '.format(str(i + 1))).lower() == 'the':
        numberOfThe += 1
print('The number of "the" =', numberOfThe)
