n = int(input('Your number = '))
is_summable = False

first_range = min(n, 9)
for i in range(1, first_range + 1):
    num1 = i
    for j in range(min(n - num1, 9) + 1):
        num2 = j
        num3 = n - num1 - num2
        if num3 < 10:
            number = str(num1) + str(num2) + str(num3)
            print(number)
            is_summable = True

if is_summable is False:
    print('Sorry, there is no numbers on your request')

