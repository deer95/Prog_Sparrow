import sys

ind = 0
ind_max = 0
maximum = -sys.maxsize  # None
while True:
    n = int(input('Your number: '))
    if n == 0:
        break

    if n > maximum:
        maximum = n
        ind_max = ind
    ind += 1
print('Index of maximum =', ind_max)


'''
ind = 0
ind_max = 0
maximum = 0
while True:
    n = int(input())
    if n == 0:
        break
    if n > maximum and ind > -1:
        maximum = n
        ind_max = ind
    elif ind == 0:
        maximum = n
    ind += 1
print(ind_max)
'''
