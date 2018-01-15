import time

n = 2000
#l = [1, 2, 1, 2, 3, 4, 5, 6] * n
l = [1, 2, 3, 4, 5, 5, 6, 7, 8, 9]
threshold = 2

t = time.time()

i = 0
while i < len(l):
    elt = l[i]
    num_elt = l.count(elt)

    if num_elt == threshold:
        j = i
        while j < len(l):
            if elt == l[j]:
                del l[j]
            else:
                j += 1
    else:
        i += 1

t = time.time() - t
print(t)
print(l[:30])
