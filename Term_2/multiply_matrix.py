def formula(a, b):
    return a ** b

def generate_matrix(rows, columns, formula):
    matrix = []
    for i in range(rows):
        row = [formula(i, j) for j in range(columns)]
        matrix.append(row)
    return matrix

def multiply_ab(matrix_a, matrix_b):
    matrix = []
    columns = [[] * k for k in range(len(matrix_a))]
    for m in range(len(matrix_b)):
        for n in range(len(columns)):
            columns[n].append(matrix_b[n][m])

    for i in range(len(matrix_a)):
        row = matrix_a[i]
        matrix.append([])
        for j in range(len(columns)):
            column = columns[j]
            matrix[i].append(0)
            s = sum([row[q] * column[q] for q in range(len(row))])
            matrix[i][j] = sum([row[q] * column[q] for q in range(len(row))])
    return matrix


file = open('multiply_matrix_txt.txt', 'r', encoding = 'utf-8')
rows_a = int(file.readline())
matrix_a = []

for i in range(rows_a):
    matrix_a.append([int(j) for j in file.readline().split()])
columns_b = int(file.readline())
file.close()

matrix_b = generate_matrix(rows_a, columns_b, formula)
matrix_c = multiply_ab(matrix_a, matrix_b)

for row1 in matrix_b:
    print(row1)
print()

for row2 in matrix_c:
    print(row2)
