import re

def comparer(s, i):
    is_palindrome = False
    while i <= len_s // 2:
        if s[i] == s[len_s - i - 1]:
            i += 1
            is_palindrome = True
            comparer(s, i)
        else:
            break
    return is_palindrome


s = 'Я не стар, брат Сеня'.lower()
s = re.sub('\W', '', s)
i = 0
len_s = len(s)

if comparer(s, i) == True:
    print('It\'s a palindrome')
else:
    print('It\'s not a palindrome')


'''
if s[:] == s[::-1]:
    print('It\'s a palindrome')
else:
    print('It\'s not a palindrome')
'''
