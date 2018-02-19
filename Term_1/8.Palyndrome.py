import re

def comparer(s):
    if len(s) <= 1:
        return True

    if s[0] != s[-1]:
        return False

    return comparer(s[1:-1])


s = 'Я не стар, брат Сеня'.lower()
s = re.sub('\W', '', s)

is_palindrome = comparer(s)

if is_palindrome:
    print('It\'s a palindrome')
else:
    print('It\'s not a palindrome')


'''
if s[:] == s[::-1]:
    print('It\'s a palindrome')
else:
    print('It\'s not a palindrome')
'''
