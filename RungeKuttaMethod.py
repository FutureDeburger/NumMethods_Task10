
def function(x, y):
    return x * y * (x * x * y + 2)

def Runge_Kutta_method(left_bord, right_bord, step):

    x = left_bord
    y = 10/3

    k0, k1, k2, k3 = 0, 0, 0, 0
    while x <= right_bord:
        k0 = function(x, y)
        k1 = function(x + step / 2, y + (step * k0 / 2))
        k2 = function(x + step / 2, y + (step * k1 / 2))
        k3 = function(x + step, y + step * k2)
        y = y + (step / 6) * (k0 + 2 * k1 + 2 * k2 + k3)
        x += step

    res_y = y + (step / 6) * (k0 + 2 * k1 + 2 * k2 + k3)
    return x, res_y

if __name__ == '__main__':
    left_border = 0
    right_border = 0.9

    h1 = 0.01
    h2 = 0.001
    h3 = 0.0001
    h4 = 0.00001
    h5 = 0.000001
    h6 = 1e-7
    h7 = 1e-8

    result1 = Runge_Kutta_method(left_border, right_border, h1)
    print(f'Ответ: {result1} при шаге {h1}.')

    result2 = Runge_Kutta_method(left_border, right_border, h2)
    print(f'Ответ: {result2} при шаге {h2}.')

    result3 = Runge_Kutta_method(left_border, right_border, h3)
    print(f'Ответ: {result3} при шаге {h3}.')

    result4 = Runge_Kutta_method(left_border, right_border, h4)
    print(f'Ответ: {result4} при шаге {h4}.')

    result5 = Runge_Kutta_method(left_border, right_border, h3)
    print(f'Ответ: {result5} при шаге {h5}.')

    result6 = Runge_Kutta_method(left_border, right_border, h6)
    print(f'Ответ: {result6} при шаге {h6}.')

    result7 = Runge_Kutta_method(left_border, right_border, h7)
    print(f'Ответ: {result7} при шаге {h7}.')