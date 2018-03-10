print('Hello, Ilon Mask')

in_file = open('12_txt/12.2-input.txt', 'r', encoding='utf-8')
out_file = open('12_txt/12.2-output.txt', 'w', encoding='utf-8')

for line in in_file:
    new_line = line.split()
    new_line.reverse()
    new_line = ' '.join(new_line)
    out_file.write(new_line + '\n')
