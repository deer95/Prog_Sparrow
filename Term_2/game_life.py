import random
import os
import time


def enter_data():
    '''ASKING USER TO ENTER DATA'''
    # enter square
    global length, height
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
    return num_cells


def generate_cells(num_cells):
    '''ESTABLISHING THE POSITION OF ALIVE CELLS'''
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
    return cells_set


def find_neighbours(row, column):
    '''FIND NEIGHBOURS FOR A CELL'''
    cell_neighbours = set()
    diff_row,  diff_column = -1, -1
    while diff_row <= 1:
        while diff_column <= 1:
            new_row = row + diff_row
            new_column = column + diff_column

            # excluding the cell itself
            if new_row == row and new_column == column:
                diff_column += 1
                continue

            # checking the borders
            if max(new_row, new_column) < 0 or new_row >= height or new_column >= length:
                diff_column += 1
                continue

            bour = (new_row, new_column)
            cell_neighbours.add(bour)

            diff_column += 1
        diff_row += 1
        diff_column = -1
    return cell_neighbours


def produce_total_neighbours(cells_set):
    '''MAKING A SET OF ALL CELLS THAT CAN CHANGE'''
    neighbours = set()
    for row, column in cells_set:
        # find all possible neighbours
        cell_neighbours = find_neighbours(row, column)
        neighbours |= cell_neighbours
    return neighbours


def animate(alive_cells, neighbours):
    '''BREATHING LIFE'''
    animated_set = set()
    for cell in neighbours:
        cell_neighbours = find_neighbours(cell[0], cell[1])
        if len(alive_cells & cell_neighbours) == 3:
            animated_set.add(cell)
    return animated_set


def kill(alive_cells):
    '''KILLING INNOCENT'''
    dead_set = set()
    for cell in alive_cells:
        cell_neighbours = find_neighbours(cell[0], cell[1])
        if len(alive_cells & cell_neighbours) > 3 or len(alive_cells & cell_neighbours) < 2:
            dead_set.add(cell)
    return dead_set


def changing_field(alive_cells, neighbours):
    '''PERFORMING THE LIFE PROCESS'''
    animated_set = animate(alive_cells, neighbours)
    new_cells_set = alive_cells | animated_set
    dead_set = kill(cells_set)
    # continue if there are changes, break if not
    if animated_set or dead_set:
        new_cells_set -= dead_set
        return new_cells_set
    else:
        return False



def print_field(alive_cells):
    '''PRINTING THE FINAL FIELD'''
    # making upper borders
    print('┌', end='')
    for i in range(length + 2):
        print('-', end='')
    print('┐')

    # printing the field
    for i in range(height):
        print('│ ', end='')
        for j in range(length):
            if (i, j) in alive_cells:
                print('+', end='')
            else:
                print(' ', end='')
        print(' │')

    # making lower borders
    print('└', end='')
    for i in range(length + 2):
        print('-', end='')
    print('┘')


length, height = 0, 0

cells_set = generate_cells(enter_data())
print_field(cells_set)
while cells_set:
    total_neighbours = produce_total_neighbours(cells_set)
    new_cells_set = changing_field(cells_set, total_neighbours)
    if new_cells_set == cells_set:
        break
    else:
        cells_set = new_cells_set
        time.sleep(0.5)
        print("\n" * 5)
        #os.system('cls')
        print_field(cells_set)

print('THE GAME IS OVER. LONG LIVE THE LIFE!')
