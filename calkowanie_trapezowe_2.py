import numpy as np


np.set_printoptions(precision=3)


def eps(wynik_dokladny, wynik_oszacowany):
    blad = np.abs((wynik_dokladny - wynik_oszacowany) / wynik_dokladny) * 100
    return blad


def simp_int(fun, a, b, n):
    dx = (b - a) / n
    dx_vec = np.linspace(a, b, n + 1)
    fval_vec = fun(dx_vec)
    maska = np.ones_like(dx_vec) * 4
    maska[::2] = maska[::2] / 2
    maska[0] = 1
    maska[-1] = 1
    calka_wynik = dx / 3 * np.matmul(maska, fval_vec.T)
    return calka_wynik


f = lambda y: y * np.exp(-y)
a = -2
b = 10

int_f = lambda x: simp_int(f, a, b, x)

int_fex = -7.3891

print('Wynik dla 100 przedziałów całkowania: {:.4f}. Blad: {:.2}%'.format(int_f(100), eps(int_fex, int_f(100))))