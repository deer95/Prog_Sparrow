import re

def comparer(s):
    if len(s) <= 1:
        return True

    if s[0] != s[-1]:
        return False

    return comparer(s[1:-1])


s = 'Я не стар, брат Сеня'.lower()
s = re.sub('\W', '', s)

if comparer(s):
    print('It\'s a palindrome')
else:
    print('It\'s not a palindrome')
