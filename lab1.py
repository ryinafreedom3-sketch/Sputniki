import numpy as np
import matplotlib.pyplot as plt

min_limit_uniform = 9
max_limit_uniform = 11
N = 300
massive_uniform = np.random.uniform(min_limit_uniform,max_limit_uniform,N)

plt.figure(1)
plt.plot(massive_uniform)
plt.grid("on")

ampl1 = 1
ampl2 = 1
ampl3 = 1
ampl4 = 9
ampl5 = 6
f1 = 1
f2 = 5
f3 = 6
f4 = 4
f5 = 2
min_limit_x = 0
max_limit_x = 2*np.pi
N = 300
x = np.linspace(min_limit_x, max_limit_x, N)
massive_sin = ampl1*np.sin(f1*x) + ampl2*np.sin(f2*x) + ampl3*np.sin(f3*x) + ampl4*np.sin(f4*x) + ampl5*np.sin(f5*x)
plt.figure(2)
plt.plot(massive_sin)
plt.grid("on")

massive_add = massive_sin + massive_uniform
plt.figure(3)
plt.plot(massive_add)
plt.grid("on")

massive_mult = massive_sin * massive_uniform
plt.figure(4)
plt.plot(massive_mult)
plt.grid("on")

spectrum_add = np.fft.fft(massive_add)
spectrum_sin = np.fft.fft(massive_sin)
spectrum_uniform = np.fft.fft(massive_uniform)
plt.figure(5)
plt.plot(abs(spectrum_add))
plt.grid("on")

plt.figure(6)
plt.plot(abs(spectrum_sin))
plt.grid("on")

plt.figure(7)
plt.plot(abs(spectrum_uniform))
plt.grid("on")

back_add = np.fft.ifft(spectrum_add).real
back_sin = np.fft.ifft(spectrum_sin).real
back_uniform = np.fft.ifft(spectrum_uniform).real
plt.figure(8)
plt.plot(back_add)
plt.grid("on")

plt.figure(9)
plt.plot(back_sin)
plt.grid("on")

plt.figure(10)
plt.plot(back_uniform)
plt.grid("on")

plt.show()