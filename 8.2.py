def absolute(x):
    if x < 0:
        x = -x
    return x


def power(a, n):
    while n > 0:
        if absolute(n) == 1:
            pass
        if n < 0:
            a *= 1 / power(a, absolute(n))
        else:
            a *= power(a, n)
        n = absolute(n) - 1
    return a

#a = float(input())
#n = int(input())
a = 8
n = 3
print(power(a, n))
