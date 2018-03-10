import re

def comparer(s):
    i = 0
    while i <= len(s) / 2:
        if s[i] != s[-i - 1]:
            return False
        else:
            i += 1
    return True


s = 'Я не стар, брат Сеня'.lower()
s = re.sub('\W', '', s)

if comparer(s):
    print('It\'s a palindrome')
else:
    print('It\'s not a palindrome')
