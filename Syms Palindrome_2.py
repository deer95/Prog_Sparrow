text = 'А роза упала на лапу Азора'.lower().replace(' ', '')
print('It\'s a palindrome') if text[:] == text[::-1] else print('It\'s a kinda fake')
