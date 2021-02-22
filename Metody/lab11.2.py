import numpy as np



def eps(wynik_dokladny, wynik_oszacowany):
    blad = np.abs((wynik_dokladny - wynik_oszacowany) / wynik_dokladny) * 100
    return blad


err = lambda x, x_old: np.abs((x - x_old) / (x)) * 100


def trapezy(fun, a, b, n):
    dx = (b - a) / n
    dx_vec = np.linspace(a, b, n + 1)
    fval_vec = fun(dx_vec)
    maska = np.ones_like(dx_vec) * 2
    maska[0] = 1
    maska[-1] = 1
    calka_wynik = dx / 2 * np.matmul(fval_vec, maska.T)
    return calka_wynik


f = lambda x: np.power(2 * x + (3 / x), 2)
int_f = lambda x: trapezy(f, 1, 2, x)

i = 0
int_fi = 0
int_fi_old = 0
for i in range(1, 100):
    int_fi = int_f(i)
    print('Podprzedzialy {}: Wartosc calki: {:.5f}. Blad: {:.2f}%'.format(i, int_fi, err(int_fi, int_fi_old)))
    if (err(int_fi, int_fi_old) < 0.82):
        break
    int_fi_old = int_fi

I = 4/3 * int_fi - 1/3 * int_fi_old
print('Wartość skorygowanej całki wynosi: {:.6f}'.format(I))