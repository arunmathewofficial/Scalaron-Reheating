# Setting up the Field Equation file
# Author: Arun Mathew
from scipy import constants as const
import math
import numpy
from matplotlib import pyplot as plt
from numpy import diff
from sympy import *


#########################################################################
# Common Physical Constants
c = const.c  # Speed of Light
G = const.G  #
pi = const.pi
hbar  = const.hbar
l_P  = math.sqrt(hbar*G/pow(c,3.0))
t_P  = l_P/c

def Hubble(alpha, beta, Ne, t):
    HS = 1 / math.sqrt(12 * beta)
    H0 = HS * math.sqrt(1 - math.exp(-2 * beta * Ne / (3 * alpha)))
    te = 18*alpha*H0*math.log((HS+H0)/(HS-H0))
    return HS*math.tanh((te-t)/(36*alpha*HS))

def Ricci(H, dHdt):
    return 6 * (dHdt + 2 * pow(H, 2))

# Slow-roll parameters
# First slow roll parameter epsilon_1 = -HDOT/H^2
def epsilon_1(H, dHdt):
        return - dHdt / pow(H, 2)


# Third slow roll parameter epsilon_3 = FDOT/2HF
def epsilon_3(H, F, Fdot):
    return Fdot/(2*H*F)


def epsilon_4(H, Fdot, F2dot):
    return F2dot/(H*Fdot)


def spectral_index(e1, e3, e4,):
    ns = 4 - 2 * math.sqrt(0.25 + (1 + e1 - e3 + e4) * (2 - e3 + e4) / pow(1 - e3, 2))
    r = 48 * pow(e3, 2) / pow(1 + e3, 2)
    return ns, r

filename = 'beta_para_space'
filetype = "txt"



# Main ##################################################################


beta = 9.0*pow(10, 8) * pow(t_P, 2)

Ne = 60.0  # Number of e-foldings
alpha = (8*pow(Ne,2)*pow(10,6)/27)*pow(t_P, 2)
print("alpha = {:e}".format(alpha/pow(t_P,2.0)))
print("beta = {:e}".format(beta/pow(t_P,2.0)))
HS = 1 / math.sqrt(12 * beta)
H0 = HS * math.sqrt(1 - math.exp(-2 * beta * Ne / (3 * alpha)))

te = 18 * alpha * H0 * math.log((HS + H0) / (HS - H0))
print("t_e = {:e}".format(te/t_P))

# Calculate Hubble Rates
t_array = numpy.linspace(0, te, 100)
H = []
for t in t_array:
    H.append( Hubble(alpha, beta, Ne, t) )

# Calculate derivative of Hubble Rate
dHdt = numpy.gradient(H,t)

# Calculate Ricci Scalar
R = []
for i in range(len(t_array)):
    if Ricci(H[i], dHdt[i]) < 0.0:
        R.append(1E-50)
    else:
        R.append( Ricci(H[i], dHdt[i]) )

# Calculate derivative of Hubble Rate
dRdt = numpy.gradient(R,t)

# Calculate second derivative of Hubble Rate
dR2dt2 = numpy.gradient(dRdt,t)

# First slow roll parameter epsilon_1 = -HDOT/H^2
E1 = []
for i in range(len(t_array)):
    E1.append( epsilon_1(H[i], dHdt[i]) )


# F
F = []
mu = pow(10, -1.0)*HS
for i in range(len(t_array)):
    log_R =  log( R[i]/pow(mu, 2) )
    F.append( 1 + (2*alpha + beta) * R[i] + 2*beta*R[i]*log_R )


# Calculate first derivative of F
dFdt = numpy.gradient(F,t)

# Calculate second derivative of F
dF2dt2 = numpy.gradient(dFdt,t)


# Thrird slow roll parameter epsilon_3
E3 = []
for i in range(len(t_array)):
    E3.append( epsilon_3(H[i], F[i], dFdt[i]))

E3.pop()
last_element = E3[-1]
E3.append(last_element)

# Fourth slow roll parameter epsilon_4
E4 = []
for i in range(len(t_array)):
    E4.append( epsilon_4(H[i], dFdt[i], dF2dt2[i]) )

E4.pop()
last_element = E4[-1]
E4.append(last_element)



# only append first value only for different value of beta

ns, r = spectral_index(E1[0], E3[0], E4[0])

print('ns = ', ns, 'r = ', r)



'''
+ 2 * beta * R[i] * log_R 
'''

'''
plt.figure()
plt.plot(t_array/t_P, H, '--', label='Hubble')
plt.legend()
plt.show()

plt.figure()
plt.plot(t_array/t_P, dHdt, '--', label='Hdot')
plt.legend()
plt.show()

plt.figure()
plt.plot(t_array/t_P, R, '--', label='Ricci')
plt.legend()
plt.show()

plt.figure()
plt.plot(t_array/t_P, dRdt, '--', label='Rdot')
plt.legend()
plt.show()

plt.figure()
plt.plot(t_array/t_P, dR2dt2, '--', label='R2dot')
plt.legend()
plt.show()


plt.figure()
plt.plot(t_array/t_P, E1, '--', label='epsilon-1')
plt.legend()
plt.show()

plt.figure()
plt.plot(t_array / t_P, F, '--', label='F')
plt.legend()
plt.show()

plt.figure()
plt.plot(t_array / t_P, dFdt, '--', label='Fdot')
plt.legend()
plt.show()

plt.figure()
plt.plot(t_array / t_P, dF2dt2, '--', label='F2dot')
plt.legend()
plt.show()



plt.figure()
plt.plot(t_array/t_P, E3, '--', label='epsilon-3')
plt.legend()
plt.show()

plt.figure()
plt.plot(t_array/t_P, E4, '--', label='epsilon-4')
plt.legend()
plt.show()


plt.figure()
plt.plot(t_array/t_P, ns, '--', label='ns')
plt.legend()
plt.show()

plt.figure()
plt.plot(t_array/t_P, r, '--', label='r')
plt.legend()
plt.show()

'''

'''
# Write data to text file
with open(filename + "." + filetype, "w") as para_file:
    para_file.write("Project Title: Reheating by Scalaron Decay\n")
    para_file.write("File Type: Data \n")
    para_file.write("Author: Arun Mathew\n")
    para_file.write("Affiliation: Dept. of Physics, IIT Guwahati, India\n\n")
    para_file.write("Data: Parameter Space\n\n")
    para_file.write("alpha, beta, n_s, r\n")

    for i in range(1, 100, 1):
        # for loop will generate the value of the parameter beta
        beta = (1 + i/10) * pow(10, 9) * pow(t_P, 2)

        HS = 1 / math.sqrt(12 * beta)
        H0 = HS * math.sqrt(1 - math.exp(-2 * beta * Ne / (3 * alpha)))
        E_1 = epsilon_1(alpha, beta, H0)
        E_3 = epsilon_3(alpha, beta, H0)
        E_4 = epsilon_3(alpha, beta, H0)
        ns, r = spectral_index(E_1, E_3, E_4)
        numpy.savetxt(para_file, numpy.c_[numpy.log10(alpha / pow(t_P, 2)),
                                          numpy.log10(beta / pow(t_P, 2)), ns, r], fmt="%f")

'''










