# Script to calculate spectral index as a function of beta
# Author: Arun Mathew

import numpy as np
from scipy.integrate import solve_ivp
import math
import matplotlib.pyplot as plt
from matplotlib.ticker import (MultipleLocator, AutoMinorLocator)
import pandas as pd

# define spectral index ns and r
def spectral_index(e1, e3, e4):
    ns = 4 - 2 * math.sqrt(0.25 + (1 + e1 - e3 + e4) * (2 - e3 + e4) / pow(1 - e3, 2))
    r = 48 * pow(e3, 2) / pow(1 + e3, 2)
    return ns, r

# define the function that represents the differential equation
def eq(t, y, alpha, beta, H0):
    dydt = y[1]
    d2ydt2 = (beta/alpha) * (y[0]**3 + 1.5 * dydt * y[0] + (dydt**2)/(2*y[0])) - (1/(12*alpha*H0**2)) * y[0] - 3*y[1]*y[0] + (dydt**2)/2
    return [dydt, d2ydt2]

# return dimensionless Ricci Scalar R/H0^2 = 6(dy/dy+ 2y^2)
def ricci(y):
    return 6.0*( y[1] + 2.0*np.power(y[0], 2) )


Ne = 60.0  # Number of e-foldings
alpha = (8*pow(Ne,2)*pow(10,6)/27)
print('alpha = ', '{:.5e}'.format(alpha))

ns_array = []
beta_array = []
r_array = []
H0_array = []


for i in range(1, 200, 1):
    # for loop will generate the value of the parameter beta
    beta = (1 + i/20) * 1e+07

    #print('beta = ', '{:.5e}'.format(beta))
    HS = 1 / math.sqrt(12 * beta)
    H0 = HS * math.sqrt(1 - math.exp(-2 * beta * Ne / (3 * alpha)))
    #print('H0 = ', '{:.5e}'.format(H0))

    # initial condition
    y_initial = 1
    ydot_initial = beta * np.power(y_initial, 2) / (3 * alpha) - 1 / (36 * alpha * np.power(H0, 2))

    # set the initial conditions and parameters
    y0 = [y_initial, ydot_initial]  # initial values for y and dy/dt
    t_span = [0, 1000]  # time interval for the solution

    # define the event function that stops the integration when dy/dt / (y^2) = 1
    def event(t, y):
        dydt = y[1]
        y_val = y[0]
        e_1 = - dydt / (y_val ** 2)
        return 0 if e_1 > 1 else 1


    event.terminal = True

    # set the options for the solver, including the event function
    options = {'events': event}

    # solve the differential equation using the fourth-order Runge-Kutta method
    sol = solve_ivp(lambda t, y: eq(t, y, alpha, beta, H0), t_span, y0, method='RK45', events=event, max_step=0.01)

    # first slow role parameter
    epsilon_1 = - sol.y[1] / (sol.y[0] ** 2)
    #print('epsilon_1 =', '{:.5e}'.format(epsilon_1[0]))

    # defining R0
    R0 = 12.0 * np.power(H0, 2.0)

    # defining dimensionless ricci scalar
    r = ricci(sol.y)

    # defining F
    F = 1 + (2 * alpha + beta) * np.power(H0, 2.0) * r + 2.0 * beta * np.power(H0, 2.0) * r * np.log(
        np.power(H0, 2.0) * r / R0)

    # defining derivative of r
    dr_dt = np.gradient(r, sol.t)

    # defining dimensionless dF/dt
    dF_dt = (2 * alpha + 3 * beta) * np.power(H0, 2.0) * dr_dt + 2.0 * beta * np.power(H0, 2.0) * dr_dt * np.log(
        np.power(H0, 2.0) * r / R0)

    # epsilon_3
    epsilon_3 = dF_dt / (2 * sol.y[0] * F)
    #print('epsilon_3 =', '{:.5e}'.format(epsilon_3[0]))

    # defining dimensionless d2F/dt2
    d2F_dt2 = np.gradient(dF_dt, sol.t)

    # epsilon_4
    epsilon_4 = d2F_dt2 / (sol.y[0] * dF_dt)
    #print('epsilon_4 =', '{:.5e}'.format(epsilon_4[0]))

    ns, r = spectral_index(epsilon_1[0], epsilon_3[0], epsilon_4[0])

    print('For beta = ', '{:.5e},'.format(beta), 'H0 = ', '{:.5e},'.format(H0), 'ns = ', '{:.5e},'.format(ns), 'r = ', '{:.5e}'.format(r))

    beta_array.append(beta)
    H0_array.append(H0)
    ns_array.append(ns)
    r_array.append(r)

# save data to file ======================================
dict = {}
dict['beta'] = beta_array
dict['H0'] = H0_array
dict['n_s'] = ns_array
dict['r'] = r_array
df = pd.DataFrame(dict)
data_file = 'Spectral_Index.txt'
print('Writing data to file', data_file)
df.to_csv(data_file, sep=' ', index=False, float_format='%.8e')
with open(data_file, 'r+') as file:
    contents = file.read()
    file.seek(0, 0)
    file.write('# Spectral index as function of parameter beta \n')
    file.write('# with alpha = {:.8e}'.format(alpha) + ' $t_p^2$\n\n'+contents)

# Plotter ===================================================
fig, ax = plt.subplots(nrows=1, ncols=2, figsize=(8,3), sharex=False, sharey=False)

ax[0].plot(beta_array, ns_array, label='n_s',linestyle='-', color='black', linewidth=0.75)
ax[0].plot([-1e+7, 4.55e+07, 4.55e+07], [0.9649, 0.9649, 0], label='r', linestyle='--', color='crimson', linewidth=0.75)
ax[0].xaxis.set_minor_locator(AutoMinorLocator())
ax[0].yaxis.set_minor_locator(AutoMinorLocator())
ax[0].tick_params(axis="both", direction="in", which="both",
                          bottom=True, top=True, left=True, right=True, length=3)
ax[0].set_xlim([0, 1.2e+8])
ax[0].set_ylim([0.9, 1.0])
ax[0].set_xlabel(r'$\rm \beta (t_p^2)$', fontsize=12)
ax[0].set_ylabel(r'$\rm n_s$', fontsize=14)


ax[1].plot(beta_array, r_array, label='r', linestyle='-', color='black', linewidth=0.75)
ax[1].plot([4.55e+07, 4.55e+07, 0], [-0.0002, 5.13280270e-04, 5.13280270e-04], label='r', linestyle='--', color='crimson', linewidth=0.75)
ax[1].xaxis.set_minor_locator(AutoMinorLocator())
ax[1].yaxis.set_minor_locator(AutoMinorLocator())
ax[1].tick_params(axis="both", direction="in", which="both",
                          bottom=True, top=True, left=True, right=True, length=3)
ax[1].set_ylim([-0.0002, 0.0025])
ax[1].set_xlim([0, 1.2e+8])
ax[1].set_xlabel(r'$\rm \beta (t_p^2)$', fontsize=12)
ax[1].set_ylabel(r'$\rm r$', fontsize=14)

plt.subplots_adjust(left=None, bottom=None, right=None, top=None, wspace=0.3, hspace=None)
plt.savefig('Spectral_Index.png', bbox_inches='tight', dpi=300)
