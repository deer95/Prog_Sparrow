import re

print('Дай папиросочку, у тебя брюки в полосочку.')

in_file = open('12_txt/12.3-input.txt', 'r', encoding='utf-8')
out_file = open('12_txt/12.3-output.txt', 'w', encoding='utf-8')

for line in in_file:
    if '@' in line:
        new_line = re.sub('[^\w\s@]', '', line).split()
        new_line.reverse()
        line_first = ' '.join(new_line)
        out_file.write(line_first + '\n')
        
        new_line.sort()
        line_second = ' '.join(new_line)
        out_file.write(line_second + '\n')
