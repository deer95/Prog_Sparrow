import random

file = open('country_capital_text.txt', 'r', encoding = 'utf-8')
coun_cap_dict = {}

'''ЗАГРУЖЕЕМ ДАННЫЕ'''
def load_data():
    for line in file:
        country, capital = line.split(':')
        capital = capital.strip()
        coun_cap_dict[capital] = country
    return(coun_cap_dict)


'''ИГРАЕМ В ИГРУ'''
def play_game(coun_cap_dict):

    score = 0

    '''ВВОД И ПРОВЕРКА ДАННЫХ'''
    rounds = input('Enter number of rounds: ')              # проверяем количество раундов на верность

    while True:
        if rounds.isdigit():
            rounds = int(rounds)
            if rounds > 233:
                print('Sorry, your number is too big. Type something less than 233.')
                rounds = input('Enter number of rounds: ')
            else:
                break
        else:
            print('Sorry, I accept only integers. Type once more.')
            rounds = input('Enter number of rounds: ')

    variants_int = input('Enter number of variants: ')          # проверяем количество вариантов на верность
    while True:
        if variants_int.isdigit():
            variants_int = int(variants_int)
            if variants_int > 10:
                print('Sorry, your number is too big. Type something less than 10.')
                variants_int = input('Enter number of rounds: ')
            else:
                break
        else:
            print('Sorry, I accept only integers. Type once more.')
            variants_int = input('Enter number of rounds: ')
        variants_int -= 1

    '''ИГРА'''
    for i in range(rounds):
        capital, country = random.choice(list(coun_cap_dict.items()))
        variants = []
        for j in range(variants_int):                       # создаем неправильные варианты ответов
            variants.append(random.choice(list(coun_cap_dict)))
        position_of_correct = random.randint(0, variants_int)       # выбираем позицию правильного ответа и кладем его туда
        variants.insert(position_of_correct, capital)

        print('There is a country named {}. What is its capital? Type the correct number.'.format(country))
        for k in range(len(variants)):
            print('{}. {}'.format(k, variants[k]))
        answer = input('The number of {} capital is: '.format(country))

        while True:                                                 # проверяем, все ли хорошо с типом ответа
            if answer.isdigit():
                answer = int(answer)
                if answer > variants_int:
                    print('Sorry, your number is too big. Type something less than {}.'.format(variants_int))
                    answer = input('The number of {} capital is: '.format(country))
                else:
                    break
            else:
                print('Sorry, I accept only integers. Type once more.')
                answer = input('The number of {} capital is: '.format(country))

        '''ОЧКИ'''
        if answer == position_of_correct:                           # проверяем правильность ответа
            print("Congratulations! You are correct. Let's see the next one.")
            score += 1
        else:
            print("Sorry, you are wrong. The capital of {} is {}.".format(country, capital))
        print()
    return score

score = play_game(load_data())
print('The game is over.\nYou finished it with the score: {}.'.format(score))
