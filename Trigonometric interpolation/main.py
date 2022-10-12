from matplotlib import pyplot as plt
import numpy as np
import cmath


def my_function(x):
    return cmath.sqrt(x)


def get_a(y, n, j):
    i = complex(0, 1)
    s = complex(0, 0)
    for k in range(0, n):
        s += y[k] * cmath.exp(-2 * cmath.pi * i * (k * j) / n)
    return s


def get_y(x, y, fx, n, h):
    s = complex(0, 0)
    i = complex(0, 1)
    j = (-n) // 2 + 1
    for k in range(0, n):
        s += get_a(y, n, j) * cmath.exp(2 * cmath.pi *
                                        i * j * (fx - x[0]) / (n * h))
        j += 1
    s /= n
    return s


def main():
    start_point = 1
    x = []
    y = []
    print("n: ", end='')
    n = int(input())
    print("h: ", end='')
    h = float(input())
    for i in range(0, n):
        x.insert(i, start_point)
        y.insert(i, my_function(x[i]))
        start_point += h

    trig_x = np.linspace(0, n * 2 * h, 500, dtype='double')
    trig_y = [get_y(x, y, i, n, h) for i in trig_x]
    real_y = [i.real for i in trig_y]
    imag_y = [i.imag for i in trig_y]
    simple_x = np.linspace(0, n * 2 * h, 500, dtype='double')
    simple_y = [my_function(i) for i in simple_x]
    ax = plt.gca()
    ax.set_title('Тригонометрическая интерполяция')
    ax.plot(trig_x, real_y, color='blue', label='Re')
    ax.plot(trig_x, imag_y, color='orange', label='Im')
    ax.plot(simple_x, simple_y, color='red', label='F(x)')
    ax.scatter(x, y, color='black')
    plt.legend()
    ax.axes.get_xaxis().set_ticks([])
    ax.axes.get_yaxis().set_ticks([])
    plt.show()


if __name__ == '__main__':
    main()
