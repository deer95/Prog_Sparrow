def uncoder(n):
    i = 0
    for line in cipher:
        uncoded_list.append('')
        for sym in line:
            new_sym = chr(ord(sym) - n)
            uncoded_list[i] += new_sym
        i += 1


cipher = open('cipher.txt', 'r', encoding='utf-8')
uncoded_list = []
uncoded_dict = {}
n = 1
ok = False

while ok == False:
    for line in uncoded_list:
        string = line.split()
        for 
