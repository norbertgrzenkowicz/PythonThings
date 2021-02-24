import numpy as np
import matplotlib.pyplot as plt
np.set_printoptions(precision=3)

def circle (x,y,r):
    theta = np.linspace(0, 2*np.pi, 101)
    xunit = r*np.cos(theta) + x
    yunit = r*np.sin(theta) + y
    return xunit, yunit

xc, yc = circle(4, 4, np.sqrt(5))
xc2, yc2 = circle(0,0,4)
plt.figure(figsize=(8, 8))
plt.plot(xc,yc)
plt.plot(xc2,yc2)
plt.show()

x_vec = np.array([1.8, 3.5])
def jac(x_vector):
    f11 = 2 * x_vector[0] - 8
    f12 = 2 * x_vector[1] - 8
    f21 = 2 * x_vector[0]
    f22 = 2 * x_vector[1]
    jac = np.array([f11, f12, f21, f22])
    jac.shape = (2, 2)
    return jac
def fun(x_vector):
    f1 = (x_vector[0] - 4) ** 2 + (x_vector[1] - 4)**2 - 5
    f2 = x_vector[0] ** 2 + x_vector[1]**2 - 16
    return np.array([f1, f2])


x_vec_old = np.copy(x_vec)
print(x_vec_old)

ea = lambda x_new, x_old : np.abs((x_new - x_old) / x_new) * 100

for i in range(1,6):
    jac_inv = np.linalg.inv(jac(x_vec))
    x_vec_new = -np.matmul(jac_inv, fun(x_vec)) + x_vec
    print('Iteracja: {}  |  x: {:.7}  |  y: {:.7}  |  blad wzgledny x: {:.4} | błąd względny y: {:.4}'.format(i, x_vec_new[0], x_vec_new[1], ea(x_vec_new[0], x_vec[0]),ea(x_vec_new[1], x_vec[1])))
    x_vec = np.copy(x_vec_new)