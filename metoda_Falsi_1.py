import numpy as np
import matplotlib.pyplot as plt

def false_position(x_upper, x_lower, fun):
    x_result = x_upper - (fun(x_upper) * (x_lower - x_upper))/(fun(x_lower) - fun(x_upper))
    f_xresult = fun(x_result)
    return x_result, f_xresult

np.set_printoptions(precision=3)

f = lambda x : - 26 + 85*x - 91*x**2+44*x**3-8*x**4+x**5

xl = 0.19
xu = 0.6

print('Dolna wartosc przedziału: {:.4f}'.format(xl))
print('Wartosc funkcji dla dolnej wartosci przedzialu: {:.4f}'.format(f(xl)))
print('Gorna wartosc przedziału: {:.4f}'.format(xu))
print('Wartosc funkcji dla gornej wartosci przedzialu: {:.4f}'.format(f(xu)))

xx = np.linspace(xl, xu, 101)
yy = f(xx)
plt.figure()
plt.grid()
plt.plot(xx, yy, label='f(x)')
plt.plot([xl, xu], [0, 0], 'r', label='f(x) = 0')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.legend()
plt.show()

print("\n")
xr, f_xr = false_position(xu, xl, f)
print('Pierwsza iteracja metody falsi: xr = {:.4f}  |  f(xr) = {:.4f}'.format(xr, f_xr))
print("\n")


var1 = f(xl) * f(xr) > 0
var2 = f(xu) * f(xr) > 0
print(var1,var2)
print("\n")

xu = np.copy(xr)
xr_old = np.copy(xr)
print('Dolna wartosc przedziału: {:.4f}'.format(xl))
print('Wartosc funkcji dla dolnej wartosci przedzialu: {:.4f}'.format(f(xl)))
print('Gorna wartosc przedziału: {:.4f}'.format(xu))
print('Wartosc funkcji dla gornej wartosci przedzialu: {:.4f}'.format(f(xu)))

print("\n")
xr, f_xr = false_position(xu, xl, f)
print('Druga iteracja metody falsi: xr = {:.4f}  |  f(xr) = {:.4f}'.format(xr, f_xr))
print("\n")

ea = lambda x_new, x_old : np.abs((x_new - x_old) / x_new) * 100
print('Blad wzgledny: {:.2f}%'.format(ea(xr, xr_old)))

print("\n")
var1 = f(xl) * f(xr) > 0
var2 = f(xu) * f(xr) > 0
print(var1,var2)
print("\n")

xu = np.copy(xr)
xr_old = np.copy(xr)
print('Dolna wartosc przedziału: {:.4f}'.format(xl))
print('Wartosc funkcji dla dolnej wartosci przedzialu: {:.4f}'.format(f(xl)))
print('Gorna wartosc przedziału: {:.4f}'.format(xu))
print('Wartosc funkcji dla gornej wartosci przedzialu: {:.4f}'.format(f(xu)))

xr, f_xr = false_position(xu, xl, f)
print('Trzecia iteracja metody falsi: xr = {:.4f}  |  f(xr) = {:.4f}'.format(xr, f_xr))
print('Blad wzgledny: {:.2f}%'.format(ea(xr, xr_old)))

print("\n")

var1 = f(xl) * f(xr) > 0
var2 = f(xu) * f(xr) > 0
print(var1,var2)
print("\n")

xu = np.copy(xr)
xr_old = np.copy(xr)
print('Dolna wartosc przedziału: {:.4f}'.format(xl))
print('Wartosc funkcji dla dolnej wartosci przedzialu: {:.4f}'.format(f(xl)))
print('Gorna wartosc przedziału: {:.4f}'.format(xu))
print('Wartosc funkcji dla gornej wartosci przedzialu: {:.4f}'.format(f(xu)))
print("\n")

xr, f_xr = false_position(xu, xl, f)
print('Czwarta iteracja metody falsi: xr = {:.4f}  |  f(xr) = {:.4f}'.format(xr, f_xr))
print('Blad wzgledny: {:.2f}%'.format(ea(xr, xr_old)))

var1 = f(xl) * f(xr) > 0
var2 = f(xu) * f(xr) > 0
print(var1,var2)
print("\n")

xu = np.copy(xr)
xr_old = np.copy(xr)
print('Dolna wartosc przedziału: {:.4f}'.format(xl))
print('Wartosc funkcji dla dolnej wartosci przedzialu: {:.4f}'.format(f(xl)))
print('Gorna wartosc przedziału: {:.4f}'.format(xu))
print('Wartosc funkcji dla gornej wartosci przedzialu: {:.4f}'.format(f(xu)))
print("\n")

xr, f_xr = false_position(xu, xl, f)
print('piata iteracja metody falsi: xr = {:.4f}  |  f(xr) = {:.4f}'.format(xr, f_xr))
print('Blad wzgledny: {:.2f}%'.format(ea(xr, xr_old)))