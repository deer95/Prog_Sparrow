import random

'''ЗАГРУЖАЕМ ДАННЫЕ'''
def load_data():
    file = open('country_capital_text.txt', 'r', encoding = 'utf-8')
    coun_cap_dict = {}
    for line in file:
        country, capital = line.split(':')
        capital = capital.strip()
        coun_cap_dict[capital] = country
    file.close()
    return(coun_cap_dict)


'''ИГРАЕМ В ИГРУ'''
def play_game(coun_cap_dict):

    score = 0

    '''ВВОД И ПРОВЕРКА ДАННЫХ'''
    rounds = input('Enter number of rounds: ')              # проверяем количество раундов на верность

    while True:
        if rounds.isdigit():
            rounds = int(rounds)
            if rounds > 233 or rounds <= 0:
                print('Sorry, your number is incorrect. Type something between 233 and 0.')
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
            if variants_int > 10 or rounds <= 0:
                print('Sorry, your number is too big. Type something between 10 and 0.')
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
    print('The game is over.\nYou finished it with the score: {}.'.format(score))


def process():
    go_on = True
    coun_cap_dict = load_data()
    print('For playing type "play".\nFor list of countries type "list".\nFor exit type "exit".')
    reply = input('Type something: ').lower()
    if reply == 'play':
        play_game(coun_cap_dict)

    elif reply == 'list':
        for capital in coun_cap_dict:
            print('The capital of {} is {}.'.format(coun_cap_dict[capital], capital))

    elif reply == 'exit':
        print('Thank you for working! Bye')
        go_on = False

    else:
        item_list = coun_cap_dict.items()
        coun_dict = {}
        for pair in item_list:
            coun_dict[pair[1].lower()] = pair[0].lower()
        if reply in coun_dict.keys():
            print('The capital of {} is {}.'.format(reply.capitalize(), coun_dict[reply].capitalize()))
        else:
            print('Sorry, there is no "{}" in my list.'.format(reply))
    print()

    return go_on

go_on = True
while go_on:
    go_on = process()

