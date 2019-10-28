import numpy as np
import matplotlib.pyplot as plt

# theta in deg
theta_deg = 45
theta_rad = theta_deg*np.pi/180
# del_m in eV
del_m = 10
# L in km
L     = 1
# E in GeV
E     = 1



# fig 7.2 pg 262 equation 7.74
# We call the product del_m**2 * L/E as arg, since this appears in groups in many equations
#arg   = del_m**2 * L /(E)
arg   = np.arange(0,100,0.01)
P_ab  = np.sin(2*theta_rad)**2 * np.sin(1.27*arg)**2
fig, ax = plt.subplots()
ax.semilogx(arg, P_ab)
plt.plot(arg, P_ab)
ax.grid()
plt.xlabel("$L/E [km/GeV] \Delta m^2 [eV^2]$")
plt.ylabel("$P_{ab}$")
#plt.show()

#the averaged oscillation probability is in equation 7.93 pg 267
#sig_l_e = 0.2 * l_e # this is given in the caption for the fig 7.2

# change this value to see the effect of detector resolution
res_factor = 0.2 # # this is given in the caption for the fig 7.2

P_ab_avg  = 0.5*np.sin(2*theta_rad)**2 * (1-(np.cos(1.27*arg*2))*(np.exp(-0.5 *(1.27*2*arg/2 * res_factor)**2)))   # see the comment above for the factor 0.2
#fig, ax = plt.subplots()
#plt.plot(arg,P_ab_avg)
ax.semilogx(arg, P_ab_avg)
ax.grid()
ax.set_title("Fig. 7.2 Pg 262 of Kim and Guinti")
# plt.xlabel("$L/E [km/GeV] \Delta m^2 [eV^2]$")
# plt.ylabel("$P_{ab}^{avg}$")
plt.show()






