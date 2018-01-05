n = int(input('Your number = '))
is_summable = False
for i in range(1, n + 1):
    num1 = i
    for j in range(n - num1 + 1):
        num2 = j
        num3 = n - num1 - num2
        number = str(num1) + str(num2) + str(num3)
        if int(number) < 1000:
            print(number)
            is_summable = True
    if is_summable is False:
        print('Sorry, there is no numbers on your request')
        break
