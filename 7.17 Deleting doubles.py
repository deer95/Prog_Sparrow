import time

l = []
i1 = 1000
N = i1
for i in zip (range (0, 20 * N, 2), list (range (1, 20, 2)) * N):
    l.extend (i)

t = time.time()

i = 0
while i < len(l):
    num_elt = l.count(l[i])
    j = i + 1
    while num_elt != 1:
        if l[i] == l[j]:
            del l[j]
            num_elt -= 1
        j += 1
    i += 1

t = time.time() - t
print(t)
print(l[:30])
