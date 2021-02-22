import numpy as np
import matplotlib.pyplot as plt
np.set_printoptions(precision=3)
ea = lambda x_new, x_old : np.abs((x_new - x_old) / x_new) * 100


fun_z2 = lambda x : 0.95*x**3-5.9*x**2+10.9*x-6
fun_nr = lambda x : x - (0.95*x**3-5.9*x**2+10.9*x-6)/(2.85*x**2-11.8*x+10.9)

xx = np.linspace(3, 5, 101)
yy = fun_z2(xx)
plt.figure()
plt.grid()
plt.plot(xx, yy, label='f(x)')
plt.plot([3, 5], [0, 0], 'r', label='f(x) = 0')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.legend()
plt.show()

x_old = 4.4

for i in range(1, 7):
    xi = fun_nr(x_old)
    yi = fun_z2(xi)
    print('Iteracja: {:d}  |  xi: {:.3e}  |  yi: {:.3e}  |  blad wzgledny: {:.2f}'.format(i, xi, yi, ea(xi, x_old)))
    x_old = np.copy(xi)

print("\n")
fun_sec = lambda x, xp, fun : x - (fun(x) * (xp-x))/(fun(xp) - fun(x))

x_old_old = 2.5
x_old = 3.44


for i in range(1, 7):
    xi = fun_sec(x_old, x_old_old, fun_z2)
    yi = fun_z2(xi)
    print('Iteracja: {:d}  |  xi: {:.3e}  |  yi: {:.3e}  |  blad wzgledny: {:.2f}'.format(i, xi, yi, ea(xi, x_old)))
    x_old_old = np.copy(x_old)
    x_old = np.copy(xi)
