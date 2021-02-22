import numpy as np
import matplotlib.pyplot as plt

dydx1 = lambda x : 10*np.sin(np.pi*x)-4.5

y_dok = lambda x : (-10/np.pi)*np.cos(np.pi*x)-4.5*x+0.9+(10/np.pi)

def eulerODE(x0, y0, xf, funkcja_nachylenia, h):
    liczba_krokow = int((xf - x0)/h)
    x_array = np.zeros(liczba_krokow+1)
    x_array[0] = x0
    y_array = np.zeros_like(x_array)
    y_array[0] = y0
    for i in range(0, liczba_krokow):
        x_array[i+1] = x_array[i] + h
        y_array[i+1] = y_array[i] + funkcja_nachylenia(x_array[i]) * h
    return x_array, y_array

x1, y1 = eulerODE(x0=0, y0=1, xf=4, funkcja_nachylenia=dydx1, h=0.25)
plt.figure(figsize=(8,6), dpi=100)

plt.subplot(2,1,1)
plt.plot(x1, y1, '.-', label='Euler h=0.25')
x_dok = np.linspace(0, 4, 101)
plt.plot(x_dok, y_dok(x_dok), '--', label='Rozw. dokladne')
plt.grid()
plt.legend()
plt.title('Rozwiazanie rownania rozniczkowego metoda Eulera i rozw. dokladne')
plt.xlabel('x')
plt.ylabel('y')

plt.subplot(2,1,2)
x_dok_err = np.linspace(0, 4, len(x1))
plt.plot(x_dok_err, y_dok(x_dok_err)-y1, '.-', label='Blad bezwzgledny')
blad_sredni = np.mean(y_dok(x_dok_err)-y1)
plt.plot(x_dok_err, blad_sredni * np.ones_like(x_dok_err), '.-r', label='Blad sredni')
plt.grid()
plt.legend()
plt.title('Blad pomiedzy rozwiazaniem dokladnym a rozwiazaniem metoda Eulera')
plt.xlabel('x')
plt.ylabel('Blędy obliczeń')


plt.tight_layout()
plt.show()

print('Blad sredni obliczen dla kroku h=0.5: {:.3f}'.format(blad_sredni))

x1, y1 = eulerODE(x0=0, y0=1, xf=4, funkcja_nachylenia=dydx1, h=0.1)
plt.figure(figsize=(8,6), dpi=100)

plt.subplot(2,1,1)
plt.plot(x1, y1, '.-', label='Euler h=0.1')
x_dok = np.linspace(0, 4, 101)
plt.plot(x_dok, y_dok(x_dok), '--', label='Rozw. dokladne')
plt.grid()
plt.legend()
plt.title('Rozwiazanie rownania rozniczkowego metoda Eulera i rozw. dokladne')
plt.xlabel('x')
plt.ylabel('y')

plt.subplot(2,1,2)
x_dok_err = np.linspace(0, 4, len(x1))
plt.plot(x_dok_err, y_dok(x_dok_err)-y1, '.-', label='Blad bezwzgledny')
blad_sredni = np.mean(y_dok(x_dok_err)-y1)
plt.plot(x_dok_err, blad_sredni * np.ones_like(x_dok_err), '.-r', label='Blad sredni')
plt.grid()
plt.legend()
plt.title('Blad pomiedzy rozwiazaniem dokladnym a rozwiazaniem metoda Eulera')
plt.xlabel('x')
plt.ylabel('Blędy obliczeń')


plt.tight_layout()
plt.show()

print('Blad sredni obliczen dla kroku h=0.05: {:.3f}'.format(blad_sredni))

x1, y1 = eulerODE(x0=0, y0=1, xf=4, funkcja_nachylenia=dydx1, h=0.01)
plt.figure(figsize=(8,6), dpi=100)

plt.subplot(2,1,1)
plt.plot(x1, y1, '-', label='Euler h=0.01')
x_dok = np.linspace(0, 4, 101)
plt.plot(x_dok, y_dok(x_dok), '--', label='Rozw. dokladne')
plt.grid()
plt.legend()
plt.title('Rozwiazanie rownania rozniczkowego metoda Eulera i rozw. dokladne')
plt.xlabel('x')
plt.ylabel('y')

plt.subplot(2,1,2)
x_dok_err = np.linspace(0, 4, len(x1))
plt.plot(x_dok_err, y_dok(x_dok_err)-y1, '-', label='Blad bezwzgledny')
blad_sredni = np.mean(y_dok(x_dok_err)-y1)
plt.plot(x_dok_err, blad_sredni * np.ones_like(x_dok_err), '-r', label='Blad sredni')
plt.grid()
plt.legend()
plt.title('Blad pomiedzy rozwiazaniem dokladnym a rozwiazaniem metoda Eulera')
plt.xlabel('x')
plt.ylabel('Blędy obliczeń')

plt.tight_layout()
plt.show()

print('Blad sredni obliczen dla kroku h=0.005: {:.3f}'.format(blad_sredni))