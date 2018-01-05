import time

t = time.time()

n = 1000
l = list(range(10)) * n
#l = [int(y) for y in '12345678912734756']
x = 7
i = 0
num_x = 0

while i + num_x < len(l):
    if l[i + num_x] == x:
        num_x += 1
    else:
        l[i] = l[i + num_x]
        i += 1

l[-num_x:] = []

t = time.time() - t

print(l[:30])
print(t)
