import numpy as np
import matplotlib.pyplot as plt

np.set_printoptions(precision=3)

n=10

def lmnk(z_mat, y_vec):
    tmp = np.matmul(z_mat.T, z_mat)  # tmp to zmienna pomocnicza
    tmp = np.linalg.inv(tmp)
    tmp = np.matmul(tmp, z_mat.T)
    a_vec = np.matmul(tmp, y_vec)
    return a_vec

x = np.array([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30], dtype='float')
x = np.reshape(x, (len(x), 1))
y = np.array([1,1,5,6,11,17,22,31,51,68,104,125,176,236,285,355,425,536,634,749,901,1051,1221,1389,1638,1862,2055,2311,2554,2946], dtype='float')
y = np.reshape(y, (len(y), 1))

plt.figure(dpi=100)
plt.plot(x, y, '*')
plt.grid()
plt.xlabel('x')
plt.ylabel('y')
plt.show()

y_ln = np.log(y)
print(f'Wektor y po operacji logarytmowania: \n{y_ln}')

z = np.append(np.ones_like(x), x, axis=1)
print(f'Macierz z: \n{z}')

a = lmnk(z, y_ln)
print(f'Poszukiwany wektor parametrow a: \n{a}')

alpha = np.exp(a[0])
beta = a[1]
print(f'Parametr alpha: \n{alpha}')
print(f'Parametr beta: \n{beta}')

xm = np.linspace(0, 40, 40)
ym = alpha * np.exp(beta * xm)
plt.figure(dpi=100)
plt.plot(x, y, '*', label='pomiary')
plt.plot(xm, ym, label='model')
plt.grid()
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.show()

print("XXXXXXXXXXXXX")
print(alpha * np.exp(beta*40))