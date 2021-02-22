import numpy as np
from scipy.sparse import diags
import matplotlib.pyplot as plt

#podpunkt A
A1 = np.array([[1, 7, -4], [4, -4, 9], [12, -1, 3]], dtype=float)
b1 = np.array([[-51], [62], [8]], dtype=float)
print(f'Macierz A: \n{A1}')
print(f'Wektor b: \n{b1}')
invA1 = np.linalg.inv(A1)
x1 = np.matmul(invA1, b1)
print(f'Rozwiazanie ukladu rownan: \n{x1}')

#PODPUNKT B
A1 = np.array([[1, 7, -4], [4, -4, 9], [12, -1, 3]], dtype=float)
U = np.copy(A1)  # Kopia macierzy A do macierzy U, ktora nalezy wyznaczyc w wyniku elimincaji w przód
f_21 = U[1,0] / U[0,0]
print('Wspolczynnik f_21: {:.3f}'.format(f_21))
U[1,:] = U[1,:] - U[0,:] * f_21
print(f'Macierz U po pierwszym kroku eliminacji w przod: \n{U}')

f_31 = U[2,0] / U[0,0]
print('Wspolczynnik f_31: {:.3f}'.format(f_31))
U[2,:] = U[2,:] - U[0,:] * f_31
print(f'Macierz U po drugim kroku eliminacji w przod: \n{U}')

f_32 = U[2,1] / U[1,1]
print('Wspolczynnik f_32: {:.3f}'.format(f_32))
U[2,:] = U[2,:] - U[1,:] * f_32
print(f'Macierz U po trzecim kroku eliminacji w przod: \n{U}')

L = np.eye(3)
L[1,0] = f_21
L[2,0] = f_31
L[2,1] = f_32
print(f'Macierz L: \n{L}')

sprawdzenie = np.matmul(L,U)
print(f'Sprawdzenie: \n{A1 == sprawdzenie}')
print(f'Macierz A1: \n{A1}')
print(f'Wynik sprawdzenia: \n{sprawdzenie}')

#C

def podstawienie_ldb(macierz_L, wektor_b):
    d = np.zeros((3,1))
    d[0] = wektor_b[0]
    d[1] = wektor_b[1] - (macierz_L[1,0]*d[0])
    d[2] = wektor_b[2] - (macierz_L[2,0]*d[0] + macierz_L[2,1]*d[1])
    print(f'Wektor d: \n{d}')
    return d

def podstawienie_uxd(macierz_U, wektor_d):
    x = np.zeros((3,1))
    x[2] = wektor_d[2] / macierz_U[2,2]
    x[1] = (-(macierz_U[1,2]*x[2]) + wektor_d[1]) / macierz_U[1,1]
    x[0] = (-(macierz_U[0,1]*x[1] + macierz_U[0,2]*x[2]) + wektor_d[0]) / macierz_U[0,0]
    print(f'Wektor rozwiazan x: \n{x}')
    return x
b1 = np.array([[1], [0], [0]])
d1 = podstawienie_ldb(L, b1)

x1 = podstawienie_uxd(U, d1)

b2 = np.array([[0], [1], [0]])
d2 = podstawienie_ldb(L, b2)
x2 = podstawienie_uxd(U, d2)

b3 = np.array([[0], [0], [1]])
d3 = podstawienie_ldb(L, b3)
x3 = podstawienie_uxd(U, d3)

inv_A1 = np.column_stack((x1, x2, x3))
print(f'Macierz odwrotna do macierzy A:\n {inv_A1}')

#D

I = np.matmul(A1, inv_A1)

print(f'Wynik przemnożenia macierzy A oraz macierzy odwrotnej do A:'\n {I})