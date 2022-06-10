# Setting up the Field Equation file
# Author: Arun Mathew
from scipy import constants as const
import math
import numpy
from tools import logger

#####################################################################################
# set the logger tree-level
SDlogger = logger.setup_logger('FieldEqs')


#####################################################################################
# Common Physical Constants
c = const.c  # Speed of Light
G = const.G  #
pi = const.pi
hbar  = const.hbar
l_P  = math.sqrt(hbar*G/pow(c,3.0))
t_P  = l_P/c


#####################################################################################
# Model: f(R) = R + alpha R^2 + beta R^2 ln R/mu^2
class model():

    def __init__(self,
                 alpha,  # parameter alpha
                 beta,   # parameter beta
                 mu,     # parameter mu
                 E,      # Energy of the particle created
                 omega   # EoS parameter
                 ):
        self.alpha = alpha
        self.beta = beta
        self.mu = mu
        self.E = E
        self.omega = omega

        # Initializing Derived Parameters
        self.HS = 1 / math.sqrt(12 * beta)
        self.Ne = 60.0  # NUmber of e-foldings
        self.H0 = self.HS * math.sqrt(1 - math.exp(-2 * beta * self.Ne / (3 * alpha)))
        self.kappa = 8 * pi * G / pow(c, 2)
        self.Gamma = E * 1.60218 * pow(10, -10) / hbar

    # Initial Hubble rate slope
    def init_hubble_slope(self):
        return self.beta/(3*self.alpha)-1/(36*self.alpha*pow(self.H0,2))


    # Timescales involved in the field equation
    def timescales(self):
        tau_1 = 1 / (self.H0 * t_P)
        tau_osc = 2 * pi * math.sqrt(6 * self.alpha) / t_P
        tau_3 = 1 / (math.sqrt(self.kappa * pow(self.E, 4) * 2.0852 * pow(10, 37)) * t_P)
        tau_4 = 1 / (self.Gamma * t_P)
        return [tau_1, tau_osc, tau_3, tau_4]

    # Field Equations
    def field_eqs(self, t, Vector):

        tau_1 = self.timescales()[0]
        tau_osc = self.timescales()[1]
        tau_3 = self.timescales()[2]
        tau_4 = self.timescales()[3]

        # Assign Variables to the vector elements
        Xi = Vector[0]
        Psi = Vector[1]
        The = Vector[2]

        # Equations
        dXidt = Psi

        dPsidt = 2 * pow(pi, 2) * pow(tau_1 / tau_osc, 2) * pow(tau_1 / tau_3, 2) * The / (3 * Xi) \
                 - 2 * pow(pi, 2) * pow(tau_1 / tau_osc, 2) * Xi - 3 * Psi * Xi + 0.5 * pow(Psi, 2) / Xi \
                 + (self.beta/self.alpha) * (pow(Xi, 3.0) + 1.5 * Psi * Xi + 0.5 * pow(Psi, 2) / Xi)

        dThedt = - 3 * Xi * (1 + self.omega) * The + tau_1 / tau_4

        return [dXidt, dPsidt, dThedt]

    # Defining Ricci scalar and its derivatives from vector Xi, Psi and time span
    # Returns Ricci scalar in the units of H0^2
    def R(self, Xi, Psi):
        return 6 * (Psi + 2 * pow(Xi, 2))

    # Returns first derivative of Ricci scalar
    def dRdt(self, t, Xi, Psi):
        return 6 * (numpy.gradient(Psi, t) + 4 * Xi * Psi)

    # Returns second derivative of Ricci scalar
    def dR2dt2(self, t, Xi, Psi):
        dPsidt = numpy.gradient(Psi, t)
        dPsi2dt2 = numpy.gradient(dPsidt, t)
        return 6 * (dPsi2dt2 + 4 * pow(Psi, 2) + 4 * Xi * dPsidt)

    # Extra Inflationary Quantities
    # Slow-roll parameters
    # First slow roll parameter epsilon_1 = -HDOT/H^2
    def epsilon_1(self, Xi, Psi):
        return -Psi / pow(Xi, 2)

    # Third slow roll parameter epsilon_3 = FDOT/2HF
    def epsilon_3(self, t, Xi, Psi):
        for element in self.R(Xi, Psi): log_R = math.log(pow(self.H0, 2) * element / pow(self.mu, 2))
        F = 1 + pow(self.H0, 2)*(2*self.alpha + self.beta)*self.R(Xi, Psi) + 2*self.beta*pow(self.H0,2)*self.R(Xi, Psi)*log_R
        dFdt = pow(self.H0, 2)*(2*self.alpha+3*self.beta)*self.dRdt(t, Xi, Psi) + 2*self.beta*pow(self.H0, 2)*self.dRdt(t, Xi, Psi)*log_R
        return dFdt / (2 * Xi * F)

    # Fourth slow roll parameter epsilon_3 = FDDOT/HFDOT
    def epsilon_4(self, t, Xi, Psi):
        for element in self.R(Xi, Psi): log_R = math.log(pow(self.H0, 2)*element/pow(self.mu, 2))
        dFdt = pow(self.H0, 2)*(2*self.alpha+3*self.beta)* self.dRdt(t, Xi, Psi) + 2*self.beta * pow(self.H0, 2)*self.dRdt(t, Xi, Psi) * log_R
        dF2dt2 = pow(self.H0,2)*(2*self.alpha+3*self.beta)*self.dR2dt2(t,Xi,Psi) + 2*self.beta*pow(self.H0,2)*self.dR2dt2(t,Xi,Psi)*log_R + 2*self.beta*pow(self.H0,2)*pow(self.dRdt(t,Xi,Psi), 2)/self.R(Xi, Psi)
        return dF2dt2 / (Xi * dFdt)

    def spectral_index(self, t, Xi, Psi):
        e1 = self.epsilon_1(Xi, Psi)[0]
        e3 = self.epsilon_3(t, Xi, Psi)[0]
        e4 = self.epsilon_4(t, Xi, Psi)[0]

        ns = 4 - 2 * math.sqrt(0.25 + (1 + e1 - e3 + e4) * (2 - e3 + e4) / pow(1 - e3, 2))
        r = 48 * pow(e3, 2) / pow(1 + e3, 2)
        return ns, r



#####################################################################################
#####################################################################################

