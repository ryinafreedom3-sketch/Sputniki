import numpy as np
import matplotlib.pyplot as plt

ampl = 1
f0 = 1
min_limit_x = 0
max_limit_x = 1
N = 300
fd = N/max_limit_x
x = np.linspace(min_limit_x, max_limit_x, N) # создаём ось
massive_sin1 = ampl*np.sin(2*np.pi*f0*x)
plt.figure()
plt.plot(x, massive_sin1)
plt.grid("on")

M = 4*N
f_range = np.zeros(M)
for smp_ref in range(-int(M/2), int(M/2)):
    f_range[smp_ref] = (smp_ref / M)*fd
fft_result = np.fft.fft(massive_sin1, M)/N
mod_fftshift_result = abs(fft_result)
plt.figure()
plt.plot(f_range, mod_fftshift_result)
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
massive_sin1 = ampl1*np.sin(2*np.pi*f1*x)
massive_sin2 = ampl2*np.sin(2*np.pi*f2*x)
massive_sin3 = ampl3*np.sin(2*np.pi*f3*x)
massive_sin4 = ampl4*np.sin(2*np.pi*f4*x)
massive_sin5 = ampl5*np.sin(2*np.pi*f5*x)
add_sig = massive_sin1 + massive_sin2 + massive_sin3 + massive_sin4 + massive_sin5
plt.figure()
plt.plot(x, add_sig)
plt.grid("on")
fft_result = np.fft.fft(add_sig, M)/N
mod_fftshift_result = abs(fft_result)
plt.figure()
plt.plot(f_range, mod_fftshift_result)
plt.grid("on")

min_limit_uniform = 9
max_limit_uniform = 11
massive_uniform = np.random.uniform(min_limit_uniform,max_limit_uniform,N)
add_smes = add_sig + massive_uniform
plt.figure()
plt.plot(x, add_smes)
plt.grid("on")
fft_result = np.fft.fft(add_smes, M)/N
mod_fftshift_result = abs(fft_result)
plt.figure()
plt.plot(f_range, mod_fftshift_result)
plt.grid("on")

a4h = np.zeros(M)
freq_rez = 4
polosa = 8
min_a4h_freq = freq_rez - polosa/2
max_a4h_freq = freq_rez + polosa/2
for smp_ref in range(-int(M/2), int(M/2)):
    if (f_range[smp_ref] > min_a4h_freq):
        if (f_range[smp_ref] < max_a4h_freq):
            a4h[smp_ref] = 1
    if (f_range[smp_ref] < -min_a4h_freq):
        if (f_range[smp_ref] > -max_a4h_freq):
            a4h[smp_ref] = 1
plt.figure()
plt.plot(f_range, a4h)
plt.grid("on")
filtered_add_smes_spektr = a4h*fft_result
filtered_add_smes = N*np.fft.ifft(filtered_add_smes_spektr)
invert_fft_mas_len = int(len(filtered_add_smes)*N/M)
plt.figure()
plt.plot(x, filtered_add_smes[0:invert_fft_mas_len])
plt.grid("on") #сетка на графике

plt.show()