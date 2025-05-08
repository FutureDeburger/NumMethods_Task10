import math

def function(x, y):
    return y / (math.log(y) - x + 1)

def Euler_method(left_bord, right_bord, step):

    x = left_bord
    y = 1

    while x <= right_bord:
        y += step * function(x, y)
        x += step

    return x, y


if __name__ == '__main__':
    left_border = 0
    right_border = 4

    h1 = 0.01
    h2 = 0.001
    h3 = 0.0001
    h4 = 0.00001
    h5 = 0.000001

    result1 = Euler_method(left_border, right_border, h1)
    print(f'Ответ: {result1} при шаге {h1}.')

    result2 = Euler_method(left_border, right_border, h2)
    print(f'Ответ: {result2} при шаге {h2}.')

    result3 = Euler_method(left_border, right_border, h3)
    print(f'Ответ: {result3} при шаге {h3}.')

    result4 = Euler_method(left_border, right_border, h4)
    print(f'Ответ: {result4} при шаге {h4}.')

    result5 = Euler_method(left_border, right_border, h5)
    print(f'Ответ: {result5} при шаге {h5}.')