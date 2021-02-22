import numpy as np
import matplotlib.pyplot as plt

def circle(x, y, r):
    theta = np.linspace(0, 2 * np.pi, 500)
    xunit = r * np.cos(theta) + x
    yunit = r * np.sin(theta) + y
    return xunit, yunit

xc, yc = circle(0, 0, np.sqrt(37.2))
xc2, yc2 = circle(1, 5, np.sqrt(5.2))
plt.plot(xc, yc)
plt.plot(xc2, yc2)
plt.show()

ea = lambda x_new, x_old : np.abs((x_new - x_old) / x_new) * 100




x_vec = np.array([[3.07], [5.23]]) #punkty startowe

def jac_z4(x_vector):
    f11 = 2 * x_vector[0]
    f12 = 2* x_vector[1]
    f21 = 2 * x_vector[1] -2
    f22 = 2* x_vector[1] - 10
    jac = np.array([f11, f12, f21, f22])
    jac.shape = (2, 2)
    return jac

def fun_z4(x_vector):
    f1 = x_vector[0] ** 2 +  x_vector[1] - 37.2
    f2 = x_vector[0] * 2 - 2 * x_vector[0] + x_vector[1] * 2 - 10 * x_vector[1] + 22.07
    return np.array([f1, f2])

for i in range(1,6):
    jac_inv = np.linalg.inv(jac_z4(x_vec))
    x_vec_new = -np.matmul(jac_inv, fun_z4(x_vec)) + x_vec
    print('Iteracja: {}  |  x1: {}  |  x2: {}  |  blad wzgledny: {}'.format(i, x_vec_new[0], x_vec_new[1], ea(x_vec_new, x_vec).reshape(1,2)))
    x_vec = np.copy(x_vec_new)