'''
функцию def_e(x), находящую численное значение производной
(с точностью до 3 знака) в точке x.
'''
from math import exp
# исходная функция
def f(x):
    return exp(x)

accur = 3
def def_e(x):
    eps = 10**(-accur)
    dx0, dx1 = eps, eps / 10
    dfx0, dfx1 = (f(x + dx0) - f(x)) / dx0,  (f(x + dx1) - f(x)) / dx1
    while abs (dfx0 - dfx1) > eps:
        # print(dx0, dfx0, dx1, dfx1)
        dx0, dx1 = dx1, dx1 / 10
        dfx0, dfx1 = dfx1, (f(x + dx1) - f(x)) / dx1
    return round(dfx1, accur)

print(def_e(3))