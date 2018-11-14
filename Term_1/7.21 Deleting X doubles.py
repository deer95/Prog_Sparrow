import time_speaker

n = 4000
l = [1, 2, 1, 2, 3, 4, 5, 6] * n
new_list = []
d = {}
threshold = 4

t = time_speaker.time_speaker()

for elt in l:
    if elt in d:
        if d[elt] < threshold:
            d[elt] += 1
            new_list.append(elt)
    if elt not in d:
        d[elt] = 1
        new_list.append(elt)

t = time_speaker.time_speaker() - t
print(t)
print(new_list)
