import numpy as np
import matplotlib.pyplot as plt
import math

np.set_printoptions(precision=3)

def lmnk(z_mat, y_vec):
    tmp = np.matmul(z_mat.T, z_mat)  # tmp to zmienna pomocnicza
    tmp = np.linalg.inv(tmp)
    tmp = np.matmul(tmp, z_mat.T)
    a_vec = np.matmul(tmp, y_vec)
    return a_vec

dane = np.loadtxt('dane_zadanie_3.csv', delimiter=',')
print(f'Liczba danych pomiarowych w jednej kolumnie: {len(dane)}')

plt.figure(dpi=100)
plt.plot(dane[:,0], dane[:,1], '*')
plt.grid()
plt.xlabel('x')
plt.ylabel('y')
plt.show()

x = dane[:,0]
x = np.reshape(x, (len(x), 1))
y = dane[:,1]
y = np.reshape(y, (len(y), 1))

zL = np.ones_like(x)
zL = np.append(zL, np.sin(x), axis=1)


aL = lmnk(zL, y)
print(f'Poszukiwany wektor parametrow dla regresji liniowej aL: \n{aL}')

xm = np.linspace(0, 15, 25)
yLm = 5 + np.sin(xm)
yLn= 5 +  np.cos(xm-1.70)


plt.figure(dpi=100)
plt.plot(x, y, '*', label='pomiary')
plt.plot(xm, yLm, 'g', label='sinus')
plt.plot(xm, yLn, 'r', label='cosinus')
plt.grid()
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.show()