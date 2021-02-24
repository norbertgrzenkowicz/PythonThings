import numpy as np
import matplotlib.pyplot as plt

def lmnk(z_mat, y_vec):
    tmp = np.matmul(z_mat.T, z_mat)  # tmp to zmienna pomocnicza
    tmp = np.linalg.inv(tmp)
    tmp = np.matmul(tmp, z_mat.T)
    a_vec = np.matmul(tmp, y_vec)
    return a_vec

np.set_printoptions(precision=3)
#parametry n dla zad.1 m dla zad.2
n = 0.519
m = 10

x = np.array([0, 25, 50, 100, 150, 200, 250, 300, 350, 400, 450,500], dtype='float')
x = np.reshape(x, (len(x), 1))  # Zamiana na wektor kolumnowy
y = np.array([0, n, 1.85, 2.08, 3.05, 4.41, 5.32, 6.39, 7.11, 8.18, 9.13, 10.42], dtype='float')
y = np.reshape(y, (len(y), 1))  # Zamiana na wektor kolumnowy

print(f'Wektor kolumnowy x: \n{x}')
print(f'Wektor kolumnowy y: \n{y}')

plt.figure(dpi=100)
plt.plot(x, y, '*')
plt.grid()
plt.xlabel('x')
plt.ylabel('y')
plt.show()

z = np.append(np.ones_like(x), x, axis=1)
print(f'Macierz z: \n{z}')


xm = np.linspace(0, 500, 500)
ym = a[0] + a[1] * xm
plt.figure(dpi=100)
plt.plot(x, y, '*', label='pomiary')
plt.plot(xm, ym, label='model')
plt.grid()
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.show()


