def power(x, n):
    powered_x = x ** n
    return  powered_x


a = 3
b = 4
x = 4.556
y = 0.845

leg_X = a - x
leg_Y = b - y
hypotenuse = power(power(leg_X, 2) + power(leg_Y, 2), 0.5)

print(hypotenuse)


'''
def quadrator(x):
    x *= x
    return x


def sqrt(x):
    y = 0
    tenth = 0.1
    while quadrator(y + 1) < x:
        y += 1
    if quadrator(y) != x:
        for i in range(15):
            while quadrator(y + tenth) < x:
                y += tenth
            tenth *= 0.1
    return y

'''
