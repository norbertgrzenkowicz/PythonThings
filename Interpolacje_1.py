import numpy as np

np.set_printoptions(precision=3)
def interpolacja_liniowa(x, f, xp):
    f1 = f[0] + (f[1] - f[0])/(x[1] - x[0]) * (xp - x[0])
    return f1

def interpolacja_kwadratowa(x, f, xp):
    b0 = f[0]
    b1 = (f[1] - f[0]) / (x[1] - x[0])
    b2 = ((f[2] - f[1]) / (x[2] - x[1]) - (f[1] - f[0]) / (x[1] - x[0])) / (x[2] - x[0])
    f2 = b0 + b1 * (xp - x[0]) + b2 * (xp - x[0]) * (xp - x[1])
    return f2

def iloraz_roznicowy(fxi, fxj, xi, xj):
    df_dx = (fxi - fxj) / (xi - xj)
    return df_dx

def lagrange(x, f, xp):
    sum = 0
    for i in range(0, x.size):
        product = f[i]
        for j in range(0, x.size):
            if i != j:
                product = product * (xp - x[j]) / (x[i] - x[j])
        sum = sum + product
    return sum

# parametr n=0.43197

print("Zadanie 1 a) Interpolacja liniowa\n")

x_data = np.array([1, 40])
f_data = np.array([0, 3.68887945])
oszacowanie = interpolacja_liniowa(x_data, f_data, 0.43197)
wartosc_dokladna = -0.8393991376
blad_oszacowania = (wartosc_dokladna - oszacowanie)/wartosc_dokladna * 100
print('Wartść oszacowania w przedziale [0,40]: {:.7f}'.format(oszacowanie))
print('Blad oszacowania: {:.2f}%'.format(blad_oszacowania))

print("\nZadanie 1 b) Interpolacja kwadratowa\n")

x_data = np.array([1, 35, 40])
f_data = np.array([0, 3.55534806 , 3.68887945])
oszacowanie = interpolacja_kwadratowa(x_data, f_data, 0.43197)
wartosc_dokladna= -0.8393991376
blad_oszacowania = (wartosc_dokladna - oszacowanie)/wartosc_dokladna * 100
print('Wartść oszacowania w przedziale [0, 40]: {:.7f}'.format(oszacowanie))
print('Blad oszacowania: {:.2f}%'.format(blad_oszacowania))

print("\nZadanie 2 a) Interpolacja liniowa\n")

x_data = np.array([0, 1.37444679])
f_data = np.array([0, 5.02733949])
oszacowanie = interpolacja_liniowa(x_data, f_data, 0.43197)
wartosc_dokladna = 0.46100753923
blad_oszacowania = (wartosc_dokladna - oszacowanie)/wartosc_dokladna * 100
print('Wartść oszacowania w przedziale [0,1.37444679]: {:.7f}'.format(oszacowanie))
print('Blad oszacowania: {:.2f}%'.format(blad_oszacowania))

print("\nZadanie 2 b) Interpolacja kwadratowa\n")

f_x1x0 = iloraz_roznicowy(0.41421356, 0, 0.39269908, 0)
f_x2x1 = iloraz_roznicowy(1, 0.41421356, 0.78539816, 0.39269908)
f_x3x2 = iloraz_roznicowy(5.02733949, 1, 1.37444679, 0.78539816)

print('Iloraz roznicowy pierwszego rzedu [i=0]: {:.3f}'.format(f_x1x0))
print('Iloraz roznicowy pierwszego rzedu [i=1]: {:.3f}'.format(f_x2x1))
print('Iloraz roznicowy pierwszego rzedu [i=2]: {:.3f}'.format(f_x3x2))

f_x2x1x0 = iloraz_roznicowy(f_x2x1, f_x1x0, 0.78539816, 0)
f_x3x2x1 = iloraz_roznicowy(f_x3x2, f_x2x1, 1.37444679, 0.39269908)

print('Iloraz roznicowy drugiego rzedu [i=0]: {:.3f}'.format(f_x2x1x0))
print('Iloraz roznicowy drugiego rzedu [i=1]: {:.3f}'.format(f_x3x2x1))

f_x3x2x1x0 = iloraz_roznicowy(f_x3x2x1, f_x2x1x0, 1.37444679, 0)
print('Iloraz roznicowy trzeciego rzedu [i=0]: {:.3f}'.format(f_x3x2x1x0))

x = 0.43197
oszacowanie = 0 + f_x1x0 * (x-0) + f_x2x1x0 * (x-0) * (x-0.39269908) + f_x3x2x1x0 * (x-0) * (x-0.39269908) * (x-0.78539816)
blad_oszacowania = (wartosc_dokladna - oszacowanie)/wartosc_dokladna * 100
print('Wartść oszacowania: {:.7f}'.format(oszacowanie))
print('Blad oszacowania: {:.2f}%'.format(blad_oszacowania))


print("\nZadanie 3 a) Interpolacja liniowa\n")

x_data = np.array([0,32])
f_data = np.array([14.621, 7.305])
oszacowanie = interpolacja_liniowa(x_data, f_data, 27)
print('Wartść oszacowania w przedziale [0,32]: {:.7f}'.format(oszacowanie))

print("\nZadanie 3 b) Interpolacja wielomianem Lagrange'a\n")

x_data = np.array([0, 8, 16, 24,32,40])
f_data = np.array([14.621, 11.843, 9.870, 8.418, 7.305, 6.413])

oszacowanie = lagrange(x_data, f_data, 27)
print('Wartść oszacowania: {:.7f}'.format(oszacowanie))
