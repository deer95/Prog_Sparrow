n = int(input('Number of cards = '))
summ = 0
for i in range(n + 1):
    summ += i
for j in range(n - 1):
    numCard = int(input('The card number = '))
    summ -= numCard
print('The lost card is', summ)
