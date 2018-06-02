import random


def enter_data():
    '''ASKING USER TO ENTER DATA'''
    # enter square
    while True:
        try:
            length, height = [int(i) for i in input('Enter the size in format like "100 100": ').split()]
            if min(length, height) > 0:
                break
            else:
                print('Your numbers are too little. Try something more than 0.')
        except ValueError:
            print('Sorry, I don\'t understand. Try to enter once more.')

    square = length * height
    print('You made a field with square {}.'.format(square))

    # enter number of cells
    while True:
        num_cells = input('Enter the number of alive cells: ')
        if not num_cells.isdigit():
            print('Sorry, enter a digit.')
        else:
            num_cells = int(num_cells)
            if num_cells > square or num_cells < 0:
                print('Sorry, the number is inappropriate. Try something between 0 and {}.'.format(square))
            else:
                break
    return (length, height, num_cells)


def generate_cells(tuple):
    '''ESTABLISHING THE POSITION OF ALIVE CELLS'''
    length, height, num_cells = tuple
    cells_set = set()
    for i in range(num_cells):
        row = random.randint(0, height - 1)
        column = random.randint(0, length - 1)
        coordinate = (row, column)
        while coordinate in cells_set:
            row = random.randint(0, height - 1)
            column = random.randint(0, length - 1)
            coordinate = (row, column)
        cells_set.add(coordinate)
    return (cells_set, length, height)


def print_field(tuple):
    '''PRINTING THE FINAL FIELD'''
    # making upper borders
    alive_cells, length, height = tuple
    print('┌', end='')
    for i in range(length):
        print('-', end='')
    print('┐')

    # printing the field
    for i in range(height):
        print('│', end='')
        for j in range(length):
            if (i, j) in alive_cells:
                print('+', end='')
            else:
                print(' ', end='')
        print('│')

    # making lower borders
    print('└', end='')
    for i in range(length):
        print('-', end='')
    print('┘')


while input('Finish?') == '':
    print_field(generate_cells(enter_data()))
