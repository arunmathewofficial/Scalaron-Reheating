# Setting up class file for the region of Inflation
# Author: Arun Mathew
from scipy.integrate import solve_ivp
from fieldeqs import *
from tools import logger
import matplotlib.pyplot as plt
import numpy
import os


# > set the logger tree-level
SDlogger = logger.setup_logger('Inflation')

class inflation():

    #####################################################################################
    def __init__(self, model_object, output_file):
        SDlogger.info('Setting up initial attributes for Inflation.')
        self.model_object = model_object # create a object for the class model
        self.output_file = output_file
        # Initial Conditions for Inflation
        init_cond = [
            1,  # Initial value of Hubble rate in the units of H0
            model_object.init_hubble_slope(), # Initial value of Hubble dot in the unit of H0t0
            0 # Initial value of Density in the units of E^4
        ]
        SDlogger.info('Inflation - Initial Conditions : [%f,%f,%f].', init_cond[0], init_cond[1], init_cond[2])
        # Inflation Time vector
        start_time = 0
        end_time = model_object.timescales()[0]*50
        step_size = model_object.timescales()[0]/50
        num_steps = int((end_time-start_time)/step_size)
        self.IC = init_cond
        self.tvector = numpy.linspace(start=0, stop=end_time, num=num_steps)
        self.tspan = [start_time, end_time]



    #####################################################################################
    def stop_condition(self, t, y):
        # Event: integration stops for when epsilon_1 > 1
        return 0 if self.model_object.epsilon_1(y[0], y[1]) > 1 else 1

    stop_condition.terminal = True



    #####################################################################################
    def inflation_solver(self):
        t_points  = self.tvector
        IC = self.IC
        tspan = self.tspan

        sol = solve_ivp(self.model_object.field_eqs, tspan, IC, t_eval=t_points,
                        method='LSODA',atol=1e-15,rtol=1e-13,
                        events= [self.stop_condition,] # Stopping Condition for integration
                        )

        inf_tspan = sol.t

        if sol.status == -1:
            Status_flag = 'Failed'
            SDlogger.error('%s', sol.message)
        elif sol.status == 0:
            Status_flag = 'OK'
            SDlogger.info('%s', sol.message)
        elif sol.status == 1:
            Status_flag = 'OK'
            SDlogger.info('%s epsilon_1 = 1.', sol.message)
            SDlogger.info('Inflation ends at t_e = %f t_Planck.', inf_tspan[-1])

        Xi       = sol.y[0]
        Psi      = sol.y[1]
        The      = sol.y[2]

        Ricci = self.model_object.R(Xi, Psi)
        Epsilon_1 = self.model_object.epsilon_1(Xi, Psi)
        Epsilon_3 = self.model_object.epsilon_3(inf_tspan, Xi, Psi)
        Epsilon_4 = self.model_object.epsilon_4(inf_tspan, Xi, Psi)

        n_s = self.model_object.spectral_index(inf_tspan, Xi, Psi)[0]
        r   = self.model_object.spectral_index(inf_tspan, Xi, Psi)[1]

        # Path of data directory
        root_Dir = os.path.normpath(os.getcwd() + os.sep + os.pardir)
        data_Dir = root_Dir + "/op_data"
        # Filename and File Type
        filename = self.output_file
        filetype = "txt"

        if(filename != 'None'):
            # Write data to text file if a filename is given
            SDlogger.info('Writting inflation data to file %s.', filename)
            with open(data_Dir + "/" + filename + "." + filetype, "w") as inf_file:
                inf_file.write("Project Title: Reheating by Scalaron Decay\n")
                inf_file.write("File Type: Data \n")
                inf_file.write("Author: Arun Mathew\n")
                inf_file.write("Affiliation: Dept. of Physics, IIT Guwahati, India\n\n")
                inf_file.write("Data: Inflation Background Data\n")
                inf_file.write("Model Parameters :\n")
                print("alpha = ", "{0:.2e}".format(self.model_object.alpha / pow(t_P, 2)), "[t_P^2]", file=inf_file)
                print("beta  = ", "{0:.2e}".format(self.model_object.beta / pow(t_P, 2)), "[t_P^2]", file=inf_file)
                print("mu    = ", "{0:.2e}".format(self.model_object.mu * t_P), "[t_P^-1]", file=inf_file)
                print("E     = ", "{0:.2e}".format(self.model_object.E), "[GeV]", file=inf_file)
                print("omega = ", "{0:.2e}".format(self.model_object.omega), file=inf_file)
                print("\n", file=inf_file)
                print("Time, Xi, Psi, Theta, Ricci, epsilon_1, epsilon_3, epsilon_4\n", file=inf_file)
                numpy.savetxt(inf_file, numpy.c_[inf_tspan, Xi, Psi, The, Ricci, Epsilon_1, Epsilon_3, Epsilon_4],
                              fmt="%f")
                print("\n", file=inf_file)
                print("Scalar Spectral Index and Tensor-to-Scalar ratio:", file=inf_file)
                print("n_s = ", "{0:.4f}".format(n_s), file=inf_file)
                print("r   = ", "{0:.4f}".format(r), file=inf_file)

         # plot the results
        fig, ax = plt.subplots(figsize=(4.5, 3), dpi=100)
        ax.plot(inf_tspan, Epsilon_1, label='$\epsilon_1$')
        ax.plot(inf_tspan, Epsilon_3, label='$\epsilon_3$')
        # plt.xlim([0, 10])
        plt.xlim([0, inf_tspan[-1]])
        # plt.ylim([-0.01, 1])
        ax.plot(inf_tspan, Epsilon_4, '--', label='$\epsilon_4$')
        # ax.plot(t, Theta, label='Theta')
        plt.xlabel('t')
        plt.legend()
        plt.tight_layout()
        plt.savefig('Slow-roll_parameters.png')
        plt.show()

        return inf_tspan, Xi, Psi, The, Ricci, Epsilon_1, Epsilon_3, Epsilon_4, n_s, r, Status_flag








        # must retun the final values

        #####################################################################################
        #####################################################################################















