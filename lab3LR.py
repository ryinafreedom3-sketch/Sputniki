import numpy as np
import matplotlib.pyplot as plt

Rz = 6371.21 # средний радиус Земли, км
beta_min = 25*np.pi/180 # минимальный угол места, рад (25 градусов)
N = 256 # длина массива
V = np.linspace(-2*np.pi, 2*np.pi, N) # истинная аномалия

# параметры эллиптических орбит бригады 5
p1 = 5*Rz # фокальный параметр, км
e1 = 0.9 # эксцентриситет
p2 = 5*Rz
e2 = 0.5
p3 = 5*Rz
e3 = 0.15
p4 = 5*Rz
e4 = 0.3

# траектории по формуле 1.1
r1 = p1/(1+e1*np.cos(V))
r2 = p2/(1+e2*np.cos(V))
r3 = p3/(1+e3*np.cos(V))
r4 = p4/(1+e4*np.cos(V))

# рисуем орбиты
plt.figure()
plt.polar(V, r1)
plt.polar(V, r2)
plt.polar(V, r3)
plt.polar(V, r4)
plt.grid("on") #сетка на графике

# высота полёта
h1 = r1 - Rz
h2 = r2 - Rz
h3 = r3 - Rz
h4 = r4 - Rz

# размер зоны радиовидимости по формуле 1.8
theta1 = np.arccos(Rz/(Rz+h1)*np.cos(beta_min)) - beta_min
theta2 = np.arccos(Rz/(Rz+h2)*np.cos(beta_min)) - beta_min
theta3 = np.arccos(Rz/(Rz+h3)*np.cos(beta_min)) - beta_min
theta4 = np.arccos(Rz/(Rz+h4)*np.cos(beta_min)) - beta_min

# рисуем семейство зависимостей размера зоны радиовидимости от высоты
plt.figure()
plt.plot(h1, theta1)
plt.plot(h2, theta2)
plt.plot(h3, theta3)
plt.plot(h4, theta4)
plt.grid("on") #сетка на графике

plt.show()