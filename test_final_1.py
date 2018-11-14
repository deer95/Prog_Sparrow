import re

file = open('test_final.txt', 'r', encoding='utf-8')
def authors_func(file):
  authors_set = set()
  authors_num = 0
  # считаем авторов
  for line in file:
    author = re.findall('(?<=<author>/)[\w_-]+/([\w_-]+)(?=/</author>)', line)
    authors_num += len(author)
    authors_set |= set(author)
  print(authors_num)
  print(len(authors_set))

  # создаем файл и пишем туда отсортированных авторов
  file_path = input('What and where would you like to create a file?')
  authors_file = open(file_path + '.txt', 'w', encoding='utf-8')
  authors_sorted = sorted(list(authors_set))
  for i in range(len(authors_sorted)):
    authors_file.write(str(i + 1) + '. ' + authors_sorted[i] + '\n')
  authors_file.close()

  # выводим автора под нужным номером
  num_name = input('What author would you like to see?')
  while True:
    if num_name.isdigit():
      num_name = int(num_name)
      if num_name < 0 and num_name > len(authors_set):
        print('Sorry, your number is inappropriate. Try something between 0 and', len(authors_set))
        continue
      else:
        break
    else:
      print('Sorry, it is not a digit. Try to input a number.')
      continue
  print('{}. {}'.format(num_name, authors_sorted[num_name - 1]))


def messages(file):
  pass


authors_func(file)
