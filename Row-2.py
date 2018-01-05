'''
Даны два целых числа A и В.
Выведите все числа от A до B включительно,
в порядке возрастания, если A < B,
или в порядке убывания в противном случае.
'''
a = int(input('A = '))
b = int(input('B = '))
step = 1 if a < b else -1
for i in range(a, b + step, step):
    print(i, end=' ')
