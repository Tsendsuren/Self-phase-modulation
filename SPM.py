# -*- coding: utf-8 -*-
"""
Created on Fri Feb 23 14:04:51 2018

@author: Tsende
"""
import numpy as np
import matplotlib.pyplot as plt

t = np.arange(-80e-15,80e-15,1e-16)
tau = 28e-15 # input pulse duration, fs
I0 = 5*1e-10 # peak intensity, W/cm2
I = I0*np.exp(-(t**2/tau**2))

lambd0 = 790e-9 # central frequency
c = 299792458
w0 = (2*np.pi*c)/lambd0

nl = 1 # linear refractive index
n2 = 1.26-24 # nonlinear refractive index
L = 100
w = w0+((4*np.pi*L*n2*t*I)/(lambd0*tau**2))
tau_new = np.fft.fft(w)
lambd = (2*np.pi*c)/w

plt.subplot(211)
plt.plot(t*1e15,I*1e10)
plt.title('Self phase modulation')
plt.grid(which='both',linestyle='-.', linewidth='0.5', color='grey')
plt.subplot(212)
plt.plot(t*1e15,lambd*1e9,'r')
plt.xlabel('Time (fs)')
plt.ylabel('Wavelength (nm)')
plt.grid(which='both',linestyle='-.', linewidth='0.5', color='grey')


plt.savefig("Self phase modulation.png", dpi=1600)