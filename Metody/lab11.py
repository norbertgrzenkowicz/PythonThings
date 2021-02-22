import numpy as np

Saa = 16.56

def calka_prostokat_lewa(fun, a, b, n):
    dx = (b-a)/n
    dx_vec = np.linspace(a, b-dx, n)
    fval_vec = fun(dx_vec)
    calka_wynik = np.sum(dx * fval_vec)
    return calka_wynik

def eps(wynik_dokladny, wynik_oszacowany):
    blad = np.abs((wynik_dokladny - wynik_oszacowany)/wynik_dokladny) * 100
    return blad

funkcja = lambda x : 8+4*np.cos(x)

Sab10 = calka_prostokat_lewa(funkcja, 0, 1.57, 10)
Sab20 = calka_prostokat_lewa(funkcja, 0, 1.57, 38)
Sab100 = calka_prostokat_lewa(funkcja, 0, 1.57, 100)
print('Wynik dla 10 przediałów całkowania: {:.4f}'.format(Sab10))
print('Wynik dla 38 przediałów całkowania: {:.4f}'.format(Sab20))
print('Wynik dla 100 przediałów całkowania: {:.4f}'.format(Sab100))

print('\n')
Eab10 = eps(Saa, Sab10)
Eab20 = eps(Saa, Sab20)
Eab100 = eps(Saa, Sab100)
print('Błąd procentowy dla 10 przediałów całkowania: {:.2f} %'.format(Eab10))
print('Błąd procentowy dla 38 przediałów całkowania: {:.2f} %'.format(Eab20))
print('Błąd procentowy dla 100 przediałów całkowania: {:.4f} %'.format(Eab100))

print("\n\n\nPrawostronna suma Riemanna")

def calka_prostokat_prawa(fun, a, b, n):
    dx = (b-a)/n
    dx_vec = np.linspace(a+dx, b, n)
    fval_vec = fun(dx_vec)
    calka_wynik = np.sum(dx * fval_vec)
    return calka_wynik

Sac10 = calka_prostokat_prawa(funkcja, 0, 1.57, 10)
Sac20 = calka_prostokat_prawa(funkcja, 0, 1.57, 38)
Sac100 = calka_prostokat_prawa(funkcja, 0, 1.57, 100)
print('Wynik dla 10 przediałów całkowania: {:.4f}'.format(Sac10))
print('Wynik dla 38 przediałów całkowania: {:.4f}'.format(Sac20))
print('Wynik dla 100 przediałów całkowania: {:.4f}'.format(Sac100))
print('\n')
Eac10 = eps(Saa, Sac10)
Eac20 = eps(Saa, Sac20)
Eac100 = eps(Saa, Sac100)
print('Błąd procentowy dla 10 przediałów całkowania: {:.2f} %'.format(Eac10))
print('Błąd procentowy dla 38 przediałów całkowania: {:.2f} %'.format(Eac20))
print('Błąd procentowy dla 100 przediałów całkowania: {:.4f} %'.format(Eac100))

print("\n\n\npunkt srodkowy")
def calka_prostokat_srodek(fun, a, b, n):
    dx = (b-a)/n
    dx_vec = np.linspace(a+dx, b, n)-(dx/2)
    fval_vec = fun(dx_vec)
    calka_wynik = np.sum(dx * fval_vec)
    return calka_wynik

Sad10 = calka_prostokat_srodek(funkcja, 0, 1.57, 10)
Sad20 = calka_prostokat_srodek(funkcja, 0, 1.57, 38)
Sad100 = calka_prostokat_srodek(funkcja, 0, 1.57, 100)
print('Wynik dla 10 przediałów całkowania: {:.4f}'.format(Sad10))
print('Wynik dla 38 przediałów całkowania: {:.4f}'.format(Sad20))
print('Wynik dla 100 przediałów całkowania: {:.4f}'.format(Sad100))

print('\n')
Ead10 = eps(Saa, Sad10)
Ead20 = eps(Saa, Sad20)
Ead100 = eps(Saa, Sad100)
print('Błąd procentowy dla 10 przediałów całkowania: {:.2f} %'.format(Ead10))
print('Błąd procentowy dla 38 przediałów całkowania: {:.2f} %'.format(Ead20))
print('Błąd procentowy dla 100 przediałów całkowania: {:.4f} %'.format(Ead100))

print("\n\n\ntrapezy")
def calka_trapezy(fun, a, b, n):
    dx = (b-a)/n
    dx_vec = np.linspace(a, b, n+1)
    fval_vec = fun(dx_vec)
    maska = np.ones_like(dx_vec)*2
    maska[0] = 1
    maska[-1] = 1
    calka_wynik = dx/2 * np.matmul(fval_vec, maska.T)
    return calka_wynik

Sae10 = calka_trapezy(funkcja, 0, 1.57, 10)
Sae20 = calka_trapezy(funkcja, 0, 1.57, 38)
Sae100 = calka_trapezy(funkcja, 0, 1.57, 100)
print('Wynik dla 10 przediałów całkowania: {:.4f}'.format(Sae10))
print('Wynik dla 38 przediałów całkowania: {:.4f}'.format(Sae20))
print('Wynik dla 100 przediałów całkowania: {:.4f}'.format(Sae100))


Eae10 = eps(Saa, Sae10)
Eae20 = eps(Saa, Sae20)
Eae100 = eps(Saa, Sae100)
print('Błąd procentowy dla 10 przediałów całkowania: {:.2f} %'.format(Eae10))
print('Błąd procentowy dla 38 przediałów całkowania: {:.2f} %'.format(Eae20))
print('Błąd procentowy dla 100 przediałów całkowania: {:.4f} %'.format(Eae100))

print("\n\n\nsimpson")
def calka_simpson(fun, a, b, n):
    dx = (b-a)/n
    dx_vec = np.linspace(a, b, n+1)
    fval_vec = fun(dx_vec)
    maska = np.ones_like(dx_vec)*4
    maska[::2] = maska[::2] / 2
    maska[0] = 1
    maska[-1] = 1
    calka_wynik = dx/3 * np.matmul(maska, fval_vec.T)
    return calka_wynik

Saf10 = calka_simpson(funkcja, 0, 1.57, 10)
Saf20 = calka_simpson(funkcja, 0, 1.57, 38)
Saf100 = calka_simpson(funkcja, 0, 1.57, 100)
print('Wynik dla 10 przediałów całkowania: {:.4f}'.format(Saf10))
print('Wynik dla 38 przediałów całkowania: {:.4f}'.format(Saf20))
print('Wynik dla 100 przediałów całkowania: {:.4f}'.format(Saf100))
print('\n')
Ead10 = eps(Saa, Sad10)
Ead20 = eps(Saa, Sad20)
Ead100 = eps(Saa, Sad100)
print('Błąd procentowy dla 10 przediałów całkowania: {:.2f} %'.format(Ead10))
print('Błąd procentowy dla 38 przediałów całkowania: {:.2f} %'.format(Ead20))
print('Błąd procentowy dla 100 przediałów całkowania: {:.4f} %'.format(Ead100))


