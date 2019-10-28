import numpy as np
import matplotlib.pyplot as plt

# exclusion plots used in neutrino physics as shown in Fig 7.3 in Pg. 269 of Kim and Guinti
# We call the product del_m**2 * L/E as arg, since this appears in groups in many equations
#arg   = del_m**2 * L /(E)
# read page 268:
# If an oscillation experiment does not observe any oscillations, the data imply an upper limit on the
# average transition probability which implies an upper limit on sin(2theta)**2
# sin(2theta)**2 < 2 P_ab_max / 1 - <cos(arg/2)>
# the analytical solution for <cos(arg/2> is given in the last few lines of pg 267
# <cos (arg/2> ~ cos(arg/2)*exp(-0.5(arg/2*sigma)**2)
# sigma = res_factor * L/E as given in the caption of fig 7.2

# following equation 7.99 Pg 268 of Kim and Guinti
P_ab_max = 0.1
arg   = np.arange(0.3,100,0.01)
res_factor = 0.2 # # this is given in the caption for the fig 7.2 and in pg. 268
avg_cos  = ((np.cos(1.27*arg*2))*(np.exp(-0.5 *(1.27*2*arg/2 * res_factor)**2)))
upper_limit = 2*P_ab_max/(1-avg_cos)
fig, ax = plt.subplots()
ax.semilogx(arg, upper_limit)
ax.grid()
ax.set_title("Fig. 7.3 Pg 269 of Kim and Guinti")
plt.xlabel("$L/E [km/GeV] \Delta m^2 [eV^2]$")
plt.ylabel("$sin^2(\theta)$")
plt.show()






