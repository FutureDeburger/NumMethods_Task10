import math

def function(x, y):
    return y / (math.log(y) - x + 1)

def Euler_method(left_border, right_border, step):

    x = left_border
    y = 1

    while x <= right_border:
        y += step * function(x, y)
        x += step

    return x, y


if __name__ == '__main__':

    h = 0.0001

    a = 0
    b = 4

    result = Euler_method(a, b, h)

    print(f'Ответ: {result}')