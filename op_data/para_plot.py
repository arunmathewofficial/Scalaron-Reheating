import matplotlib.pyplot as plt
from itertools import islice
import numpy as np
import matplotlib as mpl
#mpl.rcParams['text.usetex'] = True
#mpl.rcParams['text.latex.preamble'] = [r'\usepackage{amsmath}']

plt.rcParams['text.latex.preamble'] = r"\usepackage{bm} \usepackage{amsmath}"


alpha = []
n_s = []
r = []

with open('para_space.txt', 'r') as f:
    for line in islice(f, 8, None):
        column = line.split()
        alpha.append(float(column[0]))
        n_s.append(float(column[3]))
        r.append(float(column[4]))



# plot n_s vs alpha
dy = 0.0042
fig, ax = plt.subplots(figsize=(6.4, 4.8), dpi=100)
plt.axhline(y=0.9649, xmin=0, xmax=1, color='k', linestyle='dashed', linewidth=2)
ax.plot(alpha, n_s, color='k')
plt.plot(15.1, 0.9649, 'bo')
plt.xlim([5, 27])
plt.ylim([0.92, 0.99])
ax.set_xlabel(r'$\alpha\,\ell_P^{-2}$', color="k", fontsize=25)
plt.ylabel('$n_s$', color="k", fontsize=25)
ax.tick_params(axis='x',which='major',direction='in',length=5,width=1,color='black',pad=15,labelsize=15,labelcolor='black')
ax.tick_params(axis='y',which='major',direction='in',length=5,width=1,color='black',pad=15,labelsize=15,labelcolor='black')
#ax.minorticks_on()
plt.tight_layout()
plt.savefig('Figure_ns.png')
plt.show()


# plot r vs alpha
fig, ax = plt.subplots(figsize=(6.4, 4.8), dpi=100)
ax.plot(alpha, r, color='k')
plt.axvline(x = 15.1, color = 'k', linestyle='dashed', linewidth=2)
#ax.arrow(15.1, 0, 0, 0.00138,  head_width=0.6, head_length=0.0001,color='black', linestyle='dashed')
plt.ylim([0, 0.0023])
#ax.plot(inf_tspan, Epsilon_4, '--', label='$\epsilon_4$')
# ax.plot(t, Theta, label='Theta')
ax.set_xlabel(r'$\alpha\,\ell_P^{-2}$', color="k", fontsize=25)
plt.plot(15.1, 0.00148, 'bo')
plt.ylabel('$r$', color="k", fontsize=25)
ax.tick_params(axis='x',which='major',direction='in',length=5,width=1,color='black',pad=15,labelsize=15,labelcolor='black')
ax.tick_params(axis='y',which='major',direction='in',length=5,width=1,color='black',pad=15,labelsize=15,labelcolor='black')
plt.tight_layout()
plt.savefig('Figure_r.png')
plt.show()


