import time

n = 2000
l = [1, 2, 1, 2, 3, 4, 5, 6] * n
threshold = n

t = time.time()

i = 0
while i < len(l):
    elt = l[i]
    num_elt = l.count(elt)


    j = i + 1
    while num_elt == threshold:
        if elt == l[j]:
            del l[j]
            num_elt -= 1
        else:
            j += 1

'''
    if num_elt == threshold:
        for j in range(num_elt):
            l.remove(elt)
    else:
        i += 1
'''

t = time.time() - t
print(t)
print(l[:30])
