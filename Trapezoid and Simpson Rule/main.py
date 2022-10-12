import numpy as np
import math


def my_function(x):
    return 1 / x


def simpson(a, b, h):
    x = np.arange(a, b + h, h)
    y = [my_function(i) for i in x]
    s = 0
    for i in range(2, len(x), 2):
        s += (2 * h) * ((1 / 6) * y[i - 2] +
                        (2 / 3) * y[i - 1] + (1 / 6) * y[i])
    return s


def trapezoid(a, b, h):
    x = np.arange(a, b + h, h)
    y = [my_function(i) for i in x]
    s = 0
    for i in range(1, len(x)):
        s += h * ((y[i] + y[i - 1]) / 2)
    return s


def conclusion(i, i_h, i_h2, h, eps):
    print(i, ') ')
    print('Ih = ', i_h)
    print('Ih2 = ', i_h2)
    print('h = ', h)
    print('eps = ', i_h - i_h2)
    print('-----------------------')


def main():
    print("a = ", end='')
    a = int(input())
    print("b = ", end='')
    b = int(input())
    print("h = ", end='')
    h = float(input())
    print('1.Eps = 0.00000001')
    print('2.Eps = 0.0000000001')
    print('Choice: ', end='')
    eps = 0.01
    choice = int(input())
    if choice == 1:
        eps = 0.00000001
    elif choice == 2:
        eps = 0.0000000001
    h2 = h
    i_h = 2
    i_h2 = 0
    i = 1
    print('Trapezoid')
    while math.fabs(i_h - i_h2) >= 3 * eps:
        i_h = trapezoid(a, b, h)
        i_h2 = trapezoid(a, b, h / 2)
        conclusion(i, i_h, i_h2, h, eps)
        h /= 2
        i += 1
    i_h = 2
    i_h2 = 0
    i = 1
    print('Simpson')
    while math.fabs(i_h - i_h2) >= 15 * eps:
        i_h = simpson(a, b, h2)
        i_h2 = simpson(a, b, h2 / 2)
        conclusion(i, i_h, i_h2, h2, eps)
        h2 /= 2
        i += 1


if __name__ == '__main__':
    main()
