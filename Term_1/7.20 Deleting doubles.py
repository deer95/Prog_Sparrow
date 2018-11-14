import time_speaker

n = 1000
l = list(range(10)) * n
new_list = []
s = set()
i = 0

t = time_speaker.time_speaker()

while i < len(l):
    if l[i] not in s:
        s.add(l[i])
        new_list.append(l[i])
    i += 1

t = time_speaker.time_speaker() - t
print(t)
print(new_list[:30])
